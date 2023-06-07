# hello_psg.py

import PySimpleGUI as sg

layout = [
	[sg.Text("Hello from ya RIntern")],
	[sg.Button("Ok")]
]

# create the window
window = sg.Window("Demo", layout)

# create an event loop
while True:
	event, values = window.read()
	# End program if user closes window or presses OK button
	if event == "Ok" or event == sg.WIN_CLOSED:
		break

window.close()
