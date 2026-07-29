# GetPlayerSummaries v0002

Retrieves the basic profile information for a list of 64-bit Steam IDs.

```
ISteamUser/GetPlayerSummaries/v0002/?key=<your API key>&<arguments>
```

### Arguments

{{ param("steamids", "list", "Comma-delimited list of 64 bit Steam IDs to return profile information for. Up to 100 Steam IDs can be requested.") }}
```
&steamids=<list of 64-bit Steam IDs separated by commas>
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

{{ param("personastate", "integer", "The user's current status (0 - Offline, 1 - Online, 2 - Busy, 3 - Away, 4 - Snooze, 5 - Looking to Trade, 6 - Looking to Play). If the user's profile is set to private, this will always be `0`.") }}
!!! note
    A bug makes the status `5 - Looking to Trade` and `6 - Looking to Play` as visible, even if the user's profile is set to private.

{{ param("communityvisibilitystate", "", "") }}

{{ param("profilestate", "", "") }}

{{ param("lastlogoff", "", "") }}

{{ param("commentpermission", "", "") }}

---
#### Private Data

{{ param("realname", "string", "If set, user's \"real name\"") }}

{{ param("", "", "") }}

{{ param("", "", "") }}

{{ param("", "", "") }}

{{ param("", "", "") }}

{{ param("", "", "") }}

{{ param("", "", "") }}

{{ param("", "", "") }}

{{ param("", "", "") }}