# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.international_wire_australia_specific_data import InternationalWireAustraliaSpecificData
from mercury_banking.models.international_wire_brazil_specific_data import InternationalWireBrazilSpecificData
from mercury_banking.models.international_wire_canada_specific_data import InternationalWireCanadaSpecificData
from mercury_banking.models.international_wire_chile_specific_data import InternationalWireChileSpecificData
from mercury_banking.models.international_wire_colombia_specific_data import InternationalWireColombiaSpecificData
from mercury_banking.models.international_wire_dominican_republic_specific_data import (
    InternationalWireDominicanRepublicSpecificData,
)
from mercury_banking.models.international_wire_honduras_specific_data import InternationalWireHondurasSpecificData
from mercury_banking.models.international_wire_india_specific_data import InternationalWireIndiaSpecificData
from mercury_banking.models.international_wire_kazakhstan_specific_data import InternationalWireKazakhstanSpecificData
from mercury_banking.models.international_wire_pakistan_specific_data import InternationalWirePakistanSpecificData
from mercury_banking.models.international_wire_paraguay_specific_data import InternationalWireParaguaySpecificData
from mercury_banking.models.international_wire_philippines_specific_data import InternationalWirePhilippinesSpecificData
from mercury_banking.models.international_wire_russia_specific_data import InternationalWireRussiaSpecificData
from mercury_banking.models.international_wire_south_africa_specific_data import (
    InternationalWireSouthAfricaSpecificData,
)
from mercury_banking._runtime import ApiModel


class InternationalWireCountrySpecificData(ApiModel):
    """InternationalWireCountrySpecificData model."""

    australia: Optional[InternationalWireAustraliaSpecificData] = None
    brazil: Optional[InternationalWireBrazilSpecificData] = None
    canada: Optional[InternationalWireCanadaSpecificData] = None
    chile: Optional[InternationalWireChileSpecificData] = None
    colombia: Optional[InternationalWireColombiaSpecificData] = None
    dominican_republic: Optional[InternationalWireDominicanRepublicSpecificData] = Field(
        default=None, alias="dominicanRepublic"
    )
    honduras: Optional[InternationalWireHondurasSpecificData] = None
    india: Optional[InternationalWireIndiaSpecificData] = None
    kazakhstan: Optional[InternationalWireKazakhstanSpecificData] = None
    pakistan: Optional[InternationalWirePakistanSpecificData] = None
    paraguay: Optional[InternationalWireParaguaySpecificData] = None
    philippines: Optional[InternationalWirePhilippinesSpecificData] = None
    russia: Optional[InternationalWireRussiaSpecificData] = None
    south_africa: Optional[InternationalWireSouthAfricaSpecificData] = Field(default=None, alias="southAfrica")
