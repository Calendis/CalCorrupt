#Dialogue boxes for CalCorrupt

from tkinter import messagebox
from lib import uitext
'''Distributed under the GNU GPL-3.0-or-later.'''

def show_about():
	messagebox.showinfo(uitext.ABOUT_TITLE, uitext.ABOUT_TEXT)

def show_corruption_value_error():
	messagebox.showinfo(uitext.ERROR_TITLE, uitext.CORRUPTION_VALUE_ERROR_TEXT)

def show_every_n_error():
	messagebox.showinfo(uitext.ERROR_TITLE, uitext.EVERY_N_ERROR_TEXT)

def show_file_error():
	messagebox.showinfo(uitext.ERROR_TITLE, uitext.FILE_ERROR_TEXT)

def show_start_byte_error():
	messagebox.showinfo(uitext.ERROR_TITLE, uitext.START_BYTE_ERROR_TEXT)

def show_end_byte_error():
	messagebox.showinfo(uitext.ERROR_TITLE, uitext.END_BYTE_ERROR_TEXT)

def show_corruption_chance_error():
	messagebox.showinfo(uitext.ERROR_TITLE, uitext.CORRUPTION_CHANCE_ERROR_TEXT)