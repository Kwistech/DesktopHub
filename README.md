# DesktopHub

DesktopHub v.1.0

DesktopHub is a desktop application that opens specified directories and websites on the click of a button.

## Installation ##

This program can be ran two ways:

+ Fork the repository and clone it to your local drive.

  From the program's root directory, double-click `main.py`

---

+ Fork the repository and clone it to your local drive.

  From the program's root directory, run the following:

  `python main.py`

##How to Use

The below image is the GUI for DesktopHub:

<img src="http://s33.postimg.org/xa94b0ojz/desktophub_gui_with_mods.png" align="left" hspace="10">

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
does not file the path specified, it will open explorer to a general directory 
(i.e. My Documents).

To change the paths, open main.py and the module .py files in a script editor and change them
to match the equivalent directory on your system. Provide the full path name.

Note: You may have to add an escape character to the first backslash (\) for the path to work.


