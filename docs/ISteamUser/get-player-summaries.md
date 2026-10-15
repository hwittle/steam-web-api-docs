---
title: GetPlayerSummaries
description: Returns profile details for one or more Steam accounts, such as display name, avatars, and online status.
interface: ISteamUser
method: GetPlayerSummaries
version: v0002
http_method: GET
auth: api_key
formats: [json, xml, vdf]
privacy: public_or_owner
last_verified: 14 October 2026
tags:
  - ISteamUser
  - account
  - privacy-dependent
---

# GetPlayerSummaries <span class="p_version">`v0002`</span>

Returns profile details for one or more Steam accounts, such as display name, avatars, online status, and the game being played. Which fields come back depends on the account's privacy settings.

{{ glance() }}

## Request

```
GET https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/
```

<div class="ref-grid" markdown>

<div markdown>

### Parameters

{{ param("key", "string", "Your Steam Web API key.", required=True) }}

---

{{ param("format", "string", "Response format: `json` (default), `xml`, or `vdf`.") }}

---

{{ param("steamids", "string", "Comma-separated list of 64-bit Steam IDs to look up. Up to 100 IDs per request.", required=True) }}

<!-- VERIFY: confirm the 100 ID limit and what happens with an unknown ID. -->

</div>

<div markdown>

### Example Request

=== "One account"
    ```
    https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=YOUR_API_KEY&format=json&steamids=76561199101839601
    ```

=== "Several accounts"
    ```
    https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=YOUR_API_KEY&format=json&steamids=76561199101839601,76561198881233167,76561198377784106
    ```

</div>

</div>

<div class="ref-grid" markdown>

<div markdown>

### Response

Which fields come back depends on the account's profile visibility. If the profile is private, or friends only and you are not a friend, you receive only the fields under Always returned. The other fields are left out of the account's object. Your own account, and accounts that share their profile with you, return both groups.

{{ param("players", "Player[]", "One object per account found. Each object contains the fields below.") }}

#### Always returned

{{ param_bullet("steamid", "string", "The account's 64-bit Steam ID.") }}
{{ param_bullet("personaname", "string", "The account's display name.") }}
{{ param_bullet("profileurl", "string", "URL of the account's Steam Community profile.") }}
{{ param_bullet("avatar", "string", "URL of the 32x32 avatar. Accounts without a custom avatar get Steam's default avatar.") }}
{{ param_bullet("avatarmedium", "string", "URL of the 64x64 avatar.") }}
{{ param_bullet("avatarfull", "string", "URL of the 184x184 avatar.") }}
{{ param_bullet("avatarhash", "string", "Hash used to build the avatar URLs.", "Avatar URL pattern: `https://avatars.steamstatic.com/{hash}.jpg`. Add `_medium` or `_full` before `.jpg` for the larger sizes.") }}
{{ param_bullet("personastate", "uint32", "The account's online status: `0` Offline, `1` Online, `2` Busy, `3` Away, `4` Snooze, `5` Looking to trade, `6` Looking to play. Reports `0` for a profile you cannot see, except that `5` and `6` are still returned.") }}
{{ param_bullet("personastateflags", "uint32", "[Describe only what you observed.]") }}
{{ param_bullet("communityvisibilitystate", "uint32", "Whether the profile is visible to you. `3` means visible. `1` means it is not, which covers private and friends-only profiles. The value reflects your key's relationship to the account. No other values were observed.") }}
{{ param_bullet("profilestate", "uint32", "`1` if the account has set up a Steam Community profile.") }}
{{ param_bullet("commentpermission", "uint32", "Whether the account allows public comments on its profile.") }}
{{ param_bullet("lastlogoff", "uint32", "Unix time, in seconds, when the account was last online.") }}

#### Returned when the profile is visible to you

