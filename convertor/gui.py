import PySimpleGUI as user_interface
from functionCal import calculateToMeter

entFeet = user_interface.Text("Enter feet:")
feetInput = user_interface.InputText(key="feetKey")

entInches = user_interface.Text("Enter inches:")
incheInput = user_interface.InputText(key="inchKey")

convertBtn = user_interface.Button("Convert")
output = user_interface.Text (key="answer")

layout = [[entFeet, feetInput], [entInches, incheInput], [convertBtn, output]]
windows = user_interface.Window("Convertor", layout, font=("Helvetica",16))

while True:
    event, values = windows.read()
    print(event)
    print(values)
    match event:
        case "Convert":
            feet = float(values["feetKey"])
            inches = float (values["inchKey"])

            results = calculateToMeter(feet,inches)
            print(results)
            windows['answer'].update(value=f"{results}m", text_color="white")

        case user_interface.WIN_CLOSED:
            break

windows.close()

