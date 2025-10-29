# APIs are application programming interface- refer to third party services that we can write code that talk to
# you can write code that pretends to be a browser then connects to a third party api, on a server, and download some data that you can
# incorporate into your own program
# request package - allows you to make web requests, internet requests using python code as though you were a browser yourself
# for example you can automate the retrieval of urls that with http or https
# it can be installed in the command-line
# For example we will use apple music api to download song files
# https://itunes.apple.com/search?entity=song&limit=1&term=weezer in the link:
# entity = song provides song specifically and not ablum
# limit = 1 means only one song
# term = weezer means the artist is called weezer

# When you search the link it download json files of the song specified or even songs
# JSON(javascript object notation)and is related to js, is used as a language agnostic format for exchanging data between computers,
# meaning you can use any other language to read the json or write it as well
# and its a completely text-based format, if you visit the url, what gets downloaded is texts formatted in a standard way with colons,
# brackets, quotes
# so json is like an api
# For example

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())


# json library - allows you to manipulate json data and even print it in a formatted way that is easier to understand, for example

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))

# To print a specific value or even multiple values, eg printing the name of the song
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])

# break is used to exit from a loops while sys.exit is used to terminate from the whole program