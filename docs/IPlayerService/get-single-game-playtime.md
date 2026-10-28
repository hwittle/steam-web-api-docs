---
title: GetSingleGamePlaytime
description: Returns a Steam user's playtime for a specified game, however only developers and publishers with a WebAPI key related to the game can retreive results.
interface: IPlayerService
method: GetSingleGamePlaytime
version: v0001
http_method: GET
auth: api_key
formats: [json, xml, vdf]
privacy: developer_or_publisher
last_verified: 27 October 2026
tags:
  - IPlayerService
  - games
  - developer-dependent
  - publisher-dependent
---

# GetSingleGamePlaytime <span class="p_version">`v0001`</span>

Returns information about a Steam user's playtime for a specified game, however only developers and publishers with a WebAPI key related to the game can retreive results.

{{ glance() }}

## Request

```
GET https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/
```
{{ service_note() }}

<div class="ref-grid" markdown>

<div markdown>

### Parameters

{{ param("key", "string", "Your Steam Web API key.", required=True) }}

---

{{ param("format", "string", "Response format: `json` (default), `xml`, or `vdf`.") }}

---

{{ param("steamid", "uint64", "The 64-bit Steam ID of the account to look up.", required=True) }}

---

{{ param("appid", "uint32", "The app ID of the game to return achievements for.", required=True) }}

</div>

<div markdown>

### Example Request

!!! warning "Authorization"
    Only WebAPI keys associated with the `appid` can access and retrieve information. Otherwise, a forbidden request is returned.

</div>

</div>

<div class="ref-grid" markdown>

<div markdown>

### Response

Information of the Steam user's playtime is returned for the specified game.

!!! note "Unverified"
    Until this can be verified, this section will be a work in progress.

</div>

<div markdown>

### Example Response

!!! note "Unverified"
    Until this can be verified, this section will be a work in progress.

</div>

</div>