import json
from ActDir import ActDir

fill = {
    "Versions": {
                "1.8": True,
                "Combat Test 8c": False, 
                "1.19": False
                }
}

MainDir = ActDir()
with open(f'{MainDir}VerConfigs.json', 'w') as file:
    json.dump(fill, file)

fill2 = {
    "MicrosoftLogin": "",
    "HasBeenReLog": False
}

with open(f'{MainDir}User.json', 'w') as file:
    json.dump(fill2, file)
