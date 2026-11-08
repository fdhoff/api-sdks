// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ShopHolidayPreference } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getHolidayPreferences: Operation = {
  id: 'getHolidayPreferences',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/holiday-preferences',
  resource: 'holidayPreferences',
  name: 'list',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'path' }],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_r'] },
    ],
  ],
};

const updateHolidayPreferences: Operation = {
  id: 'updateHolidayPreferences',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}/holiday-preferences/{holiday_id}',
  resource: 'holidayPreferences',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'holiday_id', name: 'holidayId', location: 'path' },
    { wire: 'is_working', name: 'isWorking', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [getHolidayPreferences, updateHolidayPreferences];

export class HolidayPreferencesApi extends Resource {
  /** List a shop's holiday preferences. */
  list(shopId: number, options?: RequestOptions): Promise<Array<ShopHolidayPreference>> {
    return this.call(getHolidayPreferences, undefined, { shopId }, options);
  }

  /** Update a shop's preference for one holiday. */
  update(
    shopId: number,
    holidayId:
      | 1
      | 2
      | 3
      | 4
      | 5
      | 6
      | 7
      | 8
      | 9
      | 10
      | 11
      | 12
      | 13
      | 14
      | 15
      | 16
      | 17
      | 18
      | 19
      | 20
      | 21
      | 22
      | 23
      | 24
      | 25
      | 26
      | 27
      | 28
      | 29
      | 30
      | 31
      | 32
      | 33
      | 34
      | 35
      | 36
      | 37
      | 38
      | 39
      | 40
      | 41
      | 42
      | 43
      | 44
      | 45
      | 46
      | 47
      | 48
      | 49
      | 50
      | 51
      | 52
      | 53
      | 54
      | 55
      | 56
      | 57
      | 58
      | 59
      | 60
      | 61
      | 62
      | 63
      | 64
      | 65
      | 66
      | 67
      | 68
      | 69
      | 70
      | 71
      | 72
      | 73
      | 74
      | 75
      | 76
      | 77
      | 78
      | 79
      | 80
      | 81
      | 82
      | 83
      | 84
      | 85
      | 86
      | 87
      | 88
      | 89
      | 90
      | 91
      | 92
      | 93
      | 94
      | 95
      | 96
      | 97
      | 98
      | 99
      | 100
      | 101
      | 102
      | 103
      | 104
      | 105,
    params: { isWorking: boolean },
    options?: RequestOptions,
  ): Promise<ShopHolidayPreference> {
    return this.call(updateHolidayPreferences, undefined, { shopId, holidayId, ...params }, options);
  }
}
