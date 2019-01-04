# A file corruptor, by Calendis
# Intended for use with video game ROMs, but can be used for anything
# Start date: 8th April, 2018
# Ported to Qt5 3rd January, 2019

'''Distributed under the GNU GPL-3.0-or-later.'''

from lib import uitext, about_dialogue
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from random import randint
from math import log

class Ui_MainWindow(object):
    def __init__(self):
        self.file = None
        self.error_box = QtWidgets.QErrorMessage()

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 453)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(20, 20, 181, 18))
        self.welcome_label.setObjectName("welcome_label")
        self.sub_welcome_line = QtWidgets.QFrame(self.centralwidget)
        self.sub_welcome_line.setGeometry(QtCore.QRect(20, 40, 181, 16))
        self.sub_welcome_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.sub_welcome_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sub_welcome_line.setObjectName("sub_welcome_line")
        self.file_opened_label = QtWidgets.QLabel(self.centralwidget)
        self.file_opened_label.setGeometry(QtCore.QRect(20, 60, 181, 18))
        self.file_opened_label.setObjectName("file_opened_label")
        self.file_corrupted_label = QtWidgets.QLabel(self.centralwidget)
        self.file_corrupted_label.setGeometry(QtCore.QRect(20, 80, 181, 18))
        self.file_corrupted_label.setObjectName("file_corrupted_label")
        self.file_information_label = QtWidgets.QLabel(self.centralwidget)
        self.file_information_label.setGeometry(QtCore.QRect(20, 120, 101, 18))
        self.file_information_label.setObjectName("file_information_label")
        self.sub_info_line = QtWidgets.QFrame(self.centralwidget)
        self.sub_info_line.setGeometry(QtCore.QRect(20, 140, 101, 20))
        self.sub_info_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.sub_info_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sub_info_line.setObjectName("sub_info_line")
        self.settings_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_label.setGeometry(QtCore.QRect(270, 20, 131, 18))
        self.settings_label.setObjectName("settings_label")
        self.sub_settings_line = QtWidgets.QFrame(self.centralwidget)
        self.sub_settings_line.setGeometry(QtCore.QRect(240, 40, 191, 16))
        self.sub_settings_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.sub_settings_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sub_settings_line.setObjectName("sub_settings_line")
        self.corrupt_every_label = QtWidgets.QLabel(self.centralwidget)
        self.corrupt_every_label.setGeometry(QtCore.QRect(240, 60, 91, 18))
        self.corrupt_every_label.setObjectName("corrupt_every_label")
        self.thbyte_input = QtWidgets.QSpinBox(self.centralwidget)
        self.thbyte_input.setGeometry(QtCore.QRect(330, 60, 44, 24))
        self.thbyte_input.setMaximum(999999999)
        self.thbyte_input.setObjectName("thbyte_input")
        self.th_label = QtWidgets.QLabel(self.centralwidget)
        self.th_label.setGeometry(QtCore.QRect(380, 60, 58, 18))
        self.th_label.setObjectName("th_label")
        self.start_byte_label = QtWidgets.QLabel(self.centralwidget)
        self.start_byte_label.setGeometry(QtCore.QRect(240, 90, 71, 18))
        self.start_byte_label.setObjectName("start_byte_label")
        self.start_input = QtWidgets.QSpinBox(self.centralwidget)
        self.start_input.setGeometry(QtCore.QRect(330, 90, 44, 24))
        self.start_input.setMaximum(999999999)
        self.start_input.setObjectName("start_input")
        self.end_byte_label = QtWidgets.QLabel(self.centralwidget)
        self.end_byte_label.setGeometry(QtCore.QRect(240, 120, 58, 18))
        self.end_byte_label.setObjectName("end_byte_label")
        self.end_input = QtWidgets.QSpinBox(self.centralwidget)
        self.end_input.setGeometry(QtCore.QRect(330, 120, 44, 24))
        self.end_input.setMinimum(-1)
        self.end_input.setMaximum(999999999)
        self.end_input.setValue(-1)
        self.end_input.setObjectName("end_input")
        self.optional_label = QtWidgets.QLabel(self.centralwidget)
        self.optional_label.setGeometry(QtCore.QRect(380, 120, 61, 18))
        self.optional_label.setObjectName("optional_label")
        self.chance_label = QtWidgets.QLabel(self.centralwidget)
        self.chance_label.setGeometry(QtCore.QRect(240, 150, 58, 18))
        self.chance_label.setObjectName("chance_label")
        self.chance_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.chance_input.setGeometry(QtCore.QRect(330, 150, 61, 24))
        self.chance_input.setMaximum(100.0)
        self.chance_input.setObjectName("chance_input")
        self.percent_label = QtWidgets.QLabel(self.centralwidget)
        self.percent_label.setGeometry(QtCore.QRect(400, 150, 16, 21))
        self.percent_label.setObjectName("percent_label")
        self.corruption_stack_box = QtWidgets.QCheckBox(self.centralwidget)
        self.corruption_stack_box.setGeometry(QtCore.QRect(240, 250, 141, 23))
        self.corruption_stack_box.setObjectName("corruption_stack_box")
        self.min_fuzz_label = QtWidgets.QLabel(self.centralwidget)
        self.min_fuzz_label.setGeometry(QtCore.QRect(240, 180, 91, 18))
        self.min_fuzz_label.setObjectName("min_fuzz_label")
        self.min_fuzz_input = QtWidgets.QSpinBox(self.centralwidget)
        self.min_fuzz_input.setGeometry(QtCore.QRect(330, 180, 44, 24))
        self.min_fuzz_input.setMinimum(-256)
        self.min_fuzz_input.setMaximum(256)
        self.min_fuzz_input.setObjectName("min_fuzz_input")
        self.maz_fuzz_label = QtWidgets.QLabel(self.centralwidget)
        self.maz_fuzz_label.setGeometry(QtCore.QRect(240, 210, 61, 18))
        self.maz_fuzz_label.setObjectName("maz_fuzz_label")
        self.max_fuzz_input = QtWidgets.QSpinBox(self.centralwidget)
        self.max_fuzz_input.setGeometry(QtCore.QRect(330, 210, 44, 24))
        self.max_fuzz_input.setMinimum(-256)
        self.max_fuzz_input.setMaximum(256)
        self.max_fuzz_input.setObjectName("max_fuzz_input")
        self.options_label = QtWidgets.QLabel(self.centralwidget)
        self.options_label.setGeometry(QtCore.QRect(470, 20, 121, 18))
        self.options_label.setObjectName("options_label")
        self.sub_options_line = QtWidgets.QFrame(self.centralwidget)
        self.sub_options_line.setGeometry(QtCore.QRect(470, 40, 141, 16))
        self.sub_options_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.sub_options_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sub_options_line.setObjectName("sub_options_line")
        self.increment_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.increment_radio.setGeometry(QtCore.QRect(470, 60, 141, 16))
        self.increment_radio.setAutoFillBackground(False)
        self.increment_radio.setChecked(True)
        self.increment_radio.setObjectName("increment_radio")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.increment_radio)
        self.multiply_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.multiply_radio.setGeometry(QtCore.QRect(470, 80, 141, 16))
        self.multiply_radio.setObjectName("multiply_radio")
        self.buttonGroup.addButton(self.multiply_radio)
        self.power_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.power_radio.setGeometry(QtCore.QRect(470, 100, 141, 16))
        self.power_radio.setObjectName("power_radio")
        self.buttonGroup.addButton(self.power_radio)
        self.exponent_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.exponent_radio.setGeometry(QtCore.QRect(470, 120, 141, 16))
        self.exponent_radio.setObjectName("exponent_radio")
        self.buttonGroup.addButton(self.exponent_radio)
        self.log_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.log_radio.setGeometry(QtCore.QRect(470, 140, 141, 16))
        self.log_radio.setObjectName("log_radio")
        self.buttonGroup.addButton(self.log_radio)
        self.invert_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.invert_radio.setGeometry(QtCore.QRect(470, 160, 141, 16))
        self.invert_radio.setObjectName("invert_radio")
        self.buttonGroup.addButton(self.invert_radio)
        self.bitshift_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.bitshift_radio.setGeometry(QtCore.QRect(470, 180, 141, 16))
        self.bitshift_radio.setObjectName("bitshift_radio")
        self.buttonGroup.addButton(self.bitshift_radio)
        self.byteshift_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.byteshift_radio.setGeometry(QtCore.QRect(470, 200, 141, 16))
        self.byteshift_radio.setObjectName("byteshift_radio")
        self.buttonGroup.addButton(self.byteshift_radio)
        self.randomize_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.randomize_radio.setGeometry(QtCore.QRect(470, 220, 141, 16))
        self.randomize_radio.setObjectName("randomize_radio")
        self.buttonGroup.addButton(self.randomize_radio)
        self.value_label = QtWidgets.QLabel(self.centralwidget)
        self.value_label.setGeometry(QtCore.QRect(460, 250, 58, 21))
        self.value_label.setObjectName("value_label")
        self.value_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.value_input.setGeometry(QtCore.QRect(520, 250, 63, 24))
        self.value_input.setMinimum(-256.0)
        self.value_input.setMaximum(256.0)
        self.value_input.setObjectName("value_input")
        self.corrupt_button = QtWidgets.QPushButton(self.centralwidget)
        self.corrupt_button.setGeometry(QtCore.QRect(270, 370, 91, 28))
        self.corrupt_button.setCheckable(False)
        self.corrupt_button.setChecked(False)
        self.corrupt_button.setAutoDefault(False)
        self.corrupt_button.setDefault(False)
        self.corrupt_button.setFlat(False)
        self.corrupt_button.setObjectName("corrupt_button")
        self.file_type_label = QtWidgets.QLabel(self.centralwidget)
        self.file_type_label.setGeometry(QtCore.QRect(20, 160, 181, 18))
        self.file_type_label.setObjectName("file_type_label")
        self.file_length_label = QtWidgets.QLabel(self.centralwidget)
        self.file_length_label.setGeometry(QtCore.QRect(20, 180, 181, 18))
        self.file_length_label.setObjectName("file_length_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_action = QtWidgets.QAction(MainWindow)
        self.open_action.setObjectName("open_action")
        self.quit_action = QtWidgets.QAction(MainWindow)
        self.quit_action.setObjectName("quit_action")
        self.howto_action = QtWidgets.QAction(MainWindow)
        self.howto_action.setObjectName("howto_action")
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.menuFile.addAction(self.open_action)
        self.menuFile.addAction(self.quit_action)
        self.menuAbout.addAction(self.howto_action)
        self.menuAbout.addAction(self.about_action)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslate_ui(MainWindow)
        self.quit_action.triggered.connect(MainWindow.close)
        self.about_action.triggered.connect(self.display_about_dialogue)
        self.open_action.triggered.connect(self.open_file)
        self.corrupt_button.clicked.connect(self.corrupt_file)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", uitext.TITLE))
        self.welcome_label.setText(_translate("MainWindow", uitext.HEADER))
        self.file_opened_label.setText(_translate("MainWindow", uitext.NO_FILE_OPENED))
        self.file_corrupted_label.setText(_translate("MainWindow", uitext.FILE_NOT_CORRUPTED))
        self.file_information_label.setText(_translate("MainWindow", uitext.FILE_INFO))
        self.settings_label.setText(_translate("MainWindow", uitext.CORRUPTION_SETTINGS))
        self.corrupt_every_label.setText(_translate("MainWindow", uitext.CORRUPT_EVERY))
        self.thbyte_input.setToolTip(_translate("MainWindow", uitext.TH_TOOLTIP))
        self.th_label.setText(_translate("MainWindow", uitext.TH))
        self.start_byte_label.setText(_translate("MainWindow", uitext.START_BYTE))
        self.start_input.setToolTip(_translate("MainWindow", uitext.START_BYTE_TOOLTIP))
        self.end_byte_label.setText(_translate("MainWindow", uitext.END_BYTE))
        self.end_input.setToolTip(_translate("MainWindow", uitext.END_BYTE_TOOLTIP))
        self.optional_label.setText(_translate("MainWindow", uitext.OPTIONAL))
        self.chance_label.setText(_translate("MainWindow", uitext.CHANCE))
        self.chance_input.setToolTip(_translate("MainWindow", uitext.CHANCE_TOOLTIP))
        self.percent_label.setText(_translate("MainWindow", uitext.PERCENT))
        self.corruption_stack_box.setText(_translate("MainWindow", uitext.CORRUPTIONS_STACK))
        self.min_fuzz_label.setText(_translate("MainWindow", uitext.MIN_FUZZ))
        self.min_fuzz_input.setToolTip(_translate("MainWindow", uitext.MIN_FUZZ_TOOLTIP))
        self.maz_fuzz_label.setText(_translate("MainWindow", uitext.MAX_FUZZ))
        self.max_fuzz_input.setToolTip(_translate("MainWindow", uitext.MAX_FUZZ_TOOLTIP))
        self.options_label.setText(_translate("MainWindow", uitext.CORRUPTION_OPTIONS))
        self.increment_radio.setText(_translate("MainWindow", uitext.INCREMENT))
        self.multiply_radio.setText(_translate("MainWindow", uitext.MULTIPLY))
        self.power_radio.setText(_translate("MainWindow", uitext.POWER))
        self.exponent_radio.setText(_translate("MainWindow", uitext.EXPONENT))
        self.log_radio.setText(_translate("MainWindow", uitext.LOG))
        self.invert_radio.setText(_translate("MainWindow", uitext.INVERT))
        self.bitshift_radio.setText(_translate("MainWindow", uitext.BITSHIFT))
        self.byteshift_radio.setText(_translate("MainWindow", uitext.BYTESHIFT))
        self.randomize_radio.setText(_translate("MainWindow", uitext.RANDOMIZE))
        self.value_label.setText(_translate("MainWindow", uitext.CORRUPTION_VALUE))
        self.corrupt_button.setText(_translate("MainWindow", uitext.CORRUPT_BUTTON))
        self.file_type_label.setText(_translate("MainWindow", uitext.FILE_TYPE))
        self.file_length_label.setText(_translate("MainWindow", uitext.FILE_LENGTH))
        self.menuFile.setTitle(_translate("MainWindow", uitext.FILE_MENU))
        self.menuAbout.setTitle(_translate("MainWindow", uitext.HELP_MENU))
        self.open_action.setText(_translate("MainWindow", uitext.FILE_OPEN))
        self.open_action.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.quit_action.setText(_translate("MainWindow", uitext.FILE_QUIT))
        self.quit_action.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.howto_action.setText(_translate("MainWindow", uitext.HELP_HOWTO))
        self.about_action.setText(_translate("MainWindow", uitext.HELP_ABOUT))

    def display_about_dialogue(self):
        d = QtWidgets.QDialog()
        d.ui = about_dialogue.Ui_Dialog()
        d.ui.setupUi(d)
        d.exec()

    def open_file(self):
        ''' Reads a file into memory and sets some labels to do with the file. '''
        # Defines some strings based on the file we opened
        opened_file_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        opened_file_path_rel = "File opened: "+opened_file_path.split("/")[-1] # Relative version of the file path
        opened_file_extension = opened_file_path.split(".")[-1]
        opened_file_path_rel_shortened = opened_file_path_rel[:26] + (opened_file_path_rel[26:] and "...") # Shortened relative version

        if opened_file_extension.upper() == "PY":
            print("Please do not corrupt py files!")
            self.file_opened_label.setText(uitext.PY_FILE_ERROR)
            return

        if opened_file_path != "": # Only open and read if a file was selected
            try:
                self.file = open(opened_file_path, "r+b")
                self.file2 = open(opened_file_path, "r+b") # We need file2 so we can read the file twice
            except:
                print("There was an error opening the file.")
                self.file_opened_label.setText(uitext.READ_FILE_ERROR)
                self.error_box.showMessage(uitext.FILE_READ_ERROR)
            else:
                self.byte_data = bytearray(self.file.read())
                self.original_byte_data = bytearray(self.file2.read()) # Needs file2, as 'file' seems to be closed
                self.file_opened_label.setText(opened_file_path_rel_shortened)
                self.file_opened_label.setText(opened_file_path_rel_shortened)
                self.file_corrupted_label.setText(uitext.FILE_NOT_CORRUPTED)
                self.file_type_label.setText("Type: "+opened_file_extension)
                self.file_length_label.setText("Length: "+str(len(self.byte_data))+" bytes.")

    def corrupt_file(self):
        if self.file == None: # This indicates the user has not opened a file and no corruption can occur
             self.error_box.showMessage(uitext.NOFILE_ERROR)
             return

        if not self.corruption_stack_box.checkState():
        	print("Corruption stacking is OFF. Resetting byte data to original.")
        	self.byte_data = bytearray(self.original_byte_data)
        else:
        	print("Corruption stacking is ON. Not resetting byte data to original.")

        n = int(self.thbyte_input.cleanText())
        start_byte = int(self.start_input.cleanText())
        end_byte = int(self.end_input.cleanText())
        if end_byte == -1:
            end_byte = len(self.byte_data)-1
            # An end byte of -1 means do all bytes

        if end_byte < start_byte:
        	self.error_box.showMessage(uitext.BYTE_RANGE_ERROR)
        	return

        corruption_chance = float(self.chance_input.cleanText())
        min_fuzz = int(self.min_fuzz_input.cleanText())
        max_fuzz = int(self.max_fuzz_input.cleanText())

        if max_fuzz < min_fuzz:
        	self.error_box.showMessage(uitext.FUZZ_RANGE_ERROR)
        	return

        corruption_value = float(self.value_input.cleanText())

        print("Starting at byte "+self.start_input.cleanText()+" and ending at byte "+str(end_byte)+".")
        print("Corrupting every "+str(n)+" bytes.")

        print("Corrupting file using corruption option "+str(self.buttonGroup.checkedButton().text().split()[0].rstrip(",").replace("&", ""))+"!")

        for b in range(start_byte, end_byte+1):
            if n != 0 and not b % n:
        	    if randint(1, 10000)/100 <= corruption_chance:
        	        if self.buttonGroup.checkedId() == -2:
        	        	# Increment
        	        	self.byte_data[b] = int(self.byte_data[b] + corruption_value) % 255

        	        elif self.buttonGroup.checkedId() == -3:
        	            # Multiply
        	            self.byte_data[b] = int(self.byte_data[b] * corruption_value) % 255

        	        elif self.buttonGroup.checkedId() == -4:
        	            # Power
        	            self.byte_data[b] = int(self.byte_data[b] ** corruption_value) % 255

        	        elif self.buttonGroup.checkedId() == -5:
        	            # Exponent
        	            self.byte_data[b] = int(corruption_value ** self.byte_data[b]) % 255

        	        elif self.buttonGroup.checkedId() == -6:
        	            # Log
        	            if self.byte_data[b] != 0:
        	                self.byte_data[b] = int(self.log(byte_data[b], corruption_value)) % 255
        	            else:
        	                print("WARNING: byte "+str(b)+" was zero and a logarithm could not be applied!")

        	        elif self.buttonGroup.checkedId() == -7:
        	            # Invert
        	            self.byte_data[b] = int(corruption_value - self.byte_data[b]) % 255

        	        elif self.buttonGroup.checkedId() == -8:
        	            # Bitshift
        	            if corruption_value >= 0:
        	                self.byte_data[b] = self.byte_data[b] >> int(corruption_value)
        	            else:
        	                self.byte_data[b] = self.byte_data[b] << int(corruption_value)

        	        elif self.buttonGroup.checkedId() == -9:
        	            # Byteshift
        	            try:
        	                self.byte_data[b] = self.byte_data[b+int(corruption_value)]
        	            except e:
        	                print("WARNING in byteshift: "+str(e))

        	        elif self.buttonGroup.checkedId() == -10:
        	            # Randomize
        	            self.byte_data[b] = randint(0, 255)
        	        else:
        	        	self.error_box.showMessage(uitext.INVALID_CORRUPTION_ERROR)
        	        	return

        	        self.byte_data[b] = (self.byte_data[b] + randint(min_fuzz, max_fuzz)) % 255 # Add the fuzz setting

        print("Writing file...")
        self.file.seek(0)
        self.file.write(self.byte_data)

        print("All done.")
        self.file_corrupted_label.setText(uitext.FILE_CORRUPTED)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(window)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()