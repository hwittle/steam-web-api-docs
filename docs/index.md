# Welcome to the unofficial Steam Web API Documentation

The Steam Web API is a set of HTTP endpoints provided by Valve that allows 
developers to access Steam user data, game information, and community features. 
This documentation covers a curated set of commonly used endpoints with 
detailed parameter descriptions, example requests, and real response samples.

This is an unofficial community resource. For the full list of available 
interfaces, visit the official 
[Steam Web API documentation](https://developer.valvesoftware.com/wiki/Steam_Web_API).

## Getting Started
A Steam account is needed in order to obtain a Steam Web API Key. You can create an account at [store.steampowered.com/join](https://store.steampowered.com/join)

Once you have logged into your Steam account, obtain a Steam Web API Key at [steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey). This key identifies your application to Steam and determines which endpoints you can access based on your account's permissions (some endpoints require a game purchase or developer registration).

???+ warning
    Keep your API key safe and do not embed API keys into source code. Use your server's platform secret vault to provide keys to your server-side applications or environment variables if the platform does not offer a secret vault.

???+ note
    Many Steam Web API endpoints return limited or no data when a user's Steam Community profile is set to Private or Friends Only. Requests using your own API key for your own Steam ID will bypass these restrictions.

---
### API Request Structure
The template to call a Steam Web API method is as follows:

```
https://api.steampowered.com/<INTERFACE>/<METHOD>/v<VERSION>/?key=<YOUR_API_KEY>&format=<OUTPUT>
```

---
### Making Your First Request
To find interfaces and methods, call the interface/method, ISteamWebAPIUtil/GetSupportedAPIList.

???+ note
    By default, it only displays APIs that do not require an API key. When passed a key parameter (`key=<YOUR_API_KEY>`), GetSupportedAPIList will return all APIs that your key can access.

=== "No API Key"
    ```
    https://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/
    ```
=== "With API Key"
    ```
    https://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key=YOUR_API_KEY
    ```

## Output Formats
All Steam Web API calls can be returned in 3 different formats: JSON, XML, and VDF.

???+ note
    If no format parameter (`format=OUTPUT`) is passed, the output format will default to JSON.

=== "JSON"
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
                }
                ...
            ]
        }
    }
    ```

=== "XML"
    Output returned as an XML document.

    - XML attributes are not used.
    - The arrays are represented as a series of labeled sub-elements tags describing the content contained inside.
    - Null is presented as the word "null" between the element tags.
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE apilist>
    <apilist>
        <interfaces>
            <interface>
                <name>IClientStats_1046930</name>
                <methods>
                    <method>
                        <name>ReportEvent</name>
                        <version>1</version>
                        <httpmethod>POST</httpmethod>
                        <parameters></parameters>
                    </method>
                </methods>
            </interface>
            ...
        </interfaces>
    </apilist>
    ```

=== "VDF"
    Output returned as a VDF file.

    - Valve's internal data format.
    - The arrays are represented as a named VDF array describing  the types of objects listed within.
    ```
    "apilist"
    {
        "interfaces"
        {
            "0"
            {
                "name"	"IClientStats_1046930"
                "methods"
                {
                    "0"
                    {
                        "name"	"ReportEvent"
                        "version"	"1"
                        "httpmethod"	"POST"
                        "parameters"
                        {

                        }
                    }
                }
            }
            ...
        }
    }
    ```

## What's Next
Browse the API reference in the sidebar to explore available endpoints, 
or start with [GetPlayerSummaries](get-player-summaries.md) for a 
straightforward introduction to the API.