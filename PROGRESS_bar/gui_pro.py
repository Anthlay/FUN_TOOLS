import PySimpleGUI as sg
import time
mylist = [1,2,3,4,5,6,7,8]

progressbar = [ [sg.ProgressBar(len(mylist), orientation='h', size=(51, 10), key='progressbar')]]

outputwin = [ [sg.Output(size=(78,20))]]

layout = [ [sg.Frame('Progress',layout= progressbar)], [sg.Frame('Output', layout = outputwin)], [sg.Submit('Start'),sg.Cancel()]]

window = sg.Window('Custom Progress Meter', layout)

progress_bar = window['progressbar']
while True:

    event, values = window.read(timeout=10)

    if event == 'Cancel' or event is None:

        break

    elif event == 'Start':
        for i,item in enumerate(mylist):
            print(item)
            time.sleep(1)

progress_bar.UpdateBar(i + 1)
window.close()