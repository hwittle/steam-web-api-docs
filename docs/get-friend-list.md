# GetFriendList <span class="p_version">`v0001`</span>

If the user's Steam Community profile visibility is set to `Public`, retrieves the Steam user's friend list.

=== "Endpoint"
    ```
    https://api.steampowered.com/ISteamUser/GetFriendList/v0001/
    ```

### Arguments

---
<div class="grid" markdown>

<div markdown>

{{ param("key", "string", "Your designated Steam Web API key.") }}

---
{{ param("steamid", "integer", "User's 64-bit Steam ID") }}

---
{{ param("relationship", "string", "The value `friend` returns only confirmed friend and `all` returns all relationships including pending friend requests.") }}

---
{{ param("format", "string", "Values: json (default), xml, vdf.") }}

</div>

<div markdown>

=== "Example Request"
    ```
    https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=YOUR_API_KEY&steamid=76561199101839601&format=json
    ```

</div>

</div>

### Returns

The user's friend list as an array of Steam users. Nothing will be returned if the user's Steam Community profile visibility is set to `Private`.

---
<div class="grid" markdown>

<div markdown>

{{ param("steamid", "string", "64-bit Steam ID of the user's friend.") }}

---
{{ param("relationship", "string", "Relationship qualifier returned as `friend`.") }}

---
{{ param("friend_since", "integer", "In Unix time, when the relationship was created.") }}

</div>

<div markdown>

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
</div>

</div>