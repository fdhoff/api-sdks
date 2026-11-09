use serde::de::DeserializeOwned;
use serde::{Deserialize, Deserializer, Serialize};
use serde_json::{Map, Value};

use super::request::{File, Part};

/// An object's fields while a model is decoded or encoded. A field leaves the map only when its
/// value fits, so a null, a value of the wrong type and an unknown field all stay behind.
pub struct Fields(Map<String, Value>);

impl Fields {
    pub fn new(extra: &Map<String, Value>) -> Self {
        Self(extra.clone())
    }

    pub fn take<T: DeserializeOwned>(&mut self, name: &str) -> Option<T> {
        let value = self.0.get(name).filter(|value| !value.is_null())?;
        let parsed = T::deserialize(value).ok()?;
        self.0.remove(name);
        Some(parsed)
    }

    /// Sets a field, so a field set after decoding wins over what `extra` holds for it.
    pub fn put<T: Serialize>(&mut self, name: &str, value: &Option<T>) -> serde_json::Result<()> {
        if let Some(value) = value {
            self.0.insert(name.to_owned(), serde_json::to_value(value)?);
        }
        Ok(())
    }

    pub fn into_extra(self) -> Map<String, Value> {
        self.0
    }
}

/// Only a value that is not an object at all fails to decode.
impl<'de> Deserialize<'de> for Fields {
    fn deserialize<D: Deserializer<'de>>(deserializer: D) -> Result<Self, D::Error> {
        Ok(Self(
            Option::<Map<String, Value>>::deserialize(deserializer)?.unwrap_or_default(),
        ))
    }
}

/// A value that can be sent as multipart form fields.
pub trait FormValue {
    fn parts(&self, name: &str, parts: &mut Vec<Part>);
}

impl<T: FormValue> FormValue for Option<T> {
    fn parts(&self, name: &str, parts: &mut Vec<Part>) {
        if let Some(value) = self {
            value.parts(name, parts);
        }
    }
}

impl<T: FormValue> FormValue for Vec<T> {
    fn parts(&self, name: &str, parts: &mut Vec<Part>) {
        for value in self {
            value.parts(name, parts);
        }
    }
}

impl FormValue for File {
    fn parts(&self, name: &str, parts: &mut Vec<Part>) {
        parts.push(Part::File {
            name: name.to_owned(),
            file: self.clone(),
        });
    }
}

/// Sends a value as text, or as JSON when it is an object.
pub fn text_part(name: &str, value: &impl Serialize, parts: &mut Vec<Part>) {
    if let Some(text) = super::request::text(&super::request::param_value(value)) {
        parts.push(Part::Text {
            name: name.to_owned(),
            value: text,
        });
    }
}

macro_rules! text_form_values {
    ($($type:ty),*) => {
        $(impl FormValue for $type {
            fn parts(&self, name: &str, parts: &mut Vec<Part>) {
                text_part(name, self, parts);
            }
        })*
    };
}

text_form_values!(String, bool, i32, i64, f64, Value);

/// Decodes a model tolerantly, because the spec has not been confirmed against the live API: a
/// value that does not fit its field leaves the field `None` and stays in `extra`, as do unknown
/// fields and nulls. Encoding writes `extra`, then every field that is set.
macro_rules! tolerant_model {
    ($model:ident { $($field:ident: $wire:literal),* $(,)? }) => {
        impl<'de> serde::Deserialize<'de> for $model {
            fn deserialize<D: serde::Deserializer<'de>>(deserializer: D) -> Result<Self, D::Error> {
                #[allow(unused_mut)]
                let mut fields = <$crate::runtime::Fields as serde::Deserialize>::deserialize(deserializer)?;
                Ok(Self { $($field: fields.take($wire),)* extra: fields.into_extra() })
            }
        }

        impl serde::Serialize for $model {
            fn serialize<S: serde::Serializer>(&self, serializer: S) -> Result<S::Ok, S::Error> {
                #[allow(unused_mut)]
                let mut fields = $crate::runtime::Fields::new(&self.extra);
                $(fields.put($wire, &self.$field).map_err(serde::ser::Error::custom)?;)*
                serde::Serialize::serialize(&fields.into_extra(), serializer)
            }
        }

        impl $crate::runtime::FormValue for $model {
            fn parts(&self, name: &str, parts: &mut Vec<$crate::runtime::Part>) {
                $crate::runtime::text_part(name, self, parts);
            }
        }
    };
}

