# GetRecentlyPlayedGames v0001

If the user's Steam Community profile visibility is set to `Public`, returns a list of games the user played in the last two weeks. `Private`, `friends-only`, and other privacy settings are not supported unless you are asking for your own personal details, i.e., the Web API key you are using is linked to the Steam ID you are requesting.

```
.../IPlayerService/GetRecentlyPlayedGames/v0001/?key=<your API key>&<arguments>
```

### Arguments

{{ param("steamids", "integer", "User's 64-bit Steam ID") }}
```
&steamids=<64-bit Steam ID>
```

{{ param("count", "integer", "Optionally limit to a certain number of games (the number of games a person has played in the last 2 weeks is typically very small).") }}
```
&count=<Limit number for how many games are shown>
```

{{ param("format", "string", "Output format: json (default), xml, vdf.") }}
```
&format=<json, xml, or vdf>
```

### Returns

The user's achievement list as an array. Nothing will be returned if the user does not share their achivements or if they do not own the game.

{{ param("game_count", "string", "The total number of games the user owns (including free games if `include_played_free_games` passed.")) }}

{{ param("games", "array", "An array of games with the following content:") }}

{{ param_bullet("appid", "integer", "Unique ID for the game.") }}
{{ param_bullet("name", "string", "The name of the game.") }}
{{ param_bullet("playtime_2weeks", "integer", "Total number of minutes played in the last 2 weeks.") }}
{{ param_bullet("playtime_forever", "integer", "Total number of minutes played \"on record,\" since Steam began tracking total playtime in early 2009.") }}
{{ param_bullet("img_icon_url_logo", "string", "Filenames of various images for the game.") }}
    - To construct the URL to the image, use this format: https://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{hash}.jpg. For example, the TF2 logo is returned as "07385eb55b5ba974aebbe74d3c99626bda7920b8", which maps to the URL: [https://media.steampowered.com/steamcommunity/public/images/apps/440/07385eb55b5ba974aebbe74d3c99626bda7920b8.jpg]