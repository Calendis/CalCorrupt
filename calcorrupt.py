# A file corruptor
# Intended for use with video game ROMs, but can be used for anything
# Start date: 8th April, 2018
from lib import uitext

from random import randint
from math import log

import tkinter as tk
from tkinter import filedialog

base_widget = tk.Tk()
base_widget.geometry("675x500")
window_width = 675
window_height = 500

number_of_columns = 3
for i in range(number_of_columns):
	base_widget.columnconfigure(i, minsize=window_width/number_of_columns)

logo = tk.PhotoImage(file="resources/cal.png")

opened_file_path = ""
opened_file = "No file opened."

def open_file():
	global opened_file_path
	opened_file_path = filedialog.askopenfilename(title=uitext.OPEN_DIALOGUE)
	opened_file = "File opened: "+opened_file_path.split("/")[-1]
	opened_file_label = tk.Label(base_widget, text=opened_file)
	opened_file_label.grid(column=0, row=0)

def corrupt_file():
	n = int(corrupt_every_n_entry.get())
	start_byte = int(start_byte_entry.get())
	end_byte = end_byte_entry.get()
	if end_byte != "":
		end_byte = int(end_byte)
	corruption_chance = float(corruption_chance_entry.get())
	if corrupt_value_entry.get() != "":
		corruption_value = int(corrupt_value_entry.get())

	print("Corrupting every "+corrupt_every_n_entry.get()+" bytes.")
	print("Starting at "+start_byte_entry.get()+" and ending at "+end_byte_entry.get()+".")
	print("Chance of corruption: "+corruption_chance_entry.get()+".")
	print("Corruption value: "+corrupt_value_entry.get()+".")

	print(opened_file_path)
	file = open(opened_file_path, "r+b")
	byte_data = bytearray(file.read())

	if end_byte == "":
		print("No end byte. Going all the way.")
		end_byte = len(byte_data)-1

	print("Corrupting file!")
	for b in range(start_byte, end_byte+1):
		if not b % n:
			if randint(1, 10000)/100 <= corruption_chance:
				if radio_v.get() == 0:
					#Increment
					byte_data[b] = (byte_data[b] + corruption_value)%255

				elif radio_v.get() == 1:
					#Shift right/left
					if corruption_value >= 0:
						byte_data[b] = byte_data[b] >> corruption_value
					else:
						byte_data[b] = (byte_data[b] << -corruption_value)%255

				elif radio_v.get() == 2:
					#Multiply
					byte_data[b] = (byte_data[b]*corruption_value)%255

				elif radio_v.get() == 3:
					#Power
					byte_data[b] = (byte_data[b]**corruption_value)%255

				elif radio_v.get() == 4:
					#Exponent
					byte_data[b] = (corruption_value**byte_data[b])%255

				elif radio_v.get() == 5:
					#Log
					byte_data[b] = round(log(byte_data[b]+1, corruption_value)%255)

				elif radio_v.get() == 6:
					#Invert
					byte_data[b] = 255-byte_data[b]

				elif radio_v.get() == 7:
					#Randomize
					byte_data[b] = randint(0,255)

				else:
					print("ERROR: Invalid corruption option.")
	
	print("Writing file...")
	file.seek(0)
	file.write(byte_data)
	file.close()
	print("All done.")
	



#Sets up the menu
menu_bar = tk.Menu(base_widget)
base_widget.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Quit", command=base_widget.quit)
help_menu = tk.Menu(menu_bar)
help_menu.add_command(label="Help")
help_menu.add_command(label="About")
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

'''The following is responsible for creating all of the widgets.'''
logo_label = tk.Label(base_widget, image=logo, relief="raised")
hello_label = tk.Label(base_widget, text=uitext.HEADER, bg="black", fg="lime")
file_corrupted_label = tk.Label(base_widget, text=uitext.FILE_NOT_CORRUPTED)
opened_file_label = tk.Label(base_widget, text=opened_file)
corruption_settings_label = tk.Label(base_widget, text=uitext.CORRUPTION_SETTINGS, bg="black", fg="cyan")
file_info_label = tk.Label(base_widget, text=uitext.FILE_INFO)

corrupt_every_n_label = tk.Label(base_widget, text=uitext.CORRUPT_EVERY_N)
corrupt_every_n_entry = tk.Entry(base_widget, width=5, bg="white")

start_byte_label = tk.Label(base_widget, text=uitext.START_BYTE)
start_byte_entry = tk.Entry(base_widget, width=5, bg="white")

end_byte_label = tk.Label(base_widget, text=uitext.END_BYTE)
end_byte_entry = tk.Entry(base_widget, width=5, bg="white")

corruption_chance_label = tk.Label(base_widget, text=uitext.CORRUPTION_CHANCE)
corruption_chance_entry = tk.Entry(base_widget, width=5, bg="white")

corruption_options = [
	("Increment", 1),
	("Shift right", 2),
	("Multiply by", 3),
	("Power", 4),
	("Exponent", 5),
	("Log, base", 6),
	("Invert", 7),
	("Randomize value", 8)
]

radiobuttons = []
radiobutton_labels = []
radio_v = tk.IntVar()
for i, v in enumerate(corruption_options):
	radiobuttons.append(tk.Radiobutton(base_widget, variable=radio_v, value=i))
	radiobutton_labels.append(tk.Label(base_widget, text=v[0]))

corrupt_button =tk.Button(base_widget, text=uitext.CORRUPT_TEXT, command=corrupt_file)
corrupt_value_entry = tk.Entry(base_widget, width=5, bg="white")

#These add the defined widgets onto the master widget.
logo_label.grid(column=2, row=0, sticky=tk.E, padx=10, pady=10)
hello_label.grid(column=0, row=0, sticky=tk.N)
opened_file_label.grid(column=0, row=0)
file_corrupted_label.grid(column=0, row=0, sticky=tk.S)
corruption_settings_label.grid(column=1, row=0, sticky=tk.N)
file_info_label.grid(column=0, row=1, pady=32)

corrupt_every_n_label.grid(column=1, row=0)
corrupt_every_n_entry.grid(column=1, row=0, sticky=tk.E)

start_byte_label.grid(column=1, row=0, sticky=tk.S)
start_byte_entry.grid(column=1, row=0, sticky=tk.SE)

end_byte_label.grid(column=1, row=1, sticky=tk.N)
end_byte_entry.grid(column=1, row=1, sticky=tk.NE)

corruption_chance_label.grid(column=1, row=1)
corruption_chance_entry.grid(column=1, row=1, sticky=tk.E)

i = 2
for radiobutton in radiobuttons:
	radiobutton.grid(column=1, row=i)
	i += 1

i = 2
for radiobutton_label in radiobutton_labels:
	radiobutton_label.grid(column=1, row=i, sticky=tk.E)
	i += 1

corrupt_button.grid(column=1, row=10, sticky=tk.SE, pady=16)
corrupt_value_entry.grid(column=2, row=6, sticky=tk.W, padx=24)

base_widget.mainloop()