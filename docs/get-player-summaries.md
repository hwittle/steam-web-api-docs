# GetPlayerSummaries v0002

Retrieves the basic profile information for a list of 64-bit Steam IDs.
```
ISteamUser/GetPlayerSummaries/v0002/?key=<your API key>&<arguments>
```

### Arguments

{{ param("steamids", "list", "Comma-delimited list of 64 bit Steam IDs to return profile information for. Up to 100 Steam IDs can be requested.") }}
{% raw %}
```
&steamids=<list of 64-bit Steam IDs separated by commas>
```
{% endraw %}
---
{{ param("format", "list", "Output format: json (default), xml, vdf.")}}
{% raw %}
```
&format=<json, xml, or vdf>
```
{% endraw %}

### Returns