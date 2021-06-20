import random
# import winsound
import PySimpleGUI as gui
import vlc
from sys import platform as PLATFORM


#   _____ _
#  /__   \ |__   ___ _ __ ___   ___
#    / /\/ '_ \ / _ \ '_ ` _ \ / _ \
#   / /  | | | |  __/ | | | | |  __/
#   \/   |_| |_|\___|_| |_| |_|\___|
#


theme = {'BACKGROUND': '#23272a',
         'TEXT': '#7289da',
         'INPUT': '#393e46',
         'TEXT_INPUT': '#ffffff',
         'SCROLL': '#c7e78b',
         'BUTTON': ('#eeeeee', '#99aab5'),
         'PROGRESS': ('#01826B', '#D0D0D0'),
         'BORDER': 2,
         'SLIDER_DEPTH': 0,
         'PROGRESS_DEPTH': 0}
gui.theme_add_new("newTheme", theme)
gui.theme("newTheme")

username = ""

score = 0

about_us = """
                        About Us 
We are a group of high school ....
{0} Prabhnoor Singh Sahni  :  prabhnoor28@outlook.com       
{0} Hirnika Oberoi : hirnikaoberoi7@gmail.com
{0} Vishal Juneja : vishal_juneja@outlook.com       
Our Teacher : 
{0} Ms. Sangeeta Panchal 
""".format('\U0001F449')

class Module_template:
    def __init__(self, mode):
        #gui.theme("black")
        self.mode = mode
        args = {"size": (80, 2), "font": ("SanFracisco", 14, "bold")}
        global score
        if self.mode == "dd":
            mode = "Double Digit Multiplication practice"
        elif self.mode == "add":
            mode = "Addition and subtraction practice"
        elif self.mode == "div":
            mode = "Division practice"
        elif self.mode == "elev":
            mode = "Multiplication by 11"
        elif self.mode == "multi":
            mode = "Simple Multiplication Introduction and practice"
        elif self.mode == "sqr5":
            mode = "Square of 2 digit number ending with 5"

        self.get_ques()
        self.layout = [
            [gui.T("\t\t\t\t\t{} ".format(mode), **args, justification="c"),
             gui.T("Score : {}".format(score), size=(50, 2), font=("SanFrancisco", 14, "bold"), justification="right",
                   key="score")],
            [gui.Image('../assets/images/Explanation_video.png', size=(500, 500), key="vid"),
             gui.T("\t\t", size=(40, 2)),
             gui.T(self.ques, size=(50, 6), font=("SanFrancisco", 16, "bold"), key="ques")],
            [gui.B("Play", font=("SanFrancisco", 12, "bold")), gui.B("Pause", font=("SanFrancisco", 12, "bold")),
             gui.Input("Enter Answer here: ", key="ans", font=("SanFrancisco", 12, "bold")),
             gui.Button("Enter", font=("SanFrancisco", 12, "bold"))],
            [gui.T("", font=("SanFrancisco", 8), text_color="red", key="wrong", justification="c", size=(25, 1))]
        ]


    def get_two_random_number(self, low_limit, high_limit):
        a = random.randint(low_limit, high_limit)
        b = random.randint(low_limit, high_limit)
        return a, b

    def get_ques(self):
        if self.mode == "dd":
            a, b = self.get_two_random_number(9, 99)
            ques_format_list = ["There are {} toy shops in the market, each shop has {} balls. How many balls in total are present in the market ?",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product of {} and {} "
                ]
            self.ques = ques_format_list[random.randint(0,len(ques_format_list))]
            print(self.ques)
            self.ans = a * b
        elif self.mode == "add":
            # a should always be bigger
            a, b = self.get_two_random_number(2, 99)
            while a < b:
                a, b = self.get_two_random_number(2, 99)

            ques_format_list = [
                "In the First battle of Panipat, Babur used a war tactic called as \"Tulughma\", Tulughma meant "
                "dividing the whole army into various units, viz. the Left, the Right and the Centre. Babur has a "
                "total of {} thousand men how many men does he need in each position according to tulughma",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many "
                "apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product "
                "of {} and {} "
                ]
            self.ques = random.choice(ques_format_list).format(a, b)
            self.ans = a / b
        elif self.mode == "div":
            # a should always be bigger
            a, b = self.get_two_random_number(2, 99)
            while a < b:
                a, b = self.get_two_random_number(2, 99)

            ques_format_list = [
                "In the First battle of Panipat, Babur used a war tactic called as \"Tulughma\", Tulughma meant "
                "dividing the whole army into various units, viz. the Left, the Right and the Centre. Babur has a "
                "total of {} thousand men how many men does he need in each position according to tulughma",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many "
                "apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product "
                "of {} and {} "
                ]
            self.ques = random.choice(ques_format_list).format(a, b)
            self.ans = a / b
        elif self.mode == "elev":
            # a should always be bigger
            a, b = self.get_two_random_number(2, 99)
            while a < b:
                a, b = self.get_two_random_number(2, 99)

            ques_format_list = [
                "In the First battle of Panipat, Babur used a war tactic called as \"Tulughma\", Tulughma meant "
                "dividing the whole army into various units, viz. the Left, the Right and the Centre. Babur has a "
                "total of {} thousand men how many men does he need in each position according to tulughma",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many "
                "apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product "
                "of {} and {} "
                ]
            self.ques = random.choice(ques_format_list).format(a, b)
            self.ans = a / b
            # elif self.mode == "add" :
        elif self.mode == "multi":
            # a should always be bigger
            a, b = self.get_two_random_number(2, 99)
            while a < b:
                a, b = self.get_two_random_number(2, 99)

            ques_format_list = [
                "In the First battle of Panipat, Babur used a war tactic called as \"Tulughma\", Tulughma meant "
                "dividing the whole army into various units, viz. the Left, the Right and the Centre. Babur has a "
                "total of {} thousand men how many men does he need in each position according to tulughma",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many "
                "apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product "
                "of {} and {} "
            ]
            self.ques = random.choice(ques_format_list).format(a, b)
            self.ans = a / b
            # elif self.mode == "add" :
        elif self.mode == "sqr5":
            # a should always be bigger
            a, b = self.get_two_random_number(2, 99)
            while a < b:
                a, b = self.get_two_random_number(2, 99)

            ques_format_list = [
                "In the First battle of Panipat, Babur used a war tactic called as \"Tulughma\", Tulughma meant "
                "dividing the whole army into various units, viz. the Left, the Right and the Centre. Babur has a "
                "total of {} thousand men how many men does he need in each position according to tulughma",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many "
                "apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product "
                "of {} and {} "
            ]
            self.ques = random.choice(ques_format_list).format(a, b)
            self.ans = a / b
            # elif self.mode == "add" :

    def generate_window(self):
        self.window = gui.Window("Ganitansh-GUI", self.layout, element_justification='center', finalize=True,
                                 resizable=True,ttk_theme="black")
        return self.window



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


