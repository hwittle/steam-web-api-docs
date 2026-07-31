# GetFriendList v0001

If the user's Steam Community profile visibility is set to `Public`, retrieves the Steam user's friend list.

```
ISteamUser/GetFriendList/v0001/?key=<your API key>&<arguments>
```

### Arguments

{{ param("steamids", "list", "User's 64-bit Steam ID") }}
```
&steamids=<64-bit Steam ID>
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

The user's friend list as an array of Steam users. Nothing will be returned if the user's Steam Community profile visibility is set to `Private`.

{{ param("steamid", "integer", "64-bit Steam ID of the user's friend.") }}

{{ param("relationship", "string", "Relationship qualifier returned as `friend`.") }}

{{ param("friend_since", "integer", "In Unix time, when the relationship was created.") }}