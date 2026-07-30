# GetFriendList v0001

If the user's Steam Community profile visibility is set to `Public`, retrieves the Steam user's friend list.

```
ISteamUser/GetFriendList/v0001/?key=<your API key>&<arguments>
```

### Arguments

{{ param("steamids", "list", "Comma-delimited list of 64 bit Steam IDs to return profile information for. Up to 100 Steam IDs can be requested.") }}
```
&steamids=<list of 64-bit Steam IDs separated by commas>
```

{{ param("format", "string", "Values: all, friend.") }}
```
&relationship=<all or friend>
```

{{ param("format", "string", "Values: json (default), xml, vdf.") }}
```
&format=<json, xml, or vdf>
```

### Returns

Private Data associated with a Steam account are hidden if the user has their profile visibility set to `Friends Only` or `Private`.

{{ param("steamid", "integer", "64-bit Steam ID of the user's friend.") }}

{{ param("personaname", "string", "User's persona (display) name.") }}

{{ param("profileurl", "string", "The full URL of the user's Steam Community profile.") }}