{{ param_bullet("realname", "string", "The account's real name, if its owner has set one.") }}
{{ param_bullet("timecreated", "uint32", "Unix time, in seconds, when the account was created.") }}
{{ param_bullet("primaryclanid", "string", "ID of the account's primary group, if set. Returned as a string.") }}
{{ param_bullet("loccountrycode", "string", "The two-letter ISO country code the account has set.") }}
{{ param_bullet("locstatecode", "string", "The state or region code the account has set.") }}
{{ param_bullet("loccityid", "string", "ID of the city the account has set.") }}
{{ param_bullet("cityid", "string", "Deprecated. Use `loccityid`.") }}
{{ param_bullet("gameid", "string", "App ID of the game the account is playing now. Returned as a string. Also requires the account to be in a game.") }}
{{ param_bullet("gameextrainfo", "string", "Name of the game being played. Can also be the name of a non-Steam game added as a shortcut. Also requires the account to be in a game.") }}
{{ param_bullet("gameserverip", "string", "IP address and port of the game server, for games that use Steam matchmaking. Otherwise `0.0.0.0`.") }}
{{ param_bullet("lobbysteamid", "string", "An ID that appeared while the account was in a game lobby. Valve does not document this field.") }}

<!-- VERIFY: types and presence of gameserverip, locstatecode, loccityid, cityid, lastlogoff, and the values of personastateflags and commentpermission. -->

</div>

<div markdown>

### Example Response

=== "JSON"
    ```json
    {
        "response": {
            "players": [
                {
                    "steamid": "76561199101839601",
                    "communityvisibilitystate": 3,
                    "profilestate": 1,
                    "personaname": "ΛYΛ",
                    "commentpermission": 1,
                    "profileurl": "https://steamcommunity.com/id/amiaZzZ/",
                    "avatar": "https://avatars.steamstatic.com/1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe.jpg",
                    "avatarmedium": "https://avatars.steamstatic.com/1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe_medium.jpg",
                    "avatarfull": "https://avatars.steamstatic.com/1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe_full.jpg",
                    "avatarhash": "1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe",
                    "personastate": 1,
                    "realname": "Abi",
                    "primaryclanid": "103582791474321399",
                    "timecreated": 1603724668,
                    "personastateflags": 0,
                    "gameextrainfo": "Baldur's Gate 3",
                    "gameid": "1086940",
                    "lobbysteamid": "109775243509294359",
                    "loccountrycode": "US"
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
        <players>
            <player>
                <steamid>76561199101839601</steamid>
                <communityvisibilitystate>3</communityvisibilitystate>
                <profilestate>1</profilestate>
                <personaname>ΛYΛ</personaname>
                <commentpermission>1</commentpermission>
                <profileurl>https://steamcommunity.com/id/amiaZzZ/</profileurl>
                <avatar>https://avatars.steamstatic.com/1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe.jpg</avatar>
                <avatarmedium>https://avatars.steamstatic.com/1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe_medium.jpg</avatarmedium>
                <avatarfull>https://avatars.steamstatic.com/1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe_full.jpg</avatarfull>
                <avatarhash>1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe</avatarhash>
                <personastate>1</personastate>
                <realname>Abi</realname>
                <primaryclanid>103582791474321399</primaryclanid>
                <timecreated>1603724668</timecreated>
                <personastateflags>0</personastateflags>
                <loccountrycode>US</loccountrycode>
            </player>
        </players>
    </response>
    ```
=== "VDF"
    ```
    "response"
    {
        "players"
        {
            "0"
            {
                "steamid"	"76561199101839601"
                "communityvisibilitystate"	"3"
                "profilestate"	"1"
                "personaname"	"ΛYΛ"
                "commentpermission"	"1"
                "profileurl"	"https://steamcommunity.com/id/amiaZzZ/"
                "avatar"	"https://avatars.steamstatic.com/1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe.jpg"
                "avatarmedium"	"https://avatars.steamstatic.com/1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe_medium.jpg"
                "avatarfull"	"https://avatars.steamstatic.com/1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe_full.jpg"
                "avatarhash"	"1b0f9f9bae10dd50e6a5a9043f96542bc7b0a4fe"
                "personastate"	"1"
                "realname"	"Abi"
                "primaryclanid"	"103582791474321399"
                "timecreated"	"1603724668"
                "personastateflags"	"0"
                "loccountrycode"	"US"
            }
        }
    }
    ```
</div>

</div>