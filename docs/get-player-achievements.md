# GetPlayerAchievements v0001

If the user's achievement is set to visible, returns a list of achievement for this user by the requested game.

```
.../ISteamUserStats/GetPlayerAchievements/v0001/?key=<your API key>&<arguments>
```

### Arguments

{{ param("steamids", "list", "User's 64-bit Steam ID") }}
```
&steamids=<64-bit Steam ID>
```

{{ param("appid", "integer", "The ID for the game you are requesting.") }}
```
&appid=<ID number of the requested game>
```

{{ param("l (optional; letter L)", "string", "If specified and available, return the achievement data in the requested language.") }}
```
&l=<english/french/german/etc.>
```

### Returns

The user's achievement list as an array. Nothing will be returned if the user does not share their achivements or if they do not own the game.

{{ param("apiname", "string", "The API name of the achievement.") }}

{{ param("achieved", "integer", "Set as 1 if completed.") }}

{{ param("unlocktime", "integer", "In Unix time, when the achievement was completed.") }}

{{ param("name (optional)", "string", "Localized achievement name.") }}

{{ param("description (optional)", "string", "Localized achievement description.") }}