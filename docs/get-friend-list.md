---
title: GetFriendList
description: Returns the friends a Steam account befriended only if profile visibility is set to public.
interface: ISteamUser
method: GetFriendList
version: v0001
http_method: GET
auth: api_key
formats: [json, xml, vdf]
privacy: public_or_owner
last_verified: 14 October 2026
tags:
  - ISteamUser
  - friends
  - privacy-dependent
---

# GetFriendList <span class="p_version">`v0001`</span>

If the user's Steam Community profile visibility is set to `Public`, retrieves the Steam user's friend list.


{{ glance() }}

## Request

```
GET https://api.steampowered.com/ISteamUser/GetFriendList/v0001/
```

<div class="ref-grid" markdown>

<div markdown>

### Parameters

{{ param("key", "string", "Your designated Steam Web API key.") }}

---
{{ param("format", "string", "Output format: json (default), xml, vdf.") }}

---
{{ param("steamid", "integer", "User's 64-bit Steam ID") }}

---
{{ param("relationship", "string", "The value `friend` returns only confirmed friend and `all` returns all relationships including pending friend requests.") }}

</div>

<div markdown>

### Example Request

#### Minimal

=== "Readable"
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json={"steamid": 76561199101839601}
    ```

=== "URL-encoded (ready to use)"
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json=%7B%22steamid%22%3A%2076561199101839601%2C%20%22include_appinfo%22%3Atrue%2C%20%22include_played_free_games%22%3A%20true%2C%20%22appids_filter%22%3A%5B4000%2C%2021690%2C%2022330%5D%7D
    ```

#### Full

=== "Readable"
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json={"steamid": 76561199101839601, "include_appinfo":true, "include_played_free_games": true, "appids_filter":[4000, 21690, 22330]}
    ```

=== "URL-encoded (ready to use)"
    ```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json=%7B%22steamid%22%3A%2076561199101839601%2C%20%22include_appinfo%22%3Atrue%2C%20%22include_played_free_games%22%3A%20true%2C%20%22appids_filter%22%3A%5B4000%2C%2021690%2C%2022330%5D%7D
    ```
    ```

</div>

</div>

<div class="ref-grid" markdown>

<div markdown>

### Response

{{ param("steamid", "string", "64-bit Steam ID of the user's friend.") }}

---
{{ param("relationship", "string", "Relationship qualifier returned as `friend`.") }}

---
{{ param("friend_since", "integer", "In Unix time, when the relationship was created.") }}

</div>

<div markdown>

### Example Response

=== "JSON"
    ```json
    {
        "friendslist": {
            "friends": [
                {
                    "steamid": "76561198051251936",
                    "relationship": "friend",
                    "friend_since": 1771557944
                },
                {
                    "steamid": "76561198056342935",
                    "relationship": "friend",
                    "friend_since": 1630520677
                }
            ]
        }
    }
    ```
=== "XML"
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE friendslist>
    <friendslist>
        <friends>
            <friend>
                <steamid>76561198051251936</steamid>
                <relationship>friend</relationship>
                <friend_since>1771557944</friend_since>
            </friend>
            <friend>
                <steamid>76561198056342935</steamid>
                <relationship>friend</relationship>
                <friend_since>1630520677</friend_since>
            </friend>
        </friends>
    </friendslist>
    ```
=== "VDF"
    ```
    "friendslist"
    {
        "friends"
        {
            "0"
            {
                "steamid"	"76561198051251936"
                "relationship"	"friend"
                "friend_since"	"1771557944"
            }
            "1"
            {
                "steamid"	"76561198056342935"
                "relationship"	"friend"
                "friend_since"	"1630520677"
            }
        }
    }
    ```

!!! note "Format differences"
    XML wraps each game in a `message` element, and VDF uses numbered keys with string values.

</div>

</div>