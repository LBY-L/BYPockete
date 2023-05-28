import json

with open('VerConfigs.json', 'r') as file:
    Ver = json.load(file)

with open('User.json', 'r') as file:
    User = json.load(file)

def Renew():
    Names = list(Ver["Versions"].keys())
    for i in Names:
        if Ver["Versions"][i]:
            Version = i
    if Version == "1.8":
        MainFolder = "Minecraft_1.8"; MainCommand = "from LaunchFile import Launch8; Launch8()"
        return MainFolder, MainCommand 
    elif Version == "Combat Test 8c":
        MainFolder = "Minecraft_1.16"; MainCommand = "from LaunchFile import Launch6; Launch6()"
        return MainFolder, MainCommand 
    elif Version == "1.19":
        MainFolder = "Minecraft_1.19"; MainCommand = "from LaunchFile import Launch9; Launch9()"
        return MainFolder, MainCommand 