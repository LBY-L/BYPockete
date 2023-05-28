# Launch module
# I don't use portablemc api because i'm underage, im just exist XD 

def Launch8():
    import urllib3, os, subprocess, json
    from rich import print
    def download(name, url):
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        with open(f"{name}", 'wb') as f:
            f.write(response.data)

    with open('User.json', 'r') as file:
        user = json.load(file)

    with open('ModsMirrors.json', 'r') as file:
        mirrors = json.load(file)

    if os.path.isdir("Minecraft_1.8"):
        versionDef = os.listdir("Minecraft_1.8/versions")
        for i in versionDef:
            if not i == "1.8.9":
                version = list(versionDef)
                version.remove("1.8.9")
        print("[  OK  ] Launching")
        subprocess.run(['portablemc', '--main-dir', 'Minecraft_1.8', 'start', '-m', '-l', user["MicrosoftLogin"], versionDef[0]])
    else:
        os.mkdir("Minecraft_1.8")
        os.mkdir("Minecraft_1.8/mods")
        os.mkdir("Minecraft_1.8/mods_disabled")
        os.mkdir("Minecraft_1.8/versions")
        print("[      ] Downloading Minecraft")
        subprocess.run(['portablemc', '--main-dir', "Minecraft_1.8", '--work-dir', "Minecraft_1.8", 'start', '--dry', '1.8.9'])
        print("[  OK  ] Minecraft downloaded")
        print("[      ] Downloading Fabric")
        download("FabricInstall-1.8.jar", mirrors["Version 1.8"]["Resources"]["FabricInstaller"])
        print("[  OK  ] Fabric downloaded")
        print("[      ] Downloading mods")
        Names = list(mirrors["Version 1.8"]["Mods"].keys())
        for And in Names:
            MirrorDownloads = mirrors["Version 1.8"]["Mods"][And]
            download(f"Minecraft_1.8/mods/{And}.jar", MirrorDownloads)
        print("[  OK  ] Mods downloaded")
        subprocess.run(['java', '-jar', 'FabricInstall-1.8.jar', 'client', '-mcversion', '1.8.9', '-dir', "Minecraft_1.8"])
        print("[  OK  ] Launching")
        versionDef = os.listdir("Minecraft_1.8/versions")
        for i in versionDef:
            if not i == "1.8.9":
                version = list(versionDef)
                version.remove("1.8.9")
        subprocess.run(['portablemc', '--main-dir', 'Minecraft_1.8', 'start', '-m', '-l', user["MicrosoftLogin"], versionDef[0]])

def Launch6():
    import urllib3, os, subprocess, json, zipfile
    from rich import print
    def download(name, url):
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        with open(f"{name}", 'wb') as f:
            f.write(response.data)

    with open('User.json', 'r') as file:
        user = json.load(file)

    with open('ModsMirrors.json', 'r') as file:
        mirrors = json.load(file)

    if os.path.isdir("Minecraft_1.16"):
        versionDef = os.listdir("Minecraft_1.16/versions")
        for i in versionDef:
            if not i == "1.16_combat-6":
                version = list(versionDef)
                version.remove("1.16_combat-6")
        print("[  OK  ] Launching")
        subprocess.run(['portablemc', '--main-dir', 'Minecraft_1.16', 'start', '-m', '-l', user["MicrosoftLogin"], versionDef[0]])
    else:
        os.mkdir("Minecraft_1.16")
        os.mkdir("Minecraft_1.16/mods")
        os.mkdir("Minecraft_1.16/mods_disabled")
        os.mkdir("Minecraft_1.16/versions")
        print("[      ] Downloading Minecraft version from Mojang")
        download("Minecraft-1.16-Combat-6.zip", mirrors["Version Test"]["Resources"]["Minecraft"])
        zip_file = zipfile.ZipFile("Minecraft-1.16-Combat-6.zip")
        zip_file.extractall("Minecraft_1.16/versions/"); zip_file.close()
        print("[  OK  ] Minecraft version downladed")
        print("[      ] Downloading minecraft")
        subprocess.run(['portablemc', '--main-dir', "Minecraft_1.16", '--work-dir', "Minecraft_1.16", 'start', '--dry', '1_16_combat-6'])
        print("[  OK  ] Minecraft downloaded")
        print("[      ] Downloading Fabric")
        download("FabricInstall-1.16.jar", mirrors["Version Test"]["Resources"]["FabricInstaller"])
        print("[  OK  ] Fabric Downloaded")
        subprocess.run(['java', '-jar', 'FabricInstall-1.16.jar', 'client', '-mcversion', '1.16_combat-6', '-dir', "Minecraft_1.16"])
        
        # Donwload the mods
        print("[      ] Downloading mods")
        Names = list(mirrors["Version Test"]["Mods"].keys())

        for And in Names:
            MirrorDownloads = mirrors["Version Test"]["Mods"][And]
            download(f"Minecraft_1.16/mods/{And}.jar", MirrorDownloads)
        print("[  OK  ] Mods downloaded")
        # A error in the descompression, the . are converted in  _

        os.rename("Minecraft_1.16/versions/1_16_combat-6", "Minecraft_1.16/versions/1.16_combat-6")
        os.rename("Minecraft_1.16/versions/1.16_combat-6/1_16_combat-6.jar", "Minecraft_1.16/versions/1.16_combat-6/1.16_combat-6.jar")
        os.rename("Minecraft_1.16/versions/1.16_combat-6/1_16_combat-6.json", "Minecraft_1.16/versions/1.16_combat-6/1.16_combat-6.json")
        print("[  OK  ] Launching")
        versionDef = os.listdir("Minecraft_1.16/versions")
        for i in versionDef:
            if not i == "1.16_combat-6":
                version = list(versionDef)
                version.remove("1.16_combat-6")

        subprocess.run(['portablemc', '--main-dir', 'Minecraft_1.16', 'start', '-m', '-l', user["MicrosoftLogin"], versionDef[0]])

def Launch9():
    import urllib3, os, subprocess, json
    with open('User.json', 'r') as file:
        user = json.load(file)

    with open('ModsMirrors.json', 'r') as file:
        mirrors = json.load(file)

    if os.path.isdir("Minecraft_1.19"):
        print("[  OK  ] Launching")
        subprocess.run(['portablemc', '--main-dir', 'Minecraft_1.19', 'start', '-m', '-l', user["MicrosoftLogin"], "quilt:1.19.4"])
    else:
        os.mkdir("Minecraft_1.19")
        os.mkdir("Minecraft_1.19/versions")
        os.mkdir("Minecraft_1.19/mods")
        os.mkdir("Minecraft_1.19/mods_disabled")
        print("[      ] Downloading Minecraft")

        subprocess.run(['portablemc', '--main-dir', "Minecraft_1.19", '--work-dir', "Minecraft_1.19", 'start', '--dry', '1.19.4'])
        print("[  OK  ] Minecraft downloaded")
        print("[      ] Downloading mods")
        Names = list(mirrors["Version 1.19"]["Mods"].keys())

        for And in Names:
            AnotherNames = mirrors["Version 1.19"]["Mods"][And]
            http = urllib3.PoolManager()
            response = http.request('GET', AnotherNames)
            with open(f"Minecraft_1.19/mods/{And}.jar", 'wb') as f:
                f.write(response.data)
        print("[  OK  ] Mods downloaded")
        print("[  OK  ] Launching")
        subprocess.run(['portablemc', '--main-dir', 'Minecraft_1.19', 'start', '-m', '-l', user["MicrosoftLogin"], "quilt:1.19.4"])