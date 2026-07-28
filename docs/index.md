# Welcome to the unofficial Steam Web API Documentation

For full documentation visit [developer.valvesoftware.com/wiki/Steam_Web_API](https://developer.valvesoftware.com/wiki/Steam_Web_API).

## Getting Started
A Steam account is needed in order to obtain a Steam Web API Key. You can create an account at [store.steampowered.com/join](https://store.steampowered.com/join)

Once you have logged into your Steam account, obtain a Steam Web API Key at [steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey).

!!! warning
    Keep your API key safe and do not embed API keys into source code. Use your server's platform secret vault to provide keys to your server-side applications or environment variables if the platform does not offer a secret vault.

---
The template to call a Steam Web API method is as follows:
> `api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>`

To find interfaces and methods, call the interface/method, ISteamWebAPIUtil/GetSupportedAPIList
> `https://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/`

!!! note
    By default, it only displays APIs that do not require an API key.

    When passed a key parameter (`key=<your API key>`), GetSupportedAPIList will return all APIs that your key can access.

## Output Formats
All Steam Web API calls can be returned in 3 different formats: JSON, XML, and VDF.

!!! note
    If no format parameter (`format=<format>`) is passed, the output format will default to JSON.

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
            }
        ]
    }
}
```

#### XML
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
    </interface>
</apilist>
```

#### VDF
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
    }
}
```