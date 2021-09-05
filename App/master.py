import os
import PySimpleGUI as sg
import logging
from Service.importer import import_csv
from Service.requester import add_into_readwise


logging.basicConfig(level=logging.INFO, filename="error.log")

sg.theme('LightBlue')
file_layout = [[sg.Text("請輸入您的ReadWise授權碼: "),
                sg.Input(key='_TOKEN_')],
                [sg.Text("請選擇從讀墨匯出的CSV文件: "),
                sg.Input(key='_OUTPUT_'),
                sg.FileBrowse(key='_IN_')],
               [sg.Button("提交"), sg.Button("退出")]]

window = sg.Window(title="Readmoo To Readwise", layout=file_layout, margins=(300, 200))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "退出":
        break
    elif event == "提交":
        window['_OUTPUT_'].Update(values['_IN_'])
        name, extension = os.path.splitext(values['_IN_'])
        print("Processing file: " + os.path.basename(name))

        if not name:
            sg.Popup("錯誤！未選擇任何CSV文件！", title='通知')
        elif extension != '.csv':
            sg.Popup("錯誤！該文件並非CSV文件！", title='通知')
        elif not values['_TOKEN_']:
            sg.Popup("錯誤！未輸入任何授權碼！", title='通知')
        else:
            try:
                return_value = import_csv(values['_IN_'])
                response = add_into_readwise(values['_TOKEN_'], return_value)

                if response == 200:
                    sg.Popup("成功在Readwise匯入: " + os.path.basename(name), title='通知')
                else:
                    sg.Popup("發生錯誤！" + response, title='通知')
            except Exception as ex:
                if response == 401:
                    sg.Popup("發生錯誤: 授權碼不正確！", title='通知')
                else:
                    sg.Popup("發生錯誤！無法將文件匯入Readwise！", title='通知')

        window['_OUTPUT_'].Update('')
        window['_TOKEN_'].Update('')
