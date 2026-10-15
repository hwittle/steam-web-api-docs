---
title: GetFriendList
description: Returns the friends list of a Steam account, with the date each friendship began.
interface: ISteamUser
method: GetFriendList
version: v0001
http_method: GET
auth: api_key
formats: [json, xml, vdf]
privacy: public_or_owner
last_verified: 15 October 2026
tags:
  - ISteamUser
  - friends
  - privacy-dependent
---

# GetFriendList <span class="p_version">`v0001`</span>

Returns the friends of a Steam account, with the date each friendship began. The account's friends list must be visible to you, unless the API key belongs to the account you are asking about.

{{ glance() }}

## Request

```
GET https://api.steampowered.com/ISteamUser/GetFriendList/v0001/
```

<div class="ref-grid" markdown>

<div markdown>

### Parameters

{{ param("key", "string", "Your Steam Web API key.", required=True) }}

---

{{ param("format", "string", "Response format: `json` (default), `xml`, or `vdf`.") }}

---

{{ param("steamid", "uint64", "The 64-bit Steam ID of the account to look up.", required=True) }}

---

{{ param("relationship", "string", "Which relationships to return. `friend` returns confirmed friends only. `all` returns every relationship, including pending requests.") }}

<!-- VERIFY: confirm the default when relationship is omitted. -->
</div>

<div markdown>

### Example Request

#### Minimal

```
https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=YOUR_API_KEY&format=json&steamid=76561199101839601
```

#### Full

```
https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=YOUR_API_KEY&format=json&steamid=76561199101839601&relationship="friend"
```

</div>

</div>

<div class="ref-grid" markdown>

<div markdown>

### Response

{{ param("friends", "Friend[]", "One object per relationship, with the fields below.") }}

{{ param_bullet("steamid", "string", "The other account's 64-bit Steam ID. JSON and VDF return it as a string, unlike the numeric `steamid` request parameter.") }}
{{ param_bullet("relationship", "string", "How the account is related to the one you asked about. `friend` marks a confirmed friend.") }}
{{ param_bullet("friend_since", "uint32", "Unix time, in seconds, when the friendship began.") }}

<!-- VERIFY: confirm the other relationship values returned with relationship=all. -->

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
    XML wraps each friend in a `friend` element, and VDF uses numbered keys with string values.

</div>

</div>