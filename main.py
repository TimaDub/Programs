import os
from settings import *
from settings import _process

minecraft_directory = get_minecraft_directory().replace('minecraft', DIRECTORY_NAME)


class LaunchThread(QThread):
    launch_setup_signal = pyqtSignal(str, str)
    progress_update_signal = pyqtSignal(int, int, str)
    state_update_signal = pyqtSignal(bool)

    version_id = ''
    username = ''

    progress = 0
    progress_max = 0
    progress_label = ''

    def __init__(self):
        super().__init__()
        self.launch_setup_signal.connect(self.launch_setup)
        self.modLoader = 0

    def launch_setup(self, version_id, username):
        self.version_id = version_id
        self.username = username

    def update_progress_label(self, value):
        self.progress_label = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)

    def update_progress(self, value):
        self.progress = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)

    def update_progress_max(self, value):
        self.progress_max = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)

    def run(self):
        #
        if self.username == '':
            self.username = generate_username()[0]
        #
        _process.Process.save(_process.Process(), username=self.username)
        _process.Process.save(_process.Process(), last_version=self.version_id)
        _process.Process.save(_process.Process(), last_mod_loader=self.modLoader - 1)
        #
        self.state_update_signal.emit(True)
        if self.modLoader == 1:
            _process.Process.save(_process.Process(), last_vanila_version=self.version_id)
            install_minecraft_version(versionid=self.version_id, minecraft_directory=minecraft_directory,
                                      callback={'setStatus': self.update_progress_label,
                                                'setProgress': self.update_progress,
                                                'setMax': self.update_progress_max})
        elif self.modLoader == 2:
            _process.Process.save(_process.Process(), last_forge_version=self.version_id)
            if supports_automatic_install(self.version_id):
                install_forge_version(versionid=self.version_id, path=minecraft_directory,
                                      callback={'setStatus': self.update_progress_label,
                                                'setProgress': self.update_progress,
                                                'setMax': self.update_progress_max})
            else:
                run_forge_installer(self.version_id)
        elif self.modLoader == 3:
            _process.Process.save(_process.Process(), last_fabric_version=self.version_id)
            install_fabric(minecraft_version=self.version_id, minecraft_directory=minecraft_directory, callback={'setStatus': self.update_progress_label,'setProgress': self.update_progress,'setMax': self.update_progress_max})

        elif self.modLoader == 4:
            _process.Process.save(_process.Process(), last_quilt_version=self.version_id)
            install_quilt(minecraft_version=self.version_id, minecraft_directory=minecraft_directory, callback={'setStatus': self.update_progress_label,'setProgress': self.update_progress,'setMax': self.update_progress_max})

        options = {
            'username': self.username,
            'uuid': str(uuid1()),
            'token': '',
            'disableMultiplayer': False
        }

        try:
            if self.modLoader == 2:
                call(get_minecraft_command(version=forge_to_installed_version(self.version_id), minecraft_directory=minecraft_directory, options=options))
            else:
                call(get_minecraft_command(version=self.version_id, minecraft_directory=minecraft_directory, options=options))
            # if self.modLoader == 1:
            #     call(get_minecraft_command(version=self.version_id, minecraft_directory=minecraft_directory, options=options))
            # elif self.modLoader == 2:
            #     call(get_minecraft_command(version=forge_to_installed_version(self.version_id), minecraft_directory=minecraft_directory, options=options))
            # elif self.modLoader == 3:
            #     for file in listdir(minecraft_directory + '\\versions\\'):
            #         if self.version_id in file and "fabric-loader" in file:
            #             call(get_minecraft_command(version=file, minecraft_directory=minecraft_directory, options=options))
            # elif self.modLoader == 4:
            #     for file in listdir(minecraft_directory + '\\versions\\'):
            #         if self.version_id in file and "quilt-loader" in file:
            #             call(get_minecraft_command(version=file, minecraft_directory=minecraft_directory, options=options))
        except VersionNotFound:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setText("Возникла ошибка в загрузке версии!")
            error_dialog.setWindowTitle("Ошибка загрузки версии")
            error_dialog.setStandardButtons(QMessageBox.Ok)
            error_dialog.exec_()
        self.state_update_signal.emit(False)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.centralwidget = QWidget(self)
        self.current_path = os.getcwd()
        #
        self.logo = QLabel(self.centralwidget)
        self.logo.setMaximumSize(QSize(256, 92))
        self.logo.setText('Pit Launcher')
        self.setWindowTitle("Pit Launcher")
        self.setWindowIcon(QIcon(fr"{self.current_path}\assets\minecraft_ico3.png"))
        self.logo.setPixmap(QPixmap(fr'{self.current_path}\assets\minecraft_title.png'))
        self.logo.setScaledContents(True)
        #
        self.main_font_id = QFontDatabase.addApplicationFont(fr'{self.current_path}\assets\minecraftia.ttf')
        self.main_font_family = QFontDatabase.applicationFontFamilies(self.main_font_id)[0]
        self.main_font = QFont(self.main_font_family)
        self.main_font.setPointSize(MAIN_FONT_SIZE)
        #
        self.sub_font_id = QFontDatabase.addApplicationFont(fr'{self.current_path}\assets\smallest-pixel-7.ttf')
        self.sub_font_family = QFontDatabase.applicationFontFamilies(self.sub_font_id)[0]
        self.sub_font = QFont(self.sub_font_family)
        self.sub_font.setPointSize(SUB_FONT_SIZE)
        #
        self.titlespacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.show_snapshots_checkbox_vanila = QCheckBox("Показать все версии", self.centralwidget)
        self.show_snapshots_checkbox_vanila.clicked.connect(self.show_snapshots_pre_versions)
        self.show_snapshots_checkbox_forge = QCheckBox("Показать все версии лоадера", self.centralwidget)
        self.show_snapshots_checkbox_forge.clicked.connect(self.show_snapshots_pre_versions)
        self.show_snapshots_checkbox_forge_ = QCheckBox("Не показывать версию лоадера", self.centralwidget)
        self.show_snapshots_checkbox_forge_.clicked.connect(self.show_snapshots_pre_versions)
        self.show_snapshots_checkbox_fabric = QCheckBox("Показать все версии", self.centralwidget)
        self.show_snapshots_checkbox_fabric.clicked.connect(self.show_snapshots_pre_versions)
        self.show_snapshots_checkbox_quilt = QCheckBox("Показать все версии", self.centralwidget)
        self.show_snapshots_checkbox_quilt.clicked.connect(self.show_snapshots_pre_versions)
        #
        self.username = QLineEdit(self.centralwidget)
        self.username.setPlaceholderText('Username')
        if username != '':
            self.username.setText(username)
        self.username.setFont(self.main_font)
        #
        self.tab_widget = QTabWidget()
        #
        self.vanila_tab = QWidget()
        self.vanila_layout = QVBoxLayout(self.vanila_tab)
        self.vanila_list = []
        self.version_select_vanilla = QComboBox()
        for version in get_version_list():
            self.vanila_list.append(version["id"])

        self.vanila_clear_list = _process.Process.replace_from_list(self.vanila_list)
        self.vanila_layout.addWidget(self.show_snapshots_checkbox_vanila)
        self.vanila_layout.addWidget(self.version_select_vanilla)
        self.version_select_vanilla.setFont(self.main_font)

        self.forge_tab = QWidget()
        self.forge_layout = QVBoxLayout(self.forge_tab)

        self.version_select_forge = QComboBox()
        self.forge_list = []
        for version in list_forge_versions():
            self.forge_list.append(version)
         #
        self.forge_list_clear, self.forge_list_clear_cut, self.forge_list = _process.Process.forge_version_sort(self.forge_list)
        self.forge_list_clear_cut = _process.Process.sort_versions_list(self.forge_list_clear_cut)

        self.forge_layout.addWidget(self.show_snapshots_checkbox_forge)
        self.forge_layout.addWidget(self.show_snapshots_checkbox_forge_)

        self.forge_layout.addWidget(self.version_select_forge)
        self.version_select_forge.setFont(self.main_font)

        #
        self.fabric_tab = QWidget()
        self.fabric_layout = QVBoxLayout(self.fabric_tab)

        self.version_select_fabric = QComboBox()
        self.fabric_list = []
        self.fabric_list_clear = []
        for version in get_all_minecraft_versions():
            self.fabric_list.append(str(version.values()).split("'")[1])
        self.fabric_list.remove("3D Shareware v1.34")
        self.fabric_list.sort(reverse=True)

        self.fabric_list_clear = _process.Process.replace_from_list(self.fabric_list)
        self.fabric_layout.addWidget(self.show_snapshots_checkbox_fabric)
        self.fabric_layout.addWidget(self.version_select_fabric)
        self.version_select_fabric.setFont(self.main_font)

        #
        self.quilt_tab = QWidget()
        self.quilt_layout = QVBoxLayout(self.quilt_tab)

        self.version_select_quilt = QComboBox()
        self.quilt_list = []
        for version in get_all_minecraft_versions_quilt():
            self.quilt_list.append(str(version.values()).split("'")[1])
        self.quilt_list.sort(reverse=True)

        self.quilt_clear_list = _process.Process.replace_from_list(self.quilt_list)
        self.quilt_layout.addWidget(self.show_snapshots_checkbox_quilt)
        self.quilt_layout.addWidget(self.version_select_quilt)
        self.version_select_quilt.setFont(self.main_font)

        #
        self.show_snapshots_checkbox_vanila.setChecked(show_all_vanila)
        if show_all_vanila:
            for ver in self.vanila_list:
                self.version_select_vanilla.addItem(ver)
        else:
            for ver in self.vanila_clear_list:
                self.version_select_vanilla.addItem(ver)
        self.show_snapshots_checkbox_forge.setChecked(show_all_forge)
        if show_all_forge:
            for ver in self.forge_list:
                self.version_select_forge.addItem(ver)
        else:
            for ver in self.forge_list_clear:
                self.version_select_forge.addItem(ver)
        self.show_snapshots_checkbox_forge_.setChecked(show_cutted_forge)
        if show_cutted_forge:
            self.version_select_forge.clear()
            for ver in self.forge_list_clear_cut:
                self.version_select_forge.addItem(ver)
        else:
            if show_all_forge:
                self.show_snapshots_checkbox_forge_.setDisabled(True)
                self.version_select_forge.clear()
                for ver in self.forge_list:
                    self.version_select_forge.addItem(ver)
        self.show_snapshots_checkbox_fabric.setChecked(show_all_fabric)
        if show_all_fabric:
            for ver in self.fabric_list:
                self.version_select_fabric.addItem(ver)
        else:
            for ver in self.fabric_list_clear:
                self.version_select_fabric.addItem(ver)
        self.show_snapshots_checkbox_quilt.setChecked(show_all_quilt)
        if show_all_quilt:
            for ver in self.quilt_list:
                self.version_select_quilt.addItem(ver)
        else:
            for ver in self.quilt_clear_list:
                self.version_select_quilt.addItem(ver)
        try:
            if last_vanila_version != '':
                self.version_select_vanilla.setCurrentIndex(self.vanila_list.index(last_vanila_version))
            else:
                self.version_select_vanilla.setCurrentIndex(0)
        except:
            self.version_select_vanilla.setCurrentIndex(0)
        #
        try:
            if last_forge_version != '':
                if show_all_forge:
                    self.version_select_forge.setCurrentIndex(self.forge_list.index(last_forge_version))
                elif show_all_forge is False and show_cutted_forge is False:
                    self.version_select_forge.setCurrentIndex(self.forge_list_clear.index(last_forge_version))
                elif show_all_forge is False and show_cutted_forge is True:
                    self.version_select_forge.setCurrentIndex(self.forge_list_clear_cut.index(last_forge_version))
        except:
            pass
        #
        try:
            if last_fabric_version != '':
                self.version_select_fabric.setCurrentIndex(self.fabric_list_clear.index(last_fabric_version))
            else:
                self.version_select_fabric.setCurrentIndex(0)
        except:
            self.version_select_fabric.setCurrentIndex(0)
        #
        try:
            if last_quilt_version != '':
                self.version_select_quilt.setCurrentIndex(self.quilt_list.index(last_quilt_version))
            else:
                self.version_select_quilt.setCurrentIndex(0)
        except:
               self.version_select_quilt.setCurrentIndex(0)
        #

        self.vanila_tab.setMinimumWidth(200)
        self.tab_widget.addTab(self.vanila_tab, "Vanilla")
        self.tab_widget.addTab(self.forge_tab, "Forge")
        self.tab_widget.addTab(self.fabric_tab, "Fabric")
        self.tab_widget.addTab(self.quilt_tab, "Quilt")
        self.tab_widget.setCurrentIndex(last_mod_loader)
        self.tab_widget.setStyleSheet(f"""
            QTabBar::tab:selected {{
                font-family : {self.sub_font_family};
                font-size : 18px;
            }}
        """)

        self.tab_widget.setFont(self.main_font)

        self.progress_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.start_progress_label = QLabel(self.centralwidget)
        self.start_progress_label.setText('')
        self.start_progress_label.setVisible(False)

        self.start_progress = QProgressBar(self.centralwidget)
        self.start_progress.setProperty('value', 24)
        self.start_progress.setVisible(False)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setFont(self.sub_font)
        self.start_button.setText('Play')
        self.start_button.clicked.connect(self.launch_game)

        self.vertical_layout = QVBoxLayout(self.centralwidget)
        self.vertical_layout.setContentsMargins(15, 15, 15, 15)
        self.vertical_layout.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignHCenter)
        self.vertical_layout.addItem(self.titlespacer)
        self.vertical_layout.addWidget(self.username)
        self.vertical_layout.addItem(self.progress_spacer)
        self.vertical_layout.addWidget(self.start_progress_label)
        self.vertical_layout.addWidget(self.start_progress)
        self.vertical_layout.addWidget(self.start_button)
        self.vertical_layout.addWidget(self.tab_widget)

        self.launch_thread = LaunchThread()
        self.launch_thread.state_update_signal.connect(self.state_update)
        self.launch_thread.progress_update_signal.connect(self.update_progress)

        self.setCentralWidget(self.centralwidget)

    def state_update(self, value):
        self.start_button.setDisabled(value)
        self.start_progress_label.setVisible(value)
        self.start_progress.setVisible(value)

    def update_progress(self, progress, max_progress, label):
        self.start_progress.setValue(progress)
        self.start_progress.setMaximum(max_progress)
        self.start_progress_label.setText(label)

    def show_snapshots_pre_versions(self):
        current_index = self.tab_widget.currentIndex()
        if current_index == 0:
            self.version_select_vanilla.clear()
            if self.show_snapshots_checkbox_vanila.isChecked():
                for ver in self.vanila_list:
                    self.version_select_vanilla.addItem(ver)
            else:
                for ver in self.vanila_clear_list:
                    self.version_select_vanilla.addItem(ver)
        elif current_index == 1:
            self.version_select_forge.clear()
            if self.show_snapshots_checkbox_forge_.isChecked():
                for ver in self.forge_list_clear_cut:
                    self.version_select_forge.addItem(ver)
            else:
                for ver in self.forge_list_clear:
                    self.version_select_forge.addItem(ver)

            if self.show_snapshots_checkbox_forge.isChecked():
                self.version_select_forge.clear()
                self.show_snapshots_checkbox_forge_.setDisabled(True)
                for ver in self.forge_list:
                    self.version_select_forge.addItem(ver)
            else:
                self.show_snapshots_checkbox_forge_.setDisabled(False)
                self.version_select_forge.clear()
                if self.show_snapshots_checkbox_forge_.isChecked():
                    for ver in self.forge_list_clear_cut:
                        self.version_select_forge.addItem(ver)
                else:
                    for ver in self.forge_list_clear:
                        self.version_select_forge.addItem(ver)
        elif current_index == 2:
            self.version_select_fabric.clear()
            if self.show_snapshots_checkbox_fabric.isChecked():
                for ver in self.fabric_list:
                    self.version_select_fabric.addItem(ver)
            else:
                for ver in self.fabric_list_clear:
                    self.version_select_fabric.addItem(ver)
        elif current_index == 3:
            self.version_select_quilt.clear()
            if self.show_snapshots_checkbox_quilt.isChecked():
                for ver in self.quilt_list:
                    self.version_select_quilt.addItem(ver)
            else:
                for ver in self.quilt_clear_list:
                    self.version_select_quilt.addItem(ver)
        _process.Process.save(_process.Process(), ':',
                              show_sp_vanila=self.show_snapshots_checkbox_vanila.isChecked(),
                              show_sp_fabric=self.show_snapshots_checkbox_fabric.isChecked(),
                              show_sp_quilt=self.show_snapshots_checkbox_quilt.isChecked(),
                              show_cutted_forge=self.show_snapshots_checkbox_forge_.isChecked(),
                              show_all_forge=self.show_snapshots_checkbox_forge.isChecked())

    def launch_game(self):
        current_index = self.tab_widget.currentIndex()
        if current_index == 0:
            version = self.version_select_vanilla.currentText()
            self.launch_thread.modLoader = 1
        elif current_index == 1:
            current_version = self.version_select_forge.currentText()
            version = current_version
            for versions in self.vanila_list:
                if current_version == versions:
                    version = find_forge_version(current_version)
                    break
            self.launch_thread.modLoader = 2
        elif current_index == 2:
            version = self.version_select_fabric.currentText()
            self.launch_thread.modLoader = 3
        elif current_index == 3:
            version = self.version_select_quilt.currentText()
            self.launch_thread.modLoader = 4
        self.launch_thread.launch_setup_signal.emit(version, self.username.text())
        self.launch_thread.start()


if __name__ == '__main__':
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)

    app = QApplication(argv)
    window = MainWindow()
    window.show()

    exit(app.exec_())