/// An enumeration that keeps a value it does not list in `Unlisted`, so a new value from the API
/// does not fail a whole response.
#[allow(unused_macros, reason = "an API may declare no enumerations")]
macro_rules! open_enum {
    ($(#[$meta:meta])* $name:ident: $repr:ty { $($variant:ident = $value:literal),* $(,)? }) => {
        $(#[$meta])*
        #[derive(Clone, Debug, PartialEq, Eq, Hash)]
        #[non_exhaustive]
        pub enum $name {
            $($variant,)*
            /// A value this version does not list.
            Unlisted($repr),
        }

        impl serde::Serialize for $name {
            fn serialize<S: serde::Serializer>(&self, serializer: S) -> Result<S::Ok, S::Error> {
                match self {
                    $(Self::$variant => serde::Serialize::serialize(&$value, serializer),)*
                    Self::Unlisted(value) => serde::Serialize::serialize(value, serializer),
                }
            }
        }

        impl<'de> serde::Deserialize<'de> for $name {
            fn deserialize<D: serde::Deserializer<'de>>(deserializer: D) -> Result<Self, D::Error> {
                let value = <$repr as serde::Deserialize>::deserialize(deserializer)?;
                $(if value == $value {
                    return Ok(Self::$variant);
                })*
                Ok(Self::Unlisted(value))
            }
        }

        impl $crate::runtime::FormValue for $name {
            fn parts(&self, name: &str, parts: &mut Vec<$crate::runtime::Part>) {
                $crate::runtime::text_part(name, self, parts);
            }
        }
    };
}

pub(crate) use {open_enum, tolerant_model};

#[cfg(test)]
mod tests {
    use serde_json::json;

    use super::*;

    #[derive(Debug, Default, PartialEq)]
    struct Sample {
        id: Option<i64>,
        r#type: Option<String>,
        extra: Map<String, Value>,
    }

    tolerant_model!(Sample {
        id: "id",
        r#type: "type"
    });

    open_enum!(Colour: String { Red = "red" });

    #[test]
    fn a_value_that_does_not_fit_stays_in_extra() {
        let sample: Sample =
            serde_json::from_value(json!({"id": "x", "type": "a", "more": null})).unwrap();
        assert_eq!(sample.id, None);
        assert_eq!(sample.r#type.as_deref(), Some("a"));
        assert_eq!(
            sample.extra,
            json!({"id": "x", "more": null})
                .as_object()
                .unwrap()
                .clone()
        );
        assert_eq!(
            serde_json::to_value(&sample).unwrap(),
            json!({"id": "x", "type": "a", "more": null})
        );
    }

    #[test]
    fn a_field_set_after_decoding_wins() {
        let mut sample: Sample = serde_json::from_value(json!({"id": "x"})).unwrap();
        sample.id = Some(2);
        assert_eq!(serde_json::to_value(&sample).unwrap(), json!({"id": 2}));
    }

    #[test]
    fn only_a_value_that_is_not_an_object_fails() {
        assert_eq!(
            serde_json::from_value::<Sample>(Value::Null).unwrap(),
            Sample::default()
        );
        assert!(serde_json::from_value::<Sample>(json!([1])).is_err());
    }

    #[test]
    fn an_unlisted_enum_value_is_kept() {
        assert_eq!(
            serde_json::from_value::<Colour>(json!("red")).unwrap(),
            Colour::Red
        );
        let other: Colour = serde_json::from_value(json!("blue")).unwrap();
        assert_eq!(other, Colour::Unlisted("blue".to_owned()));
        assert_eq!(serde_json::to_value(other).unwrap(), json!("blue"));
    }
}
