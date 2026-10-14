---
title: GetPlayerAchievements
description: Returns the achievements of a game the Steam account owns only if profile visibility is set to public.
interface: ISteamUserStats
method: GetPlayerAchievements
version: v0001
http_method: GET
auth: api_key
formats: [json, xml, vdf]
privacy: public_or_owner
last_verified: 14 October 2026
tags:
  - ISteamUserStats
  - achievements
  - privacy-dependent
---

# GetPlayerAchievements <span class="p_version">`v0001`</span>

If the user's game details are publicly visible, returns a list of achievement for this user by the requested game.

{{ glance() }}

## Request

```
GET https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/
```

<div class="ref-grid" markdown>

<div markdown>

### Parameters

{{ param("key", "string", "Your designated Steam Web API key.", required=True) }}

---
{{ param("steamids", "integer", "User's 64-bit Steam ID") }}

---
{{ param("appid", "integer", "Unique ID for the game you are requesting.") }}

---
{{ param("format", "string", "Output format: json (default), xml, vdf.") }}

---
{{ param("l (optional)", "string", "If specified and available, return the achievement data in the requested language.") }}

</div>

<div markdown>

### Example Request

#### Minimal

=== "Example Request"
    ```
    https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?key=YOUR_API_KEY&steamids=76561199101839601&appid=1086940&format=json&l=french
    ```

#### Full

</div>

</div>

<div class="ref-grid" markdown>

<div markdown>

### Response

A list of achievements the user has obtained for the requested game. Nothing is returned if the profile is not publicly visible or the user does not own the game.

{{ param("steamid", "string", "User's 64-bit Steam ID.") }}

---

{{ param("gameName", "string", "The name of the game.") }}

---
{{ param("achievements", "array", "An array of achievemets with the following content:") }}

{{ param_bullet("apiname", "string", "The API name of the achievement.") }}
{{ param_bullet("achieved", "integer", "Set as 1 if completed.") }}
{{ param_bullet("unlocktime", "integer", "In Unix time, when the achievement was completed.") }}
{{ param_bullet("name (optional)", "string", "Localized achievement name.") }}
{{ param_bullet("description (optional)", "string", "Localized achievement description.") }}

{{ param("success", "boolean", "Undocumented in the official Steam Web API documentation. Returns true if the request was successful. In VDF format, returned as \"1\" instead of true.") }}

</div>

<div markdown>

### Example Response

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
    XML wraps each game in a `message` element, and VDF uses numbered keys with string values.

</div>

</div>