# GetPlayerAchievements <span class="p_version">`v0001`</span>

If the user's achievement is set to visible, returns a list of achievement for this user by the requested game.

=== "Endpoint"
    ```
    https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/
    ```

### Arguments

---
<div class="grid" markdown>

<div markdown>

{{ param("key", "string", "Your designated Steam Web API key.") }}

---
{{ param("steamids", "list", "User's 64-bit Steam ID") }}

---
{{ param("appid", "integer", "Unique ID for the game you are requesting.") }}

---
{{ param("l (optional; letter L)", "string", "If specified and available, return the achievement data in the requested language.") }}

</div>

<div markdown>

=== "Example Request"
    ```
    https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?key=YOUR_API_KEY&steamids=76561199101839601&appid=1086940&format=json&l=french
    ```

</div>

</div>

---

### Returns

A list of achievements a user has obtained, if the profile is publically visible and owns the game.
The user's achievement list as an array. Private, friends-only, and other privacy settings are not supported unless you are asking for your own personal details, e.g., the WebAPI key you are using is linked to the steamid you are requesting.
---

<div class="grid" markdown>

<div markdown>

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

</div>

<div markdown>

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
</div>

</div>