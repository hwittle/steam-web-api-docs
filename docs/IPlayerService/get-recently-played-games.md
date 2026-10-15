---
title: GetRecentlyPlayedGames
description: Returns the games a Steam account has played in the last two weeks, with playtime for each.
interface: IPlayerService
method: GetRecentlyPlayedGames
version: v0001
http_method: GET
auth: api_key
formats: [json, xml, vdf]
privacy: public_or_owner
last_verified: 15 October 2026
tags:
  - IPlayerService
  - games
  - privacy-dependent
---

# GetRecentlyPlayedGames <span class="p_version">`v0001`</span>

Returns the games an account has played in the last two weeks, with playtime for each. The account's data must be visible to you, unless the API key belongs to the account you are asking about.

{{ glance() }}

## Request

```
GET https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/
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

---

{{ param("count", "uint32", "Maximum number of games to return. When omitted, every game played in the last two weeks is returned.") }}

</div>

<div markdown>

### Example Request

#### Minimal

=== "Readable"
    ```
    https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=YOUR_API_KEY&format=json&input_json={"steamid": 76561199101839601}
    ```

=== "URL-encoded"
    ```
    https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=YOUR_API_KEY&format=json&input_json=%7B%22steamid%22%3A%2076561199101839601%7D
    ```

#### Full

=== "Readable"
    ```
    https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=YOUR_API_KEY&format=json&input_json={"steamid": 76561199101839601, "count":3}
    ```

=== "URL-encoded"
    ```
    https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=YOUR_API_KEY&format=json&input_json=%7B%22steamid%22%3A%2076561199101839601%2C%20%22count%22%3A3%7D
    ```

</div>

</div>

<div class="ref-grid" markdown>

<div markdown>

### Response

A list of games the user has played in the last two weeks. Nothing is returned if the profile is not publicly visible.

{{ param("total_count", "uint32", "Number of games the account played in the last two weeks. This value is not affected by `count`, so it can be larger than the number of objects in `games`.") }}

{{ param("games", "Game[]", "One object per game, with the fields below.") }}

{{ param_bullet("appid", "uint32", "The game's app ID.") }}
{{ param_bullet("name", "string", "The game's title.") }}
{{ param_bullet("playtime_2weeks", "int64", "Minutes played in the last two weeks.") }}
{{ param_bullet("playtime_forever", "int64", "Total minutes played on record.") }}
{{ param_bullet("img_icon_url", "string", "Hash used to build the game's icon URL.", "Icon URL pattern: `https://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{hash}.jpg`") }}

</div>

<div markdown>

### Example Response

=== "JSON"
    ```json
    {
        "response": {
            "total_count": 20,
            "games": [
                {
                    "appid": 1086940,
                    "name": "Baldur's Gate 3",
                    "playtime_2weeks": 1083,
                    "playtime_forever": 40067,
                    "img_icon_url": "d866cae7ea1e471fdbc206287111f1b642373bd9"
                },
                {
                    "appid": 2767030,
                    "name": "Marvel Rivals",
                    "playtime_2weeks": 583,
                    "playtime_forever": 7621,
                    "img_icon_url": "839b4712925b95702ca56e0c4d399adf54f4d617"
                },
                {
                    "appid": 21690,
                    "name": "Resident Evil 5",
                    "playtime_2weeks": 542,
                    "playtime_forever": 1922,
                    "img_icon_url": "26108f5caff3638c9f522dd79ee84a12761f373a"
                }
            ]
        }
    }
    ```
=== "XML"
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE response>
    <response>
        <total_count>20</total_count>
        <games>
            <message>
                <appid>1086940</appid>
                <name>Baldur&apos;s Gate 3</name>
                <playtime_2weeks>1083</playtime_2weeks>
                <playtime_forever>40067</playtime_forever>
                <img_icon_url>d866cae7ea1e471fdbc206287111f1b642373bd9</img_icon_url>
            </message>
            <message>
                <appid>2767030</appid>
                <name>Marvel Rivals</name>
                <playtime_2weeks>583</playtime_2weeks>
                <playtime_forever>7621</playtime_forever>
                <img_icon_url>839b4712925b95702ca56e0c4d399adf54f4d617</img_icon_url>
            </message>
            <message>
                <appid>21690</appid>
                <name>Resident Evil 5</name>
                <playtime_2weeks>542</playtime_2weeks>
                <playtime_forever>1922</playtime_forever>
                <img_icon_url>26108f5caff3638c9f522dd79ee84a12761f373a</img_icon_url>
            </message>
        </games>
    </response>
    ```
=== "VDF"
    ```
    "response"
    {
        "total_count"	"20"
        "games"
        {
            "0"
            {
                "appid"	"1086940"
                "name"	"Baldur's Gate 3"
                "playtime_2weeks"	"1083"
                "playtime_forever"	"40067"
                "img_icon_url"	"d866cae7ea1e471fdbc206287111f1b642373bd9"
            }
            "1"
            {
                "appid"	"2767030"
                "name"	"Marvel Rivals"
                "playtime_2weeks"	"583"
                "playtime_forever"	"7621"
                "img_icon_url"	"839b4712925b95702ca56e0c4d399adf54f4d617"
            }
            "2"
            {
                "appid"	"21690"
                "name"	"Resident Evil 5"
                "playtime_2weeks"	"542"
                "playtime_forever"	"1922"
                "img_icon_url"	"26108f5caff3638c9f522dd79ee84a12761f373a"
            }
        }
    }
    ```
    
!!! note "Format differences"
    XML wraps each game in a `message` element, and VDF uses numbered keys with string values.

</div>

</div>