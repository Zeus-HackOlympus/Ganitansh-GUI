import PySimpleGUI as gui
import random
# import winsound
import Module_template

#   _____ _
#  /__   \ |__   ___ _ __ ___   ___
#    / /\/ '_ \ / _ \ '_ ` _ \ / _ \
#   / /  | | | |  __/ | | | | |  __/
#   \/   |_| |_|\___|_| |_| |_|\___|
#


theme = {'BACKGROUND': '#222831',
         'TEXT': '#00adb5',
         'INPUT': '#393e46',
         'TEXT_INPUT': '#000000',
         'SCROLL': '#c7e78b',
         'BUTTON': ('#eeeeee', '#00adb5'),
         'PROGRESS': ('#01826B', '#D0D0D0'),
         'BORDER': 2,
         'SLIDER_DEPTH': 0,
         'PROGRESS_DEPTH': 0}
gui.theme_add_new("newTheme", theme)
gui.theme("newTheme")

username = ""


#             _           _
#            (_)         | |
#   __      ___ _ __   __| | _____      _____
#   \ \ /\ / / | '_ \ / _` |/ _ \ \ /\ / / __|
#    \ V  V /| | | | | (_| | (_) \ V  V /\__ \
#     \_/\_/ |_|_| |_|\__,_|\___/ \_/\_/ |___/
#
#

def starting_window():
    menu = [
        ["About Us", ["About ..."]]
    ]
    # TODO : ADD ART/LOGO IN 1ST GUI.TEXT()

    layout = [
        [gui.Menu(menu)],
        [gui.Text("")],
        [gui.Text("Hello, Please Introduce yourself: ", size=(40, 0), font=("SanFrancisco", 16, "bold"))],
        [gui.Text("Enter your name: ", size=(20, 0), font=("SanFrancisco", 16, "bold"))],
        [gui.InputText("", font=("SanFrancisco", 16), text_color="#845ec2", focus=True, border_width=2)],
        [gui.Text("", key="error", size=(24, 1), text_color="Red")],
        [gui.Button("Next"), gui.Exit()],
        [gui.Image('', key="gif")]
    ]
    window = gui.Window("Ganitansh-GUI", layout, enable_close_attempted_event=True, finalize=True)
    return window


def MainMenu_window():
    Bargs = {"size": (70, 4), "font": ('Helvetica', 12, "bold")}
    global username
    layout = [
        [gui.Text("\t Main Menu", font=("SanFrancisco", 20, "bold"), justification="center")],
        [gui.T("Welcome {}".format(username), text_color="green", font=("SanFrancisco", 13, "bold"),
               justification="c", )],
        [gui.T("\n")],
        [gui.Button("\t\t\tGames 🎮  \t\t\t", key="Games", **Bargs, pad=(2, 3))],
        [gui.T("\n")],
        [gui.Button("\t\t\tPractice 🎯\t\t\t", key="Practice", **Bargs, pad=(2, 3))],
    ]
    window = gui.Window("Ganitansh-GUI", layout, enable_close_attempted_event=True, size=(500, 450),
                        finalize=True)
    return window


def Practice_window():
    layout = [
        [gui.Text("\t\tPractice Math Menu", font=("SanFrancisco", 12, "bold"), text_color="cyan",
                  justification="center")],
        [gui.Button("Finding Square of a double digit number ending with 5", font=("SanFrancisco", 12, "bold"))],
        [gui.Button("Division introduction and practice", font=("SanFrancisco", 12, "bold"))],
        [gui.Button("Multiplication introduction", font=("SanFrancisco", 12, "bold"))],
        [gui.Button("Double Digit Multiplication practice ", font=("SanFrancisco", 12, "bold"))],
        [gui.Button("Multiplication of a 2 digit number by 11", font=("SanFrancisco", 12, "bold"))],
        [gui.Button("Addition and subtraction introduction and practice", font=("SanFrancisco", 12, "bold"))],
        [gui.Button("Go Back", font=("SanFrancisco", 12, "bold"))]
    ]
    window = gui.Window("Ganitansh-GUI", layout, finalize=True)
    return window


# class MAIN:
#     def __init__(self):
#         self.layout_starting_window = starting_window()
#         self.layout_practice_window = Practice_window()
#         self.layout_Main_menu_window = MainMenu_window()
# main = MAIN()


# ╔═╗┬  ┬┌─┐┌┐┌┌┬┐  ╦  ┌─┐┌─┐┌─┐
# ║╣ └┐┌┘├┤ │││ │   ║  │ ││ │├─┘
# ╚═╝ └┘ └─┘┘└┘ ┴   ╩═╝└─┘└─┘┴

module = Module_template("dd")

window = starting_window()
while True:
    event, values = window.read()
    print(event, values)
    if event in (gui.WIN_CLOSED, gui.WIN_CLOSE_ATTEMPTED_EVENT, "Exit"):
        break
    elif event == "Next":
        username = values[1]
        window.close()
        window = MainMenu_window()
    elif event == "Practice":
        window.close()
        window = Practice_window()
    elif event == "Finding Square of a double digit number ending with 5":
        window.hide()
        # Module_template
    elif event == "Division introduction and practice":
        window.hide()
        # Module_template
    elif event == "Multiplication introduction":
        window.hide()
        # Module_template
    elif event == "Double Digit Multiplication practice":
        window.hide()
        # Module_template
    elif event == "Multiplication of a 2 digit number by 11":
        window.hide()
        # Module_template
    elif event == "Addition and subtraction introduction and practice":
        window.hide()
        # Module_template
    elif event == "Go Back":
        window.close()
        window = MainMenu_window()

window.close()
