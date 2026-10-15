---
title: Unofficial Steam Web API documentation
description: An unofficial reference for the Steam Web API, with parameters, example requests, and captured responses in JSON, XML, and VDF.
---

# Unofficial Steam Web API documentation

The Steam Web API is a set of HTTP endpoints from Valve for reading Steam account, game, and community data. This site documents its endpoints with parameter descriptions, example requests, and captured responses in JSON, XML, and VDF.

This is an unofficial resource and is not affiliated with Valve. See [About this documentation](about.md) for its sources and how pages are verified.

## Get an API key

1. [Create a Steam account](https://store.steampowered.com/join) if you do not have one.
2. Sign in and register for a key at [steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey).
3. Copy the key and store it somewhere private.

The key identifies your application to Steam. Some methods return data only for certain kinds of keys, such as publisher keys. Each endpoint page states what it requires.

<!-- VERIFY: confirm the key form's current requirements before describing them. -->

!!! warning
    Treat your API key like a password. Do not put it in source code, in code that runs in a browser, or in a URL you share. Store it in your server's secret manager or in an environment variable. If a key is exposed, revoke it on the page where you registered it and request a new one.

## Make your first request

Every request follows this pattern:

```
https://api.steampowered.com/INTERFACE/METHOD/VERSION/?key=YOUR_API_KEY&format=FORMAT
```

Replace the uppercase placeholders:

- `INTERFACE`: the group the method belongs to, such as `ISteamUser`.
- `METHOD`: the method name, such as `GetPlayerSummaries`.
- `VERSION`: the version as the endpoint page shows it, such as `v0001`.
- `YOUR_API_KEY`: your key.
- `FORMAT`: `json`, `xml`, or `vdf`. The default is `json`.

To list the interfaces and methods Steam exposes, call `ISteamWebAPIUtil/GetSupportedAPIList`. Without a key it lists only methods that do not require one. With a key it lists every method that key can access.

=== "Without a key"
```
    https://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/
```

=== "With a key"
```
    https://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key=YOUR_API_KEY
```

All examples on this site use the public host, `api.steampowered.com`. Valve also runs `partner.steam-api.com` for publishers. It uses a publisher key and has stricter rate limits, and this site does not cover it.

<!-- VERIFY: confirm the partner host description against Valve's reference. -->

## Pass parameters

How you send a method's parameters depends on its interface.

Most interfaces take parameters as ordinary query parameters:

```
https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=YOUR_API_KEY&steamid=76561199101839601
```

<!-- VERIFY: confirm the GetFriendList version and parameters when that page is converted. -->

Service interfaces, whose names end in `Service`, such as `IPlayerService`, take their parameters in one `input_json` query parameter. The `key` and `format` parameters stay at the top level. This is also how you send array parameters such as `appids_filter`.

=== "Readable"
```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json={"steamid": 76561199101839601}
```

=== "URL-encoded"
```
    https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=YOUR_API_KEY&format=json&input_json=%7B%22steamid%22%3A%2076561199101839601%7D
```

Percent-encode the JSON before you send it. Browsers and most HTTP libraries do this for you. If you build the URL by hand, encode it yourself.

## Response formats

Every method can return JSON, XML, or VDF. JSON is the default. Set `format` to change it. The samples below are an excerpt of the `GetSupportedAPIList` response.

[keep your three tabs here]

Each endpoint page lists any differences in how a format represents its fields.

## Profile privacy

A Steam Community profile can be public, friends only, or private. Many methods return less data, or none, when the account you ask about is not public. What you get depends on that account's privacy settings and on your relationship to it. Each endpoint page shows a Privacy value in its at-a-glance strip and describes what was observed.

<!-- VERIFY: the old text said a key's own Steam ID bypasses privacy restrictions. Confirm per endpoint before restoring it. -->

## Next steps

- Choose a method from the endpoint reference in the sidebar.
- See [GetOwnedGames](IPlayerService/get-owned-games.md) for a complete example page.
- If a request fails or returns nothing, see [Errors](errors.md).