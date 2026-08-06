# GetOwnedGames <span class="p_version">`v0001`</span>

If the user's Steam Community profile visibility is set to `Public`, returns a list of games the user owns along with playtime information. `Private`, `friends-only`, and other privacy settings are not supported unless you are asking for your own personal details, i.e., the Web API key you are using is linked to the Steam ID you are requesting.

=== "Endpoint"
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/
    ```

### Arguments

---

<div class="grid" markdown>

<div markdown>

{{ param("key", "string", "Your designated Steam Web API key.") }}
---

{{ param("steamid", "integer", "User's 64-bit Steam ID.") }}

{{ param("include_appinfo", "boolean", "Include game name and logo information in the output. The default is to return appids only.") }}

{{ param("include_played_free_games", "boolean", "By default, free games like Team Fortress 2 are excluded (as technically everyone owns them). If `include_played_free_games` is set, they will be returned if the player has played them at some point. This is the same behavior as the games list on the Steam Community.") }}

{{ param("format", "string", "Output format: json (default), xml, vdf.") }}

{{ param("appids_filter", "array of integers", "You can optionally filter the list to a set of appids.") }}
???+ note
    This cannot be passed as a query parameter directly. You have to use the query parameter `input_json`, passing `steamid` and `appids_filter` nested inside as a URL-encoded parameter.

</div>

<div markdown>

=== "Example Request"
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&steamid=76561199101839601&include_appinfo=true&include_played_free_games=true&format=json
    ```
    
---

=== "With "appids_filter" - Pretty Ver."
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json={"steamid":76561199101839601,"include_appinfo":true,"appids_filter":[4000, 21690, 22330]}
    ```
=== "With "appids_filter" - Encoded Ver."
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json=%7B%22steamid%22%3A76561199101839601%2C%22include_appinfo%22%3Atrue%2C%22appids_filter%22%3A%5B4000%2C%2021690%2C%2022330%5D%7D
    ```

</div>

</div>

---

### Returns

The user's achievement list as an array. Nothing will be returned if the user does not share their achivements or if they do not own the game.

---

<div class="grid" markdown>

<div markdown>

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

</div>

<div markdown>
=== "JSON"
    ```json
    {
        "response": {
            "game_count": 3,
            "games": [
                {
                    "appid": 4000,
                    "name": "Garry's Mod",
                    "playtime_forever": 102,
                    "img_icon_url": "4a6f25cfa2426445d0d9d6e233408de4d371ce8b",
                    "has_community_visible_stats": true
                },
                {
                    "appid": 21690,
                    "name": "Resident Evil 5",
                    "playtime_2weeks": 542,
                    "playtime_forever": 1922,
                    "img_icon_url": "26108f5caff3638c9f522dd79ee84a12761f373a",
                    "has_community_visible_stats": true,
                    "has_leaderboards": true
                },
                {
                    "appid": 22330,
                    "name": "The Elder Scrolls IV: Oblivion Game of the Year Edition (2009)",
                    "playtime_forever": 51,
                    "img_icon_url": "e33402f6e1e4ed6dd001c7add26934f345cbd31e",
                    "content_descriptorids": [
                        2,
                        5
                    ]
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
        <game_count>3</game_count>
        <games>
            <message>
                <appid>4000</appid>
                <name>Garry&apos;s Mod</name>
                <playtime_forever>102</playtime_forever>
                <img_icon_url>4a6f25cfa2426445d0d9d6e233408de4d371ce8b</img_icon_url>
                <has_community_visible_stats>true</has_community_visible_stats>
            </message>
            <message>
                <appid>21690</appid>
                <name>Resident Evil 5</name>
                <playtime_2weeks>542</playtime_2weeks>
                <playtime_forever>1922</playtime_forever>
                <img_icon_url>26108f5caff3638c9f522dd79ee84a12761f373a</img_icon_url>
                <has_community_visible_stats>true</has_community_visible_stats>
                <has_leaderboards>true</has_leaderboards>
            </message>
            <message>
                <appid>22330</appid>
                <name>The Elder Scrolls IV: Oblivion Game of the Year Edition (2009)</name>
                <playtime_forever>51</playtime_forever>
                <img_icon_url>e33402f6e1e4ed6dd001c7add26934f345cbd31e</img_icon_url>
                <content_descriptorids>
                    <uint32>2</uint32>
                    <uint32>5</uint32>
                </content_descriptorids>
            </message>
        </games>
    </response>
    ```
=== "VDF"
    ```
    "response"
    {
        "game_count"	"3"
        "games"
        {
            "0"
            {
                "appid"	"4000"
                "name"	"Garry's Mod"
                "playtime_forever"	"102"
                "img_icon_url"	"4a6f25cfa2426445d0d9d6e233408de4d371ce8b"
                "has_community_visible_stats"	"1"
            }
            "1"
            {
                "appid"	"21690"
                "name"	"Resident Evil 5"
                "playtime_2weeks"	"542"
                "playtime_forever"	"1922"
                "img_icon_url"	"26108f5caff3638c9f522dd79ee84a12761f373a"
                "has_community_visible_stats"	"1"
                "has_leaderboards"	"1"
            }
            "2"
            {
                "appid"	"22330"
                "name"	"The Elder Scrolls IV: Oblivion Game of the Year Edition (2009)"
                "playtime_forever"	"51"
                "img_icon_url"	"e33402f6e1e4ed6dd001c7add26934f345cbd31e"
                "content_descriptorids"
                {
                    "0"	"2"
                    "1"	"5"
                }
            }
        }
    }
    ```
</div>

</div>