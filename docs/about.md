# About this documentation

This is an unofficial reference for the Steam Web API. It is not affiliated with or endorsed by Valve.

## Scope

This documentation currently covers 5 endpoints across 3 interfaces. It documents the public host, `api.steampowered.com`. It does not cover `partner.steam-api.com`, which is used with publisher keys. The goal is to cover the full public API. For methods not listed here, see the [Steamworks Web API reference](https://partner.steamgames.com/doc/webapi).

## Sources

- **Steamworks Web API reference:** the official source for interfaces, methods, and parameters.
- **[Valve Developer Community](https://developer.valvesoftware.com/wiki/Steam_Web_API):** a community-edited wiki, used for context only. It is not official.

Paid third-party services are not used as sources. Descriptions on every page are written in this project's own words.

Steam is a trademark of Valve Corporation. This project is not affiliated with or endorsed by Valve.

## Verification

Steam provides no test accounts for developers, so samples come from accounts whose owners made them public. Data that was visible only through a friendship is replaced with placeholders where noted.

Each endpoint was called against the live API using a standard Steam Web API key, and the JSON, XML, and VDF samples on each page are captured from those calls. Where behavior depends on profile privacy, the page states which privacy settings it was tested with.

Field names and types are cross-checked against two community type libraries:

- [@oddlaceguy49/steam-web-api-types](https://www.npmjs.com/package/@oddlaceguy49/steam-web-api-types): typed response definitions, including platform-specific responses.
- [Jleagle/steam-go](https://pkg.go.dev/github.com/Jleagle/steam-go/steamapi): a secondary reference for field types and structures the first library does not cover.

Valve does not publish response schemas for the Web API, so numeric widths such as `uint32` and `uint64` are inferred from observed values and Steam's C++ type definitions.

Where observed behavior differs from the Steamworks reference, the page says so next to the field it affects. Each page shows its own last verified date, because endpoints are checked one at a time.

## License

[Your license choice]