# DesktopHub

DesktopHub v.1.0 (Python 3.5)

DesktopHub is a desktop application that opens specified directories and websites on the click of a button.

Check the project's [Wiki](https://github.com/Kwistech/DesktopHub/wiki) for more info.

## Installation ##

This program can be ran two ways:

+ Fork the repository and clone it to your local drive.

  From the program's root directory, double-click `main.py`

---

+ Fork the repository and clone it to your local drive.

  From the program's root directory, run the following:

  `python main.py`

## How to Use

The below image is the GUI for DesktopHub:

[![desktophub-gui-with-mods.png](https://s2.postimg.org/icglqecnd/desktophub-gui-with-mods.png)](https://postimg.org/image/58b1dpklh/)

DesktopHub is split into two sections:

**Main section** - Contains the top four buttons (C:, D:, Docs, and DLs). 
                   The button text corresponds to what will open in explorer 
                   or a browser when that button is pressed.

**Module(s)** - Optional "plug-ins" for DesktopHub. On the image to the left,
                there are three modules loaded (below the dotted horizontal line)
                in addition to the main section. Each module takes up 1-2 rows in the GUI.
                The modules shown here (top to bottom) are: python_paths.py, github.py,
                and google_search.py.
            
Note: Modules can be activated and inactivated by moving the module (files in 
      DesktopHub/modules folder with the .py extention) from the modules folder into 
      the inactive modules folder (and visa-versa).
      
## Editing File Paths ##

**Each buttons filepath must be changed to the users path to the equivalent directory!**
As of this writing, the app opens the directories I have set. This means that the app
will use the paths I have given it to open the corresponding directories. If the app
does not find the path specified, it will open explorer in a general directory 
(i.e. My Documents).

To change the paths, open main.py and the module .py files in a script editor and change them
to match the equivalent directory on your system. Provide the full path name.

Note: You may have to add an escape character to the first backslash (\\) for the path to work.

## Creating Your Own Modules ##

If you want to create your own modules for DesktopHub, I suggest you do the following:

1. Create a new .py file in the module directory with the name of your new module
2. Copy all the contents from an existing module and paste it into your new module
3. Rename function(s) and edit the pasted code to your liking (follow pasted code as a guideline)
4. Edit main.py by adding a try/except block with the import to your module (see main.py lines 6-17)
5. Add try/except block to _load_modules(self) method with call to your module (pass in parameters, if any)
6. In except block, let the call to your modules be None (i.e. `mod4 = None`); add module to return tuple (line 86)
7. Add elif block to action(self, text, query=None) method with the action that your modules initiates upon button press.

---

I plan to add more features and modules to this app in the future. Any suggestions and/or recommendations are welcome.
Feel free to try this app out for yourself!


