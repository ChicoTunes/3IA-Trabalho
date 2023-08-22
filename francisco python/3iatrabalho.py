import PySimpleGUI as sg
sg.theme("DarkBlue")
def calcular_muv(aceleracao, velocidade_inicial, velocidade_final):
    tempo = (velocidade_final - velocidade_inicial) / aceleracao
    return tempo

layout = [
    [sg.Text("Cálculo de Cinemática Vetorial", font=("Helvetica", 16))],
    [sg.Text("MUV - Tempo para atingir uma velocidade", font=("Helvetica", 12))],
    [sg.Text("Aceleração (m/s²):"), sg.InputText(key="aceleracao")],
    [sg.Text("Velocidade Inicial (m/s):"), sg.InputText(key="velocidade_inicial")],
    [sg.Text("Velocidade Final (m/s):"), sg.InputText(key="velocidade_final")],
    [sg.Button("Calcular")],
    [sg.Text("", size=(40, 1), key="resultado_cenario1")],

    [sg.Button("Sair")]
]

window = sg.Window("Cinemática Vetorial", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    elif event == "Calcular":
        try:
            aceleracao = float(values["aceleracao"])
            velocidade_inicial = float(values["velocidade_inicial"])
            velocidade_final = float(values["velocidade_final"])
            tempo = calcular_muv(aceleracao, velocidade_inicial, velocidade_final)
            sg.popup(f"Tempo: {tempo:.2f} segundos")
        except ValueError:
            sg.popup_error("Insira valores numéricos válidos.")
        except ValueError:
            sg.popup_error("Insira os valores corretamente.")

window.close()