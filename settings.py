import _process
#
from os import listdir
from PyQt5.QtCore import QThread, pyqtSignal, QSize, Qt, QMetaObject
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, \
    QProgressBar, QPushButton, QApplication, QMainWindow, QTabWidget, QTabBar, QMessageBox, QCheckBox
from PyQt5.QtGui import QPixmap, QIcon, QFont, QFontDatabase
from minecraft_launcher_lib.utils import get_minecraft_directory, get_version_list, generate_test_options, get_installed_versions
from minecraft_launcher_lib.forge import list_forge_versions, install_forge_version, supports_automatic_install, \
    run_forge_installer, forge_to_installed_version, find_forge_version
from minecraft_launcher_lib.fabric import get_all_minecraft_versions, install_fabric
from minecraft_launcher_lib.quilt import install_quilt
from minecraft_launcher_lib.quilt import get_all_minecraft_versions as get_all_minecraft_versions_quilt
from minecraft_launcher_lib.install import install_minecraft_version
from minecraft_launcher_lib.command import get_minecraft_command, VersionNotFound
from random_username.generate import generate_username
from uuid import uuid1
from subprocess import call
from sys import argv, exit
import re
#
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 450
MAIN_FONT_SIZE = 12
SUB_FONT_SIZE = 20
DIRECTORY_NAME = "pitLauncher"
MAIN_COLOR = 1
SUB_COLOR = 1
MAIN_FONT_COLOR = 1
SUB_FONT_COLOR = 1
#
username = _process.Process.load(_process.Process(), 'username')
print(username)
last_vanila_version = _process.Process.load(_process.Process(), 'last_vanila_version')
if last_vanila_version is None:
    last_vanila_version = ''

last_forge_version = _process.Process.load(_process.Process(), 'last_forge_version')
if last_forge_version is None:
    last_forge_version = ''

last_fabric_version = _process.Process.load(_process.Process(), 'last_fabric_version')
if last_fabric_version is None:
    last_fabric_version = ''

last_quilt_version = _process.Process.load(_process.Process(), 'last_quilt_version')
if last_quilt_version is None:
    last_quilt_version = ''

last_mod_loader = _process.Process.load(_process.Process(), 'last_mod_loader')
if last_mod_loader is None:
    last_mod_loader = 0
else:
    last_mod_loader = int(last_mod_loader)


def f_t(value):
    if value is None: value = False
    if value == "True": value = True
    else: value = False
    return value


show_all_vanila = f_t(_process.Process.load(_process.Process(), 'show_sp_vanila'))
show_all_fabric = f_t(_process.Process.load(_process.Process(), 'show_sp_fabric'))
show_all_quilt = f_t(_process.Process.load(_process.Process(), 'show_sp_quilt'))
show_cutted_forge = f_t(_process.Process.load(_process.Process(), 'show_cutted_forge'))
show_all_forge = f_t(_process.Process.load(_process.Process(), 'show_all_forge'))

if show_cutted_forge:
    last_forge_version = last_forge_version.split('-')[0]
