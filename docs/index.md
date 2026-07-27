# Welcome to the unofficial Steam Web API Documentation

For full documentation visit [developer.valvesoftware.com/wiki/Steam_Web_API](https://developer.valvesoftware.com/wiki/Steam_Web_API).

## Getting Started
A Steam account is needed in order to obtain a Steam Web API Key. You can create an account at [store.steampowered.com/join](https://store.steampowered.com/join)

Once you have logged into your Steam account, obtain a Steam Web API Key at [steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey).

---

To find interfaces and methods, call [ISteamWebAPIUtil/GetSupportedAPIList](https://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/).

!!! note
    By dafault, it only displays APIs that do not require an API key.

    When passed a key parameter (`key=<your API key>`), GetSupportedAPIList will return all APIs that your key can access.

## Output Formats
All Steam Web API calls can take the following form:
`http://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>`
#### JSON
Output returned in the JSON format.

- The arrays are represented as a named array describing the types of objects listed within.
- Null is present as json's null
``` json
{
    "apilist": {
        "interfaces": [
            {
                "name": "IClientStats_1046930",
                "methods": [
                    {
                        "name": "ReportEvent",
                        "version": 1,
                        "httpmethod": "POST",
                        "parameters": []
                    }
                ]
            },
    }
}
```

#### XML
Output returned as an XML document.

- XML attributes are not used.
- The arrays are represented as a series of labeled sub-elements tags describing the content contained inside.
- Null is presented as the word "null" between the element tags.

#### VDF
Output returned as a VDF file.

- Valve's internal data format.
- The arrays are represented as a named VDF array describing  the types of objects listed within.