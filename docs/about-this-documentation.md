# About This Documentation

## Scope

This documentation covers [N] endpoints across [N] interfaces. Endpoints
were selected based on [usage frequency / community demand / personal need].
Endpoints not listed here are not covered — see the
[Steamworks Web API Reference](https://partner.steamgames.com/doc/webapi)
for the full list.

## Verification

Response samples were obtained by making live API calls. Each endpoint was
tested and the raw JSON response was recorded.

Response field structure and types are cross-referenced against:

- [@oddlaceguy49/steam-web-api-types](https://www.npmjs.com/package/@oddlaceguy49/steam-web-api-types) — most extensive set of typed response definitions, including platform-specific responses (Windows, macOS, Linux)
- [Jleagle/steam-go](https://pkg.go.dev/github.com/Jleagle/steam-go/steamapi) — used as a secondary reference for field types and structures not covered in the above

Numeric field widths (`uint32` vs `uint64`) are inferred from value range
and Steam's C++ type definitions. Valve does not publish response schemas
for the Web API.

Last verified: **October 2026**

## Contributing

Contributions are welcome via pull request. Before opening a PR:

- Read the style guide below
- Verify any new or updated endpoint against the live API
- Include the raw response in your PR description

To report an inaccuracy, open an issue with the endpoint name and the
discrepancy you found.

## Style Guide

### Terminology

- Use "endpoint" for individual API methods (e.g. `GetPlayerSummaries`)
- Use "interface" for the service group (e.g. `ISteamUser`)
- Use "parameter" for query/body inputs, "field" for response properties

### Formatting

- All code blocks use `bash` for requests, `json` for responses
- Parameter tables use: Name | Type | Required | Description
- Response examples use real data with PII redacted (`[REDACTED]`)
- Dates in prose use the format "Month YYYY" (e.g. "October 2026")

### Structure

- Each endpoint page follows: Overview → Parameters → Example Request
  → Example Response → Response Fields → Notes
- Notes section is optional; use it for edge cases, rate limits, or
  behavioral quirks not in the official docs

## License

[MIT / CC BY-SA / etc.]