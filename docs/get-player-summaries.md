# GetPlayerSummaries v0002

Retrieves the basic profile information for a list of 64-bit Steam IDs.

```
ISteamUser/GetPlayerSummaries/v0002/?key=<your API key>&<arguments>
```

### Arguments

{{ param("steamids", "array", "Comma-delimited array of 64 bit Steam IDs to return profile information for. Up to 100 Steam IDs can be requested.") }}
```
&steamids=<array of 64-bit Steam IDs separated by commas>
```

{{ param("format", "string", "Output format: json (default), xml, vdf.") }}
```
&format=<json, xml, or vdf>
```

### Returns

Private Data associated with a Steam account are hidden if the user has their profile visibility set to `Friends Only` or `Private`.

---
#### Public Data

{{ param("steamid", "integer", "User's 64-bit Steam ID.") }}

{{ param("personaname", "string", "User's persona (display) name.") }}

{{ param("profileurl", "string", "The full URL of the user's Steam Community profile.") }}

{{ param("avatar", "string", "The full URL of the user's 32x32 avatar. If no avatar has been configured, this will be the default ? avatar.") }}

{{ param("avatarmedium", "string", "The full URL of the user's 64x64 avatar. If no avatar has been configured, this will be the default ? avatar.") }}

{{ param("avatarfull", "string", "The full URL of the user's 184x184 avatar. If no avatar has been configured, this will be the default ? avatar.") }}

{{ param("personastate", "integer", "The user's current status (0 - Offline, 1 - Online, 2 - Busy, 3 - Away, 4 - Snooze, 5 - Looking to Trade, 6 - Looking to Play). If the user's community visibility state is set to private, this will always be `0`.") }}
!!! note
    A bug makes the status `5 - Looking to Trade` and `6 - Looking to Play` as visible, even if the user's profile is set to private.

{{ param("communityvisibilitystate", "integer", "This represents whether the profile is visible or not.") }}
!!! note
    This Web API does not use authentication and only returns two possible values: `1 - Private, Friends Only, etc (Data not visible)` or `3 - Public (Data is visible)`.

    The community visibility state is from the account making the request to the account being viewed given the requesting account's relationship to the viewed account.

{{ param("profilestate", "integer", "Set to \"1\" if the user have a community profile configured.") }}

{{ param("lastlogoff", "integer", "In Unix time, the last time the user was online.") }}

{{ param("commentpermission", "integer", "Indicates if the user allows public comments.") }}

---
#### Private Data

{{ param("realname", "string", "If set, user's \"real name\"") }}

{{ param("primaryclanid", "integer", "If set, user's primary group.") }}

{{ param("timecreated", "integer", "In Unix time, when the user's account was created.") }}

{{ param("gameid", "integer", "If the user is currently in-game, this value will be returned and set to the gameid of that game.") }}

{{ param("gameserverip", "integer", "If the user is playing online in a game that uses Steam matchmaking, this value will return the ip and port of the game server. Otherwise, the value will be set to `0.0.0.0`") }}

{{ param("gameextrainfo", "string", "If the user is currently in-game, this value will be returned and set to the name of the game they are playing (may also be the name of a non-Steam game shortcut).") }}

{{ param("cityid", "string", "Returns the name of the city the user has set.") }}
!!! warning
    This method is now deprecated and replaced with `loccityid`.

{{ param("loccountrycode", "string", "If set, returns the user's country of residence as a 2-character ISO country code.") }}

{{ param("locstatecode", "string", "If set, returns the user's state of residence.") }}

{{ param("loccityid", "string", "If set, returns the user's city of residence.") }}
!!! note
    A future update will provide this data in a more useful way.

    - Use [gem/package](https://github.com/Holek/steam-friends-countries) to make user location data readable for output.
        - An updated readable list can be found at [github.com/quer/steam-friends-countries](https://github.com/quer/steam-friends-countries).
    - Getting locstatecode and loccityid, can now be done from `https://steamcommunity.com/actions/QueryLocations/<loccountrycode\>/<locstatecode\>/`