def vlc_setup(video):
    inst = vlc.Instance()
    list_player = inst.media_list_player_new()
    media_list = inst.media_list_new([])
    list_player.set_media_list(media_list)
    player = list_player.get_media_player()
    if PLATFORM.startswith('linux'):
        player.set_xwindow(window['vid'].Widget.winfo_id())
    else:
        player.set_hwnd(window['vid'].Widget.winfo_id())
    window['vid'].update(size=(900,500))
    media_list.add_media(video)
    list_player.play()
# class MAIN:
#     def __init__(self):
#         self.layout_starting_window = starting_window()
#         self.layout_practice_window = Practice_window()
#         self.layout_Main_menu_window = MainMenu_window()
# main = MAIN()


# ╔═╗┬  ┬┌─┐┌┐┌┌┬┐  ╦  ┌─┐┌─┐┌─┐
# ║╣ └┐┌┘├┤ │││ │   ║  │ ││ │├─┘
# ╚═╝ └┘ └─┘┘└┘ ┴   ╩═╝└─┘└─┘┴
module = ""


Videos = {'add':'../assets/videos/add.mp4', 'dd':'../assets/videos/dd.mp4', 'div':'../assets/videos/div.mp4',
        'elev':'../assets/videos/elev.mp4', 'multi':'../assets/videos/multi.mp4', 'sqr5':'../assets/videos/sqr5.mp4'}



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
        window.close()
        module = Module_template("sqr5")
        window = module.generate_window()
        gui.theme("black")
        window['vid'].expand(True, True)
        # Module_template
    elif event == "Division introduction and practice":
        window.close()
        module = Module_template("div")
        # Module_template
    elif event == "Multiplication introduction":
        window.hide()
        module = Module_template("multi")
        # Module_template
    elif event == "Double Digit Multiplication practice":
        window.hide()
        module = Module_template("dd")
        # Module_template
    elif event == "Multiplication of a 2 digit number by 11":
        window.hide()
        module = Module_template("elev")
        # Module_template
    elif event == "Addition and subtraction introduction and practice":
        window.hide()
        module = Module_template("add")
        # Module_template
    elif event == "Go Back":
        window.close()
        window = MainMenu_window()
    elif event == "Enter" :
        if isinstance(module,Module_template):
            if module.ans == values['ans']:
                module.window['wrong'].update("Correct answer",text_color="green")
            else:
                module.window['wrong'].update("Incorrect answer",text_color="red")
    elif event == "Play" :
        if isinstance(module,Module_template):
            if module.mode == "add" : vlc_setup(Videos['dd'])
            elif module.mode == "dd": vlc_setup(Videos['add'])
            elif module.mode == "div" : vlc_setup(Videos['dd'])
            elif module.mode == "elev" : vlc_setup(Videos['dd'])
            elif module.mode == "multi" : vlc_setup(Videos['dd'])
            elif module.mode == "sqr5" : vlc_setup(Videos['dd'])
    elif event == "About ...":
        gui.popup_ok(about_us)


window.close()
