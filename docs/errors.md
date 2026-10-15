---
title: Common errors
description: The HTTP errors and empty responses you are most likely to see when calling the Steam Web API, with likely causes and fixes.
last_verified: 14 October 2026
---

# Common errors

This page covers errors that many Steam Web API methods share. It is not a complete list. Valve does not publish one, and this project documents only what it has observed. Errors that belong to a single method are described on that method's page under "Behavior and observations."

When a request fails, check the HTTP status code first, then find it below.

## 400 Bad request

The request was malformed or a required parameter is missing or invalid.

**Likely causes**

- A required parameter is missing, such as `steamid`.
- A value has the wrong type, such as text where a number is expected.
- On a Service interface, the `input_json` value is not valid JSON, or it was not percent-encoded when the URL was built by hand.

**What to try**

- Compare your request with the Request section on the endpoint page.
- Paste your `input_json` value into a JSON validator.
- Check that the Steam ID is the 64-bit form, a 17-digit number.

<!-- VERIFY: confirm the status code and any response body for a missing parameter and for invalid input_json. -->

## 401 Unauthorized

The request reached Steam, but you are not allowed to see the data you asked for.

**Likely causes**

- The account you asked about has a private profile or a private friends list.
- The method requires a different kind of key or access than yours.

**What to try**

- Ask about an account with a public profile to confirm the request itself works.
- Check the Privacy value in the at-a-glance strip on the endpoint page.

<!-- VERIFY: confirm which methods return 401 for private profiles, for example GetFriendList. -->

## 403 Forbidden

Steam rejected your API key, or the key cannot call this method.

**Likely causes**

- The `key` parameter is missing, misspelled, or has extra characters or spaces.
- The key was revoked or replaced, or you copied an old one.
- The method needs a key type you do not have, such as a publisher key.

**What to try**

- Copy the key again from your registration page and check for stray characters.
- Call `ISteamWebAPIUtil/GetSupportedAPIList` with your key to see which methods it can access. See [Make your first request](index.md#make-your-first-request).
- Make sure you are using the public host, `api.steampowered.com`, unless you have a publisher key.

<!-- VERIFY: confirm the response body returned for a missing key and for an invalid key. -->

## 404 Not found

The URL does not match a method Steam serves.

**Likely causes**

- A typo in the interface name, method name, or version.
- The version in the URL does not exist for that method, for example `v1` where the page shows `v0001`.

**What to try**

- Copy the request URL from the endpoint page.
- Look up the exact names and versions with `GetSupportedAPIList`.

<!-- VERIFY: confirm 404 versus another status for a wrong method name and for a wrong version. -->

## 405 Method not allowed

You used the wrong HTTP method.

**Likely causes**

- You sent a GET request to a method that requires POST, or the reverse.

**What to try**

- Check the HTTP method value on the endpoint page, or in the `GetSupportedAPIList` response.

<!-- VERIFY: confirm the status code by sending the wrong HTTP method to a tested endpoint. -->

## 429 Too many requests

You have sent too many requests in a short time.

**What to try**

- Stop sending requests and wait before you retry.
- Cache responses you already have instead of requesting them again.
- Add a delay between requests, and increase it each time a retry fails.

Steam's Web API terms set usage limits. Check Valve's current terms for the numbers, because this project has not measured them.

<!-- VERIFY: confirm the limits against Valve's current Steam Web API terms, and whether a Retry-After header is sent. -->

## 500 and 503 Server errors

Steam had a problem handling the request.

**Likely causes**

- Steam services are temporarily unavailable.
- Some invalid inputs may also produce a 500 instead of a 400.

**What to try**

- Retry after a short wait.
- If it keeps failing, check your parameters against the endpoint page, then try a different Steam ID.

<!-- VERIFY: confirm which invalid inputs produce 500. Do not state a cause that was not reproduced. -->

## Empty or missing data

A request can succeed with a 200 status and still return no useful data.

**Likely causes**

- The account's profile or game details are private, so the response is empty or leaves out fields. See [Profile privacy](index.md#profile-privacy).
- The `steamid` is valid but belongs to an account with nothing to return, such as no owned games.
- A filter, such as `appids_filter`, matched nothing.
- A field you expected only appears for some items. Each endpoint page notes where this applies.

**What to try**

- Repeat the request with an account you own and a public profile.
- Remove optional parameters one at a time to see which one changes the result.

<!-- VERIFY: record the exact empty response shape in JSON, XML, and VDF for a private profile. -->

## Report a missing error

If you hit an error that is not listed here, [open an issue](https://github.com/hwittle/steam-web-api-docs/issues) with the status code, the response body, and the request with your API key removed. See [Contributing](contributing.md).