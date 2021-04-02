import json
import requests
import sys

def make_url(state, county):
    return ("https://en.wikipedia.org/wiki/%s, %s" % (county, state)).replace(" ", "_")

states = json.loads(open("counties.json").read())

output_states = {}

for state, counties in states.items():
    print(state)
    for county in counties:
        url = make_url(state, county)
        r = requests.get(url)
        if r.status_code == 200:
            output_states[url] = r.text
            print(".", end="")
            sys.stdout.flush()
        else:
            print("\n", state, county, url, "status code:", r.status_code)

with open("countydb.json","w") as fp:
    fp.write(json.dumps(output_states, indent=2))

