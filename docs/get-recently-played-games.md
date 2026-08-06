# GetRecentlyPlayedGames v0001

If the user's Steam Community profile visibility is set to `Public`, returns a list of games the user played in the last two weeks. `Private`, `friends-only`, and other privacy settings are not supported unless you are asking for your own personal details, i.e., the Web API key you are using is linked to the Steam ID you are requesting.

=== "Endpoint"
    ```
    https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/
    ```

### Arguments

---

<div class="grid" markdown>

<div markdown>

{{ param("key", "string", "Your designated Steam Web API key.") }}

{{ param("steamid", "integer", "User's 64-bit Steam ID") }}

{{ param("count", "integer", "Optionally limit to a certain number of games (the number of games a person has played in the last 2 weeks is typically very small).") }}

{{ param("format", "string", "Output format: json (default), xml, vdf.") }}

</div>

<div markdown>

=== "Example Request"
    ```
    https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=YOUR_API_KEY&steamid=76561199101839601&count=3&format=json
    ```
</div>

</div>

---

### Returns

The user's achievement list as an array. Nothing will be returned if the user does not share their achivements or if they do not own the game.

---

<div class="grid" markdown>

<div markdown>

{{ param("game_count", "string", "The total number of games the user owns, including free games if `include_played_free_games` passed.") }}

{{ param("games", "array", "An array of games with the following content:") }}

{{ param_bullet("appid", "integer", "Unique ID for the game.") }}
{{ param_bullet("name", "string", "The name of the game.") }}
{{ param_bullet("playtime_2weeks", "integer", "Total number of minutes played in the last 2 weeks.") }}
{{ param_bullet("playtime_forever", "integer", "Total number of minutes played \"on record,\" since Steam began tracking total playtime in early 2009.") }}
{{ param_bullet("img_icon_url_logo", "string", "Filenames of various images for the game.") }}
    - To construct the URL to the image, use this format: https://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{hash}.jpg. For example, the TF2 logo is returned as "07385eb55b5ba974aebbe74d3c99626bda7920b8", which maps to the URL: [https://media.steampowered.com/steamcommunity/public/images/apps/440/07385eb55b5ba974aebbe74d3c99626bda7920b8.jpg]

</div>

<div markdown>
=== "JSON"
    ```json
    {
        "response": {
            "total_count": 20,
            "games": [
                {
                    "appid": 1086940,
                    "name": "Baldur's Gate 3",
                    "playtime_2weeks": 1085,
                    "playtime_forever": 40067,
                    "img_icon_url": "d866cae7ea1e471fdbc206287111f1b642373bd9"
                },
                {
                    "appid": 2767030,
                    "name": "Marvel Rivals",
                    "playtime_2weeks": 583,
                    "playtime_forever": 7621,
                    "img_icon_url": "839b4712925b95702ca56e0c4d399adf54f4d617"
                },
                {
                    "appid": 21690,
                    "name": "Resident Evil 5",
                    "playtime_2weeks": 542,
                    "playtime_forever": 1922,
                    "img_icon_url": "26108f5caff3638c9f522dd79ee84a12761f373a"
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
        <total_count>20</total_count>
        <games>
            <message>
                <appid>1086940</appid>
                <name>Baldur&apos;s Gate 3</name>
                <playtime_2weeks>1083</playtime_2weeks>
                <playtime_forever>40067</playtime_forever>
                <img_icon_url>d866cae7ea1e471fdbc206287111f1b642373bd9</img_icon_url>
            </message>
            <message>
                <appid>2767030</appid>
                <name>Marvel Rivals</name>
                <playtime_2weeks>583</playtime_2weeks>
                <playtime_forever>7621</playtime_forever>
                <img_icon_url>839b4712925b95702ca56e0c4d399adf54f4d617</img_icon_url>
            </message>
            <message>
                <appid>21690</appid>
                <name>Resident Evil 5</name>
                <playtime_2weeks>542</playtime_2weeks>
                <playtime_forever>1922</playtime_forever>
                <img_icon_url>26108f5caff3638c9f522dd79ee84a12761f373a</img_icon_url>
            </message>
        </games>
    </response>
    ```
=== "VDF"
    ```
    "response"
    {
        "total_count"	"20"
        "games"
        {
            "0"
            {
                "appid"	"1086940"
                "name"	"Baldur's Gate 3"
                "playtime_2weeks"	"1083"
                "playtime_forever"	"40067"
                "img_icon_url"	"d866cae7ea1e471fdbc206287111f1b642373bd9"
            }
            "1"
            {
                "appid"	"2767030"
                "name"	"Marvel Rivals"
                "playtime_2weeks"	"583"
                "playtime_forever"	"7621"
                "img_icon_url"	"839b4712925b95702ca56e0c4d399adf54f4d617"
            }
            "2"
            {
                "appid"	"21690"
                "name"	"Resident Evil 5"
                "playtime_2weeks"	"542"
                "playtime_forever"	"1922"
                "img_icon_url"	"26108f5caff3638c9f522dd79ee84a12761f373a"
            }
        }
    }
    ```
</div>

</div>