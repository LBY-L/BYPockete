import typer, os, subprocess, json, shutil
from time import sleep

app = typer.Typer()

loginUser = typer.Typer()
app.add_typer(loginUser, name="login", help="Manage your Minecraft account")
UpdateMine = typer.Typer()
app.add_typer(UpdateMine, name="update", help="Updates the Minecraft versions")

ALLOWED_VERSIONS = ["1.8", "Combat Test", "1.19"]

@app.command()
def run():
    """
    Run BYPockete lancher
    """
    typer.echo("Starting the launcher...")
    sleep(0.5)
    ActDirecory = os.path.abspath(__file__)
    print(ActDirecory)
    subprocess.run(["python", "LauncherTUI.py"])

@UpdateMine.command("mirrors")
def mirrors():
    """
    Update the mirrors
    """
    

@UpdateMine.command("now")
def now(str = typer.Argument(..., metavar='VERSION', help=f"Specify the version to update (options: {', '.join(ALLOWED_VERSIONS)})")):
    """
    Update Minecraft mods and version (need to specify)
    """
    if os.path.isdir("Minecraft_1.8") or os.path.isdir("Minecraft_1.16") or os.path.isdir("Minecraft_1.19"):
        if str == "1.8" and os.path.isdir("Minecraft_1.8"):
            shutil.rmtree("Minecraft_1.8")
            os.remove("FabricInstall-1.8.jar")
        elif str == "Combat" and os.path.isdir("Minecraft_1.16"):
            shutil.rmtree("Minecraft_1.16")
            os.remove("Minecraft-1.16-Combat-6.zip")
            os.remove("FabricInstall-1.16.jar")
        elif str == "1.19" and os.path.isdir("Minecraft_1.19"):
            shutil.rmtree("Minecraft_1.19")
    else:
        typer.echo(f"ERROR: You don't have any version. Available versions: {', '.join(ALLOWED_VERSIONS)}")

@app.command()
def uninstall(str = typer.Argument(..., metavar='VERSION', help=f"Specify the version to uninstall (options: {', '.join(ALLOWED_VERSIONS)})")):
    """
    Uninstall Minecraft versions 
    """
    if str not in ALLOWED_VERSIONS:
        typer.echo(f"ERROR: Invalid version '{str}'. Available versions: {', '.join(ALLOWED_VERSIONS)}")

    if os.path.isdir("Minecraft_1.8") or os.path.isdir("Minecraft_1.16") or os.path.isdir("Minecraft_1.19"):
        if str == "1.8" and os.path.isdir("Minecraft_1.8"):
            shutil.rmtree("Minecraft_1.8")
            os.remove("FabricInstall-1.8.jar")
        elif str == "Combat" and os.path.isdir("Minecraft_1.16"):
            shutil.rmtree("Minecraft_1.16")
            os.remove("Minecraft-1.16-Combat-6.zip")
            os.remove("FabricInstall-1.16.jar")
        elif str == "1.19" and os.path.isdir("Minecraft_1.19"):
            shutil.rmtree("Minecraft_1.19")
    else:
        typer.echo(f"ERROR: You don't have any version. Available versions: {', '.join(ALLOWED_VERSIONS)}")

@loginUser.command("relogin")
def relogin():
    """
    Enable re-login if you get an error
    """
    with open('LBYSLoginUser.json', 'r') as file:
        User = json.load(file)

    User["MicrosoftLogin"] = ""
    User["HasBeenReLog"] = True
    with open('LBYSLoginUser.json', 'w') as file:
        json.dump(User, file)
    subprocess.run(["python", "LBYSLauncherTUI.py"])

@loginUser.command("logout")
def logout():
    """
    Logout of your Minecraft account
    """

    with open('LBYSLoginUser.json', 'r') as file:
        User = json.load(file)

    subprocess.Popen(['portablemc', 'logout', '-m', User["MicrosoftLogin"]], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    User["MicrosoftLogin"] = ""
    User["HasBeenReLog"] = False
    with open('LBYSLoginUser.json', 'w') as file:
        json.dump(User, file)


if __name__ == "__main__":
    app()