import json

twitterCredentials = dict()
twitterCredentials['Consumer_Key']='45wGsIXPF2NfyzlAjWCoEG6yZ'
twitterCredentials['Consumer_Secret']='bWvfTOGnegVbVEvnRMWl8BWJsjkjVQgvzYjVGAAb6daALewe6a'
twitterCredentials['Access_Key']='1075558017326821376-R9Gpmdmbml1gKzsLw4V2PiI6chUZOA'
twitterCredentials['Access_Secret']='q7FehYIpZzoKJhwEZGQWTR1fESBFJwHlIMOBzLX0ut8tv'

with open('TwitterCredentials.json', 'w') as secretInfo:
    json.dump(twitterCredentials, secretInfo, indent=4, sort_keys=True)
