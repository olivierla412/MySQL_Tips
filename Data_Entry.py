

from operator import index
import PySimpleGUI as sg
import numpy as np
import pandas as pd
from sqlalchemy import false
from datetime import datetime
import glob

sg.theme('DarkTeal9')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
# EXCEL_FILE = ['User_Data.xlsx']
# df = pd.read_excel(EXCEL_FILE)
#files = ['response.xlsx']
Excel_files = glob.glob("Data_Entry.xlsx")
#Excel_File  = ['Data_Entry.xlsx']

for file in Excel_files:
    df = pd.read_excel(file)

layout = [
    [sg.Txt('Please fill out the following fileds:')],
    [sg.Txt('Name', size = (12,1)), sg.InputText(key='Name')],
    [sg.Txt('City', size = (12,1)), sg.InputText(key='City')],
    [sg.Txt('Time', size = (12,1)), sg.InputText(key='Time')],
    [sg.Text('Favourite Coulour', size=(12,1)),sg.Combo(['Green', 'Blue','red'], key='Favourite Colour')],
    [sg.Text('I speak', size=(12,1)),
              sg.Checkbox('German', key='German'),
              sg.Checkbox('Spanish', key='Spanish'),
              sg.Checkbox('English', key='English'),
              sg.Checkbox('French', key='French')
              ],
              
     [sg.Text('No. of children', size=(12,1)), sg.Spin([i for i in range(0, 16)],
     initial_value= 0, key='Children')],

    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Simple data entry form',layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel('Data_Entry.xlsx', index=False)
        sg.popup('Data saved!')      
window.close()
# print("Current Time =", current_time)