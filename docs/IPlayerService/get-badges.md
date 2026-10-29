---
title: GetBadges
description: Returns a list of badges obtained from a Steam account.
interface: IPlayerService
method: GetBadges
version: v0001
http_method: GET
auth: api_key
formats: [json, xml, vdf]
privacy: public
last_verified: 28 October 2026
tags:
  - IPlayerService
  - badges
  - public
---

# GetOwnedGames <span class="p_version">`v0001`</span>

Returns a list of badges obtained from a Steam account, account's current xp, level, xp needed to level up, and current number of xp, regardless of privacy.

{{ glance() }}

## Request

```
GET https://api.steampowered.com/IPlayerService/GetBadges/v0001/
```
{{ service_note() }}

<div class="ref-grid" markdown>

<div markdown>

### Parameters

{{ param("key", "string", "Your Steam Web API key.", required=True) }}

---

{{ param("format", "string", "Response format: `json` (default), `xml`, or `vdf`.") }}

---

{{ param("steamid", "uint64", "The 64-bit Steam ID of the account to look up.", required=True) }}

</div>

<div markdown>

### Example Request

=== "Readable"
    ```
    https://api.steampowered.com/IPlayerService/GetBadges/v0001/?key=YOUR_API_KEY&format=json&input_json={"steamid": 76561199101839601}
    ```

=== "URL-encoded"
    ```
    https://api.steampowered.com/IPlayerService/GetBadges/v0001/?key=YOUR_API_KEY&format=json&input_json=%7B%22steamid%22%3A%2076561199101839601%7D
    ```

</div>

</div>

<div class="ref-grid" markdown>

<div markdown>

### Response

The response is a single `response` object.

{{ param("badgeid", "uint32", "The id number of the badge.") }}

{{ param("level", "uint32", "Assigned level of the badge.") }}

{{ param("completion_time", "uint64", "Date and time the badge was obtained.") }}

{{ param("xp", "uint32", "Amount of experience points granted to Steam account's level when obtained.") }}

{{ param("scarcity", "uint32", "Amount of Steam accounts that have unlocked at least level 1 of this badge.") }}

</div>

<div markdown>

### Example Response

=== "JSON"
    ```json
    {
        "response": {
            "badges": [
                {
                    "badgeid": 13,
                    "level": 115,
                    "completion_time": 1793030917,
                    "xp": 342,
                    "scarcity": 18835621
                },
                {
                    "badgeid": 69,
                    "level": 1,
                    "completion_time": 1766031310,
                    "xp": 50,
                    "scarcity": 32013466
                },
                {
                    "badgeid": 70,
                    "level": 4,
                    "completion_time": 1764537295,
                    "xp": 100,
                    "scarcity": 1963536
                },
            ...
            ],
            "player_xp": 1742,
            "player_level": 13,
            "player_xp_needed_to_level_up": 58,
            "player_xp_needed_current_level": 1600
        }
    }
    ```

=== "XML"
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE response>
    <response>
        <badges>
            <message>
                <badgeid>13</badgeid>
                <level>115</level>
                <completion_time>1793030917</completion_time>
                <xp>342</xp>
                <scarcity>18835621</scarcity>
            </message>
            <message>
                <badgeid>69</badgeid>
                <level>1</level>
                <completion_time>1766031310</completion_time>
                <xp>50</xp>
                <scarcity>32013466</scarcity>
            </message>
            <message>
                <badgeid>70</badgeid>
                <level>4</level>
                <completion_time>1764537295</completion_time>
                <xp>100</xp>
                <scarcity>1963536</scarcity>
            </message>
            ...
        </badges>
        <player_xp>1742</player_xp>
        <player_level>13</player_level>
        <player_xp_needed_to_level_up>58</player_xp_needed_to_level_up>
        <player_xp_needed_current_level>1600</player_xp_needed_current_level>
    </response>
    ```

=== "VDF"
    ```
    "response"
    {
        "badges"
        {
            "0"
            {
                "badgeid"	"13"
                "level"	"115"
                "completion_time"	"1793030917"
                "xp"	"342"
                "scarcity"	"18835621"
            }
            "1"
            {
                "badgeid"	"69"
                "level"	"1"
                "completion_time"	"1766031310"
                "xp"	"50"
                "scarcity"	"32013466"
            }
            "2"
            {
                "badgeid"	"70"
                "level"	"4"
                "completion_time"	"1764537295"
                "xp"	"100"
                "scarcity"	"1963536"
            }
            "3"
            {
                "badgeid"	"2"
                "level"	"3"
                "completion_time"	"1749998689"
                "xp"	"500"
                "scarcity"	"12164392"
            }
            ...
        }
        "player_xp"	"1742"
        "player_level"	"13"
        "player_xp_needed_to_level_up"	"58"
        "player_xp_needed_current_level"	"1600"
    }
    ```

!!! note "Format differences"
    XML wraps each badge in a `message` element, and VDF uses numbered keys with string values.

</div>

</div>