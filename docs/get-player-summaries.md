# GetPlayerSummaries <span class="p_version">`v0002`</span>

Retrieves the basic profile information for a list of 64-bit Steam IDs.

=== "Endpoint"
    ```
    https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/
    ```

## Arguments

---
<div class="grid" markdown>

<div markdown>

{{ param("key", "string", "Your designated Steam Web API key.") }}

---
{{ param("steamids", "array of integers", "Comma-delimited array of 64 bit Steam IDs to return profile information for. Up to 100 Steam IDs can be requested.") }}

---
{{ param("format", "string", "Output format: json (default), xml, vdf.") }}

</div>

<div markdown>

=== "Example Request - Single User"
    ```
    https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=YOUR_API_KEY&steamids=76561199101839601&format=json
    ```
=== "Example Request - Multiple Users"
    ```
    https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=YOUR_API_KEY&steamids=76561199101839601, 76561198881233167, 76561198377784106&format=json
    ```

</div>

</div>

---

## Returns

Private Data associated with a Steam account are hidden if the user has their profile visibility set to `Friends Only` or `Private`.

---

<div class="grid" markdown>

<div markdown>

#### Public Data

{{ param("steamid", "string", "User's 64-bit Steam ID.") }}

---
{{ param("personaname", "string", "User's persona (display) name.") }}

---
{{ param("profileurl", "string", "The full URL of the user's Steam Community profile.") }}

---
{{ param("avatar", "string", "The full URL of the user's 32x32 avatar. If no avatar has been configured, this will be the default ? avatar.") }}

---
{{ param("avatarmedium", "string", "The full URL of the user's 64x64 avatar. If no avatar has been configured, this will be the default ? avatar.") }}

---
{{ param("avatarfull", "string", "The full URL of the user's 184x184 avatar. If no avatar has been configured, this will be the default ? avatar.") }}

---
{{ param("personastate", "integer", "The user's current status (0 - Offline, 1 - Online, 2 - Busy, 3 - Away, 4 - Snooze, 5 - Looking to Trade, 6 - Looking to Play). If the user's community visibility state is set to private, this will always be `0`.") }}
???+ note
    A bug makes the status `5 - Looking to Trade` and `6 - Looking to Play` as visible, even if the user's profile is set to private.

---
{{ param("communityvisibilitystate", "integer", "This represents whether the profile is visible or not.") }}
???+ note
    This Web API does not use authentication and only returns two possible values: `1 - Private, Friends Only, etc (Data not visible)` or `3 - Public (Data is visible)`.

    The community visibility state is from the account making the request to the account being viewed given the requesting account's relationship to the viewed account.

---
{{ param("profilestate", "integer", "Set to \"1\" if the user have a community profile configured.") }}

---
{{ param("lastlogoff", "integer", "In Unix time, the last time the user was online.") }}

---
{{ param("commentpermission", "integer", "Indicates if the user allows public comments.") }}

---
#### Private Data

{{ param("realname", "string", "If set, user's \"real name\"") }}

---
{{ param("primaryclanid", "integer", "If set, user's primary group.") }}

---
{{ param("timecreated", "integer", "In Unix time, when the user's account was created.") }}

---
{{ param("gameid", "integer", "If the user is currently in-game, this value will be returned and set to the gameid of that game.") }}

---
{{ param("gameserverip", "string", "If the user is playing online in a game that uses Steam matchmaking, this value will return the ip and port of the game server. Otherwise, the value will be set to `0.0.0.0`") }}

---
{{ param("gameextrainfo", "string", "If the user is currently in-game, this value will be returned and set to the name of the game they are playing (may also be the name of a non-Steam game shortcut).") }}

---
{{ param("locstatecode", "string", "If set, returns the user's state of residence.") }}

---
{{ param("cityid", "string", "Returns the name of the city the user has set.") }}
???+ warning
    This method is now deprecated and replaced with `loccityid`.

---
{{ param("loccountrycode", "string", "If set, returns the user's country of residence as a 2-character ISO country code.") }}

---
{{ param("lobbysteamid", "string", "Undocumented in the official Steam Web API documentation. Based on observed responses, this field appears when a user is in an active game lobby and likely represents the Steam lobby instance ID for games that support Steam matchmaking servers.") }}

---
{{ param("loccityid", "string", "If set, returns the user's city of residence.") }}
???+ note
    A future update will provide this data in a more useful way.

    - Use [gem/package](https://github.com/Holek/steam-friends-countries) to make user location data readable for output.
        - An updated readable list can be found at [github.com/quer/steam-friends-countries](https://github.com/quer/steam-friends-countries).
    - Getting locstatecode and loccityid, can now be done from `https://steamcommunity.com/actions/QueryLocations/<loccountrycode\>/<locstatecode\>/`

</div>

<div markdown>
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