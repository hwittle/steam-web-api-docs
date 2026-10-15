---
title: GetOwnedGames
description: Returns the games a Steam account owns, with playtime for each game.
interface: IPlayerService
method: GetOwnedGames
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

# GetOwnedGames <span class="p_version">`v0001`</span>

Returns a list of games a Steam account owns. What comes back depends on the targeted account's privacy settings in relation to your Steam account.

{{ glance() }}

## Request

```
GET https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/
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

{{ param("include_appinfo", "bool", "When true, each game also includes its name and image hashes. When omitted, the response contains only app IDs and playtime fields.") }}

---

{{ param("include_played_free_games", "bool", "When true, free games the account has played are included. They are left out by default.") }}

---

{{ param("appids_filter", "uint32", "Limits the response to the listed app IDs.") }}

</div>

<div markdown>

### Example Request

#### Minimal

=== "Readable"
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json={"steamid": 76561199101839601}
    ```

=== "URL-encoded"
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json=%7B%22steamid%22%3A%2076561199101839601%7D
    ```

#### Full

=== "Readable"
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json={"steamid": 76561199101839601, "include_appinfo":true, "include_played_free_games": true, "appids_filter":[4000, 21690, 22330]}
    ```

=== "URL-encoded"
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json=%7B%22steamid%22%3A%2076561199101839601%2C%20%22include_appinfo%22%3Atrue%2C%20%22include_played_free_games%22%3A%20true%2C%20%22appids_filter%22%3A%5B4000%2C%2021690%2C%2022330%5D%7D
    ```

</div>

</div>

<div class="ref-grid" markdown>

<div markdown>

### Response

The response is a single `response` object. If the account's game details are hidden from you, it is empty. Which fields each game includes depends on the parameters you send, such as `include_appinfo`.

{{ param("game_count", "uint32", "Number of games in the response. Includes played free games when `include_played_free_games` is set. When `appids_filter` is used, it counts only the filtered games.") }}

{{ param("games", "Game[]", "One object per game, with the fields below.") }}

{{ param_bullet("appid", "uint32", "The game's app ID.") }}
{{ param_bullet("name", "string", "The game's title. Present when `include_appinfo` is set.") }}
{{ param_bullet("playtime_forever", "int64", "Total minutes played on record.") }}
{{ param_bullet("playtime_2weeks", "int64", "Minutes played in the last two weeks. Appears only for games played in that period.") }}
{{ param_bullet("img_icon_url", "string", "Hash used to build the game's icon URL. Present when `include_appinfo` is set.", "Icon URL pattern: `https://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{hash}.jpg`") }}
{{ param_bullet("has_community_visible_stats", "bool", "Whether the game has a public stats page. Appears only for some games. Returned as `true` in JSON and XML, and as the string `1` in VDF.", "Stats page URL pattern: `https://steamcommunity.com/profiles/{steamid}/stats/{appid}`") }}
{{ param_bullet("has_leaderboards", "bool", "Appears only for some games.") }}
{{ param_bullet("content_descriptorids", "uint32[]", "Appears only for some games with mature content. The list of ids can be found under [EUGCContentDescriptorID](https://partner.steamgames.com/doc/api/ISteamUGC#EUGCContentDescriptorID).") }}

</div>

<div markdown>

### Example Response

=== "JSON"
    ```json
    {
        "response": {
            "game_count": 3,
            "games": [
                {
                    "appid": 4000,
                    "name": "Garry's Mod",
                    "playtime_forever": 102,
                    "img_icon_url": "4a6f25cfa2426445d0d9d6e233408de4d371ce8b",
                    "has_community_visible_stats": true
                },
                {
                    "appid": 21690,
                    "name": "Resident Evil 5",
                    "playtime_2weeks": 542,
                    "playtime_forever": 1922,
                    "img_icon_url": "26108f5caff3638c9f522dd79ee84a12761f373a",
                    "has_community_visible_stats": true,
                    "has_leaderboards": true
                },
                {
                    "appid": 22330,
                    "name": "The Elder Scrolls IV: Oblivion Game of the Year Edition (2009)",
                    "playtime_forever": 51,
                    "img_icon_url": "e33402f6e1e4ed6dd001c7add26934f345cbd31e",
                    "content_descriptorids": [
                        2,
                        5
                    ]
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
        <game_count>3</game_count>
        <games>
            <message>
                <appid>4000</appid>
                <name>Garry&apos;s Mod</name>
                <playtime_forever>102</playtime_forever>
                <img_icon_url>4a6f25cfa2426445d0d9d6e233408de4d371ce8b</img_icon_url>
                <has_community_visible_stats>true</has_community_visible_stats>
            </message>
            <message>
                <appid>21690</appid>
                <name>Resident Evil 5</name>
                <playtime_2weeks>542</playtime_2weeks>
                <playtime_forever>1922</playtime_forever>
                <img_icon_url>26108f5caff3638c9f522dd79ee84a12761f373a</img_icon_url>
                <has_community_visible_stats>true</has_community_visible_stats>
                <has_leaderboards>true</has_leaderboards>
            </message>
            <message>
                <appid>22330</appid>
                <name>The Elder Scrolls IV: Oblivion Game of the Year Edition (2009)</name>
                <playtime_forever>51</playtime_forever>
                <img_icon_url>e33402f6e1e4ed6dd001c7add26934f345cbd31e</img_icon_url>
                <content_descriptorids>
                    <uint32>2</uint32>
                    <uint32>5</uint32>
                </content_descriptorids>
            </message>
        </games>
    </response>
    ```

=== "VDF"
    ```
    "response"
    {
        "game_count"	"3"
        "games"
        {
            "0"
            {
                "appid"	"4000"
                "name"	"Garry's Mod"
                "playtime_forever"	"102"
                "img_icon_url"	"4a6f25cfa2426445d0d9d6e233408de4d371ce8b"
                "has_community_visible_stats"	"1"
            }
            "1"
            {
                "appid"	"21690"
                "name"	"Resident Evil 5"
                "playtime_2weeks"	"542"
                "playtime_forever"	"1922"
                "img_icon_url"	"26108f5caff3638c9f522dd79ee84a12761f373a"
                "has_community_visible_stats"	"1"
                "has_leaderboards"	"1"
            }
            "2"
            {
                "appid"	"22330"
                "name"	"The Elder Scrolls IV: Oblivion Game of the Year Edition (2009)"
                "playtime_forever"	"51"
                "img_icon_url"	"e33402f6e1e4ed6dd001c7add26934f345cbd31e"
                "content_descriptorids"
                {
                    "0"	"2"
                    "1"	"5"
                }
            }
        }
    }
    ```

!!! note "Format differences"
    XML wraps each game in a `message` element, and VDF uses numbered keys with string values.

</div>

</div>