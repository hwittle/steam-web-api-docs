# Contributing

## Report a problem

To report an inaccuracy, [open an issue](https://github.com/hwittle/steam-web-api-docs/issues) with the endpoint name, the parameters you sent, and the response you received. Remove your API key from any URL before you paste it. Do not post data from private profiles.

## Submit a change

Use the Edit this page button on any page, or open a pull request from a fork. Before you open a pull request:

- Read the style guide below.
- Verify new or changed behavior against the live API.
- Attach the response with your API key and any private data removed.
- Run `mkdocs build --strict` and fix every warning. The site build runs the same check, so broken links fail it.

## Preview locally

Install the dependencies listed in `requirements.txt`, run `mkdocs serve`, and open the address it prints.

## Endpoint page template

Copy an existing endpoint page, such as GetOwnedGames, and replace its contents.

### Front matter

Each page starts with YAML front matter. The at-a-glance strip is built from it.

- `title`, `description`: the method name and a one-sentence summary.
- `interface`, `method`, `version`: exactly as they appear in the request URL.
- `http_method`: `GET` or `POST`.
- `auth`, `privacy`: use the values existing pages use. A new value also needs a label added to `glance()` in `main.py`.
- `formats`: the formats you captured samples for.
- `last_verified`: the date you last tested the endpoint against the live API. Change it only when you retest. It is separate from the page's revision date.
- `tags`: the interface name, a topic, and `privacy-dependent` where it applies.

### Components

- `param(name, type, description, required=True)` writes a parameter. Leave out `required` for optional parameters.
- `param_bullet(name, type, description, extra)` writes a field nested under a response object.
- `glance()` writes the at-a-glance strip.
- `ref-grid` places parameters on the left and examples on the right on wide screens. Add `ref-grid--stack` to pages with very long parameter or field lists.
- `service_note()` writes the standard note for Service interfaces. Use it under the Request URL on those pages.
- `differs(text)` writes a "Differs from Valve's reference" note. Place it under the parameter or field it concerns.

### Unverified claims

Mark anything you have not tested with an HTML comment that starts with `VERIFY:`. Resolve every one before you update `last_verified`.

## Style guide

### Terminology

- **Interface:** a group of methods, such as `ISteamUser`.
- **Method:** Valve's name for a callable operation, such as `GetPlayerSummaries`. Each method has one page, and this site calls that page an endpoint.
- **Parameter:** an input to a request.
- **Field:** a property in a response.
- **Service interface:** an interface whose name ends in `Service`, such as `IPlayerService`. Its methods accept parameters in the `input_json` query parameter.

### Writing

- Use sentence case for headings.
- Address the reader as "you" and write in the present tense.
- State only behavior that was tested. Put a finding next to the parameter or field it concerns. Use a "Differs from Valve's reference" note when it conflicts with the Steamworks reference. Use a Notes section at the end of the page only for behavior that does not belong to one field, and leave it out when there is nothing to add.
- Write descriptions in your own words. Do not copy wording from Valve's reference or the community wiki.

### Formatting

- Parameters and fields show the name and type on one line, with the description below. A Required badge marks required parameters. There are no tables.
- Types use Valve's names (`uint32`, `uint64`, `bool`, `string`). Arrays add brackets, such as `uint32[]`.
- Request URLs use a plain code block. Responses use `json`, `xml`, or a plain block for VDF.
- Placeholders are uppercase with underscores, such as `YOUR_API_KEY`. Never include a real key.
- Samples come from accounts whose owners made them public, or from accounts you own. Do not publish data that was visible to you only because you are friends with the account or because you own it. If a sample needs data of that kind, replace it with a placeholder and say so above the sample. If a profile you used becomes private, recapture the sample from another public account before you update `last_verified`.
- Dates are written out in full, such as 14 October 2026.

### Page structure

Title with version badge, at-a-glance strip, Request, Parameters, Response, and an optional Notes section.

### Requests and responses

- Requests to Service interfaces pass parameters in `input_json`. Show a Readable tab and a URL-encoded tab, and give a minimal and a full example.
- Write the version as it appears in the request URL, such as `v0001`.
- When a field is represented differently between formats, explain it in a Format differences note.
- Errors shared by many methods belong on the Errors page. Errors specific to one method go under Behavior and observations.