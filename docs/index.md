# Welcome to the unofficial Steam Web API Documentation

For full documentation visit [developer.valvesoftware.com/wiki/Steam_Web_API](https://developer.valvesoftware.com/wiki/Steam_Web_API).

## Getting Started
A Steam account is needed in order to obtain a Steam Web API Key. You can create an account at [store.steampowered.com/join](https://store.steampowered.com/join)

Once you have logged into your Steam account, obtain a Steam Web API Key at [steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey).

## Output Formats
All Steam Web API calls can take the following form:
`http://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>`
#### JSON
Output returned in the JSON format.

- The arrays are represented as a named array describing the types of objects listed within.
- Null is present as json's null

#### XML
Output returned as an XML document.

- XML attributes are not used.
- The arrays are represented as a series of labeled sub-elements tags describing the content contained inside.
- Null is presented as the word "null" between the element tags.

#### VDF
Output returned as a VDF file.

- Valve's internal data format.
- The arrays are represented as a named VDF array describing  the types of objects listed within.

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
