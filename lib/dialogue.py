#Dialogue boxes for CalCorrupt

from tkinter import messagebox
from lib import uitext
'''Distributed under the GNU GPL-3.0-or-later.'''

def show_about():
	messagebox.showinfo(uitext.ABOUT_TITLE, uitext.ABOUT_TEXT)