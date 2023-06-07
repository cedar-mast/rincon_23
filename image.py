# image.py

import PySimpleGUI as sg
import os.path

# window layout of two columns

file_list_column = [
	[
		sg.Text("Image Folder"),
		sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
		sg.FolderBrowse(),
	],
	[
		sg.Listbox(
			values=[], enable_events=True, size=(40,20),
			key="-FILE LIST-"
		)
	],
]

# only show the name of the chosen file (for now)
image_viewer_column = [
	[sg.Text("Choose an image from the list on the left:")],
	[sg.Text(size=(40,1), key="-TOUT-")],
	[sg.Image(key="-IMAGE-")]
]

# ----- full layout -----
layout = [
	[
		sg.Column(file_list_column),
		sg.VSeparator(),
		sg.Column(image_viewer_column),
	]
]

window = sg.Window("Image Viewer", layout)

# event loop
while True:
	event, values = window.read()
	if event == "Exit" or event == sg.WIN_CLOSED:
		break
	# folder name was folled in so make a list of all files
	if event == "-FOLDER-":
		folder = values["-FOLDER-"]
		try:
			# get list of files in folder
			file_list = os.listdir(folder)
		except:
			file_list = []

		fnames = [
			f
			for f in file_list
			if  os.path.isfile(os.path.join(folder, f))
			and f.lower().endswith((".png", ".gif"))
		]
		window["-FILE LIST-"].update(fnames)
	elif event == "-FILE LIST-": # if a file was chosen from the list
		try: 
			filename = os.path.join(
				values["-FOLDER-"], values["-FILE LIST-"][0]
			)
			window["-TOUT-"].update(filename)
			window["-IMAGE-"].update(filename=filename)
		except:
			pass

window.close()

