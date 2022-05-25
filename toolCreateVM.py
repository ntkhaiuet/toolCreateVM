import PySimpleGUI as sg
import os

layout = [  [sg.Text('Select VM configuration', font=('Arial',15, 'bold'))],
            [sg.Radio('Windows 10, 2 CPU, 4GB RAM, 32GB Disk', 1, enable_events=True, font=('Arial',13), key='-R1-')],
            [sg.Radio('Windows 10, 2 CPU, 6GB RAM, 50GB Disk',1, enable_events=True, font=('Arial',13), key='-R2-')],
            [sg.Radio('Ubuntu, 1 CPU, 2GB RAM, 16GB Disk',1, enable_events=True, font=('Arial',13), key='-R3-')],
            [sg.Radio('Ubuntu, 2 CPU, 4GB RAM, 32GB Disk',1, enable_events=True, font=('Arial',13), key='-R4-')],
            [sg.Text('Path to VMware OVF Tool:', font=('Arial', 15, 'bold'))],
            [sg.In( visible=False), sg.Input(key='-PATH-', font=('Arial', 13), default_text='C:\Program Files\VMware\VMware OVF Tool'), sg.FileBrowse('Browse', target='-DIR-', font=('Arial', 10, 'bold'))],
            [sg.Text('Datastore', font=('Arial',15, 'bold'))],
            [sg.Input(key='-DATASTORE-', font=('Arial', 13), default_text='datastore1')],
            [sg.Text('VM name', font=('Arial',15, 'bold'))],
            [sg.Input(key='-VMNAME-', font=('Arial', 13))],
            [sg.Text('ESXI hostname or IP Address', font=('Arial',15, 'bold'))],
            [sg.Input(key='-IP-', font=('Arial', 13))],
            [sg.Text('Username', font=('Arial',15, 'bold'))],
            [sg.Input(key='-USERNAME-', font=('Arial', 13), default_text='root')],
            [sg.Text('Password', font=('Arial',15, 'bold'))],
            [sg.Input('', key='-PASSWORD-', password_char='*', font=('Arial', 13))],
            [sg.Button('CREATE', font=('Arial',16))]  ]

window = sg.Window('Tool Create VM', layout, enable_close_attempted_event=True)

while True:             # Event Loop
    event, values = window.read()

    required1 = window['-VMNAME-'].get().strip()
    required2 = window['-IP-'].get().strip()
    required3 = window['-USERNAME-'].get().strip()
    required4 = window['-PASSWORD-'].get().strip()

    win10_2_4_32 = values["-R1-"]
    win10_2_6_50 = values["-R2-"]
    u1_2_16 = values["-R3-"]
    u2_4_32 = values["-R4-"]

    ovaURL = ["https://dl.dropbox.com/s/uurlzcyad172tdu/Windows10-2-4-32.ova",
        "https://dl.dropbox.com/s/2428m49v5uf1jlq/Windows10-2-6-50.ova",
        "https://dl.dropbox.com/s/129ts6r5ojvej2w/Ubuntu1-2-16.ova",
        "https://dl.dropbox.com/s/rzm8ulufajvpern/Ubuntu2-4-32.ova"]

    if (win10_2_4_32 or win10_2_6_50 or u1_2_16 or u2_4_32):
        if event == 'CREATE' and required1 and required2 and required3 and required4:
            # print(event, values)

            command = 'ovftool.exe -ds='
            pathovftool = values["-PATH-"]
            datastore = values["-DATASTORE-"]
            vmname = values["-VMNAME-"]

            command = command + datastore + ' -n=' + vmname + ' "'
            if win10_2_4_32:
                command = command + ovaURL[0] + '" vi://'
            elif win10_2_6_50:
                command = command + ovaURL[1] + '" vi://'
            elif u1_2_16:
                command = command + ovaURL[2] + '" vi://'
            else:
                command = command + ovaURL[3] + '" vi://'
            
            username = values["-USERNAME-"]
            password = values["-PASSWORD-"]
            ip = values["-IP-"]
            command = command + username + ':' + password + '@' + ip
            os.chdir(pathovftool)
            os.system(command)
            break

window.close()