import threading, os, subprocess, json, shutil, json
import py_cui

def logoLog():
    with open('ANSI.txt', 'r') as file:
        logo = file.read()
    lines = logo.split("\n")
    return lines

class MinecraftLauncher:
    def __init__(self):
        self.root = py_cui.PyCUI(8, 3)
        self.root.toggle_unicode_borders()
        self.root.set_refresh_timeout(0.1)
        if User["MicrosoftLogin"] == "":
            self.root.set_title("BYPockete - Login")
            self.Login_window()
        else:
            self.Default()

    def Default(self):
        self.DefaultWidgets = self.root.create_new_widget_set(7, 3)
        self.root.set_title("BYPockete")
        self.output_box = self.DefaultWidgets.add_scroll_menu("BYPockete Launcher News", 0, 0, row_span=6, column_span=3)
        self.launch_button = self.DefaultWidgets.add_button('Launch', 6, 1, command=self.LaunchMinecraft)
        self.config_button = self.DefaultWidgets.add_button('Config', 6, 0, command=self.Config_popup)
        self.version_button = self.DefaultWidgets.add_button('Version', 6, 2, command=self.Version_popup)
        self.launch_button.set_color(py_cui.WHITE_ON_GREEN)
        self.config_button.set_color(py_cui.BLACK_ON_WHITE)
        self.version_button.set_color(py_cui.WHITE_ON_MAGENTA)
        lines = logoLog()
        for line in lines:
            self.output_box.add_item(line)
        self.proc = None
        self.root.apply_widget_set(self.DefaultWidgets)

    def Login_window(self):
        self.WindowLogin = self.root.create_new_widget_set(6, 3)
        self.var = self.WindowLogin.add_text_block('Login Minecraft', 2, 0, column_span=3)
        self.var.set_color(py_cui.BLACK_ON_GREEN)
        self.var.set_selected_color(py_cui.BLACK_ON_CYAN)
        self.var.add_key_command(py_cui.keys.KEY_ENTER, self.Login)
        self.root.apply_widget_set(self.WindowLogin)
    
    def Login(self):
        GetVar = self.var.get()
        self.root.show_loading_icon_popup("Now you can login in your browser", "Wait to login")
        def Autenticate():
            subprocess.run(['portablemc', 'login', '-m', GetVar], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            Modified = GetVar.replace('\n', "")
            User["MicrosoftLogin"] = Modified
            with open('User.json', 'w') as file:
                json.dump(User, file)
            self.root.stop_loading_popup()
            if User["HasBeenReLog"]:
                self.root.stop()
            else:
                self.Default()
        t = threading.Thread(target=Autenticate)
        t.daemon = True
        t.start()

    def LaunchMinecraft(self):
        if self.proc is not None:
            return
        Folder, Command = Renew()
        self.proc = subprocess.Popen(['python', '-c', Command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        self.root.set_title('BYPockete - Minecraft Running')
        self.output_box.set_title("Launcher Output")
        self.launch_button.set_title("Launched")
        
        def Update():
            self.output_box.clear()
            self.output_box.add_item("[  OK  ] If this is your first time starting the client it will take a little longer")
            while True:
                line = self.proc.stdout.readline()
                if line == '':
                    break
                self.output_box.add_item(line.strip())
                idk1 = self.output_box.get_absolute_start_pos()
                idk2 = self.output_box.get_absolute_stop_pos()
                WinSpace = idk2[1] - idk1[1]
                AcutualWinSpace = len(self.output_box.get_item_list())
                if WinSpace <= AcutualWinSpace:
                    self.output_box.clear()
            self.proc.stdout.close()
            self.proc.wait()
            self.proc = None
            self.root.set_title('BYPockete')
            self.output_box.set_title("BYPockete News")
            self.output_box.clear()
            self.launch_button.set_title("Launch")
            lineas = logoLog()
            for linea in lineas:
                self.output_box.add_item(linea)

        t = threading.Thread(target=Update)
        t.daemon = True
        t.start()

    def Config_popup(self):
        Folder, Command = Renew()
        if os.path.isdir(Folder):
            mods = os.listdir(f"{Folder}/mods")
            disabledMods = os.listdir(f"{Folder}/mods_disabled")
            if disabledMods == []:
                disabledMods = ['None']
            elif mods == []:
                mods = ['None']
            self.root.show_menu_popup('Config', ['── Enabled mods ──'] + mods + ['── Disabled Mods ──'] + disabledMods, self.Config)
        else:
            self.root.show_error_popup("Error", "Minecraft is not installed")

    def Config(self, mod):
        Folder, Command = Renew()
        mods = os.listdir(f"{Folder}/mods")
        disabledMods = os.listdir(f"{Folder}/mods_disabled")
        if mod in mods:
            shutil.move(f'{Folder}/mods/{mod}', f'{Folder}/mods_disabled')
        elif mod in disabledMods:
            shutil.move(f'{Folder}/mods_disabled/{mod}', f'{Folder}/mods')
        self.Config_popup()

    def Version_popup(self):
        Namesi = list(Ver["Versions"].keys())
        for Veri in Namesi:
            if Ver["Versions"][Veri]:
                Enabledi = Veri
        Disabledi = list(Namesi)
        Disabledi.remove(Enabledi)
        self.root.show_menu_popup('Config', ['── Used Version ──'] + [Enabledi] + ['──── Versions ────'] + Disabledi, self.Version)


    def Version(self, version):
        Names = list(Ver["Versions"].keys())
        if version in Names:
            for i in Names:
                Ver["Versions"][i] = False
            Ver["Versions"][version] = True
            with open("VerConfigs.json", "w") as file:
                json.dump(Ver, file)
        self.Version_popup()

if __name__ == '__main__':
    launcher = MinecraftLauncher()
    launcher.root.start()