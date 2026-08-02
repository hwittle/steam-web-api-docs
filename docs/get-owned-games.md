# GetOwnedGames v0001

If the user's Steam Community profile visibility is set to `Public`, returns a list of games the user owns along with playtime information. `Private`, `friends-only`, and other privacy settings are not supported unless you are asking for your own personal details, i.e., the Web API key you are using is linked to the Steam ID you are requesting.

```
.../IPlayerService/GetOwnedGames/v0001/?key=<your API key>&<arguments>
```

### Arguments

{{ param("steamids", "list", "User's 64-bit Steam ID") }}
```
&steamids=<64-bit Steam ID>
```

{{ param("include_appinfo", "integer", "Include game name and logo information in the output. The default is to return appids only.") }}
```
&include_appinfo=<`0 - to not include` or `1 - to include`>
```

{{ param("include_played_free_games", "", "By default, free games like Team Fortress 2 are excluded (as technically everyone owns them). If include_played_free_games is set, they will be returned if the player has played them at some point. This is the same behavior as the games list on the Steam Community.") }}
```
&include_played_free_games=<`0 - to not include` or `1 - to include`>
```

{{ param("format", "string", "Output format: json (default), xml, vdf.") }}
```
&format=<json, xml, or vdf>
```

{{ param("appids_filter", "array of integers", "You can optionally filter the list to a set of appids.") }}
!!! note
    Note that these cannot be passed as a URL parameter, instead you must use the JSON format described in Steam_Web_API#Calling_Service_interfaces.
```
&input_json=<URL-encoded parameters>
```

### Returns

The user's achievement list as an array. Nothing will be returned if the user does not share their achivements or if they do not own the game.

{{ param("game_count", "string", "The total number of games the user owns \(including free games if `include_played_free_games` passed\).") }}

{{ param("games", "array", "An array of games with the following content:") }}

{{ param_bullet("appid", "integer", "Unique ID for the game.") }}
{{ param_bullet("name", "string", "The name of the game.") }}
{{ param_bullet("playtime_2weeks", "integer", "Total number of minutes played in the last 2 weeks.") }}
{{ param_bullet("playtime_forever", "integer", "Total number of minutes played \"on record,\" since Steam began tracking total playtime in early 2009.") }}
{{ param_bullet("img_icon_url_logo", "string", "Filenames of various images for the game.") }}
    - To construct the URL to the image, use this format: https://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{hash}.jpg. For example, the TF2 logo is returned as "07385eb55b5ba974aebbe74d3c99626bda7920b8", which maps to the URL: [https://media.steampowered.com/steamcommunity/public/images/apps/440/07385eb55b5ba974aebbe74d3c99626bda7920b8.jpg]
{{ param_bullet("has_community_visible_stats", "integer", "Indicates there is a stats page with achievements or other game stats available for this game.") }}
    - The uniform URL for accessing this data is https://steamcommunity.com/profiles/{steamid}/stats/{appid}. For example, Robin's TF2 stats can be found at: https://steamcommunity.com/profiles/76561197960435530/stats/440. You may notice that clicking this link will actually redirect to a vanity URL like /id/robinwalker/stats/TF2