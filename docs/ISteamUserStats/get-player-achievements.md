---
title: GetPlayerAchievements
description: Returns the achievements an account has unlocked, or not yet unlocked, in one game.
interface: ISteamUserStats
method: GetPlayerAchievements
version: v0001
http_method: GET
auth: api_key
formats: [json, xml, vdf]
privacy: public_or_owner
last_verified: 27 October 2026
tags:
  - ISteamUserStats
  - achievements
  - privacy-dependent
---

# GetPlayerAchievements <span class="p_version">`v0001`</span>

Returns the achievements for one game on a Steam account, with the unlock time for each one that has been completed. The account's game details must be visible to you, unless the API key belongs to the account you are asking about.

{{ glance() }}

## Request

```
GET https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/
```

<div class="ref-grid" markdown>

<div markdown>

### Parameters

{{ param("key", "string", "Your Steam Web API key.", required=True) }}

---

{{ param("format", "string", "Response format: `json` (default), `xml`, or `vdf`.") }}

---

{{ param("steamid", "uint64", "The 64-bit Steam ID of the account to look up.", required=True) }}

---

{{ param("appid", "uint32", "The app ID of the game to return achievements for.", required=True) }}

---

{{ param("l", "string", "Language for the achievement names and descriptions. When omitted, the name of the achievement and its description will not be retrieved.") }}

</div>

<div markdown>

### Example Request

#### Minimal

```
https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?key=YOUR_API_KEY&format=json&steamids=76561199101839601&appid=1086940
```

#### Full

```
https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?key=YOUR_API_KEY&format=json&steamids=76561199101839601&appid=1086940&l=french
```

</div>

</div>

<div class="ref-grid" markdown>

<div markdown>

### Response

The response is a single `playerstats` object. The account's game details must be visible to you, or the response contains no achievements. If the account does not own the game, an `error` and `success` response will be returned with no information about the account and the game's achievements.

{{ param("steamID", "string", "The account's 64-bit Steam ID. Returned as a string.") }}

---

{{ param("gameName", "string", "The game's title.") }}

---

{{ param("achievements", "Achievement[]", "One object per achievement, with the fields below.") }}

{{ param_bullet("apiname", "string", "The achievement's API name.") }}
{{ param_bullet("achieved", "uint32", "`1` if the account has unlocked the achievement, `0` if not.") }}
{{ param_bullet("unlocktime", "uint32", "Unix time, in seconds, when the achievement was unlocked. `0` when it has not been unlocked.") }}
{{ param_bullet("name", "string", "The achievement's display name. Present when `l` is set.") }}
{{ param_bullet("description", "string", "The achievement's description. Present when `l` is set.") }}

---

{{ param("error", "string", "If the account is not public or does not own the specified game, returns `Profile is not public`.") }}

---

{{ param("success", "bool", "Whether the request succeeded. Valve does not document this field. VDF returns it as the string `1`.") }}

</div>

<div markdown>

### Example Response

Shortened to two of the game's achievements. Captured with `l=french`.

=== "JSON"
    ```json
    {
        "playerstats": {
            "steamID": "76561199101839601",
            "gameName": "Baldur's Gate 3",
            "achievements": [
                {
                    "apiname": "BG3_Quest01",
                    "achieved": 1,
                    "unlocktime": 1731884559,
                    "name": "Fuite de l'Avernus",
                    "description": "Prendre le contrôle du nautiloïde et vous enfuir des Enfers."
                },
                ...
                {
                    "apiname": "BG3_Quest07",
                    "achieved": 0,
                    "unlocktime": 0,
                    "name": "Les péchés du père",
                    "description": ""
                },
                ...
            ],
            "success": true
        }
    }
    ```
=== "XML"
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE playerstats>
    <playerstats>
        <steamID>76561199101839601</steamID>
        <gameName>Baldur&apos;s Gate 3</gameName>
        <achievements>
            <achievement>
                <apiname>BG3_Quest01</apiname>
                <achieved>1</achieved>
                <unlocktime>1731884559</unlocktime>
                <name>Fuite de l&apos;Avernus</name>
                <description>Prendre le contrôle du nautiloïde et vous enfuir des Enfers.</description>
            </achievement>
            ...
            <achievement>
                <apiname>BG3_Quest07</apiname>
                <achieved>0</achieved>
                <unlocktime>0</unlocktime>
                <name>Les péchés du père</name>
                <description></description>
            </achievement>
            ...
        </achievements>
        <success>true</success>
    </playerstats>
    ```
=== "VDF"
    ```
    "playerstats"
    {
        "steamID"	"76561199101839601"
        "gameName"	"Baldur's Gate 3"
        "achievements"
        {
            "0"
            {
                "apiname"	"BG3_Quest01"
                "achieved"	"1"
                "unlocktime"	"1731884559"
                "name"	"Fuite de l'Avernus"
                "description"	"Prendre le contrôle du nautiloïde et vous enfuir des Enfers."
            }
            ...
            "6"
            {
                "apiname"	"BG3_Quest07"
                "achieved"	"0"
                "unlocktime"	"0"
                "name"	"Les péchés du père"
                "description"	""
            }
            ...
        }
        "success"	"1"
    }
    ```
!!! note "Format differences"
    XML wraps each achievement in an `achievement` element, and VDF uses numbered keys with string values.

</div>

</div>