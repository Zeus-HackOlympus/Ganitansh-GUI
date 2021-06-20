#! /usr/bin/env python3 



# import winsound



module = Module_template("dd")


class Module_template:
    def __init__(self, mode):
        gui.theme("black")
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
             gui.T(self.ques, size=(50, 2), font=("SanFrancisco", 18, "bold"), key="ques")],
            [gui.B("Play", font=("SanFrancisco", 12, "bold")), gui.B("Pause", font=("SanFrancisco", 12, "bold")),
             gui.Input("Enter Answer here: ", key="ans", font=("SanFrancisco", 12, "bold")),
             gui.Button("Enter", font=("SanFrancisco", 12, "bold"))],
            [gui.T("", font=("SanFrancisco", 8), text_color="red", key="wrong", justification="c", size=(25, 1))]
        ]
        self.window = gui.Window("Ganitansh-GUI", self.layout, element_justification='center', finalize=True,
                                 resizable=True)

    def get_two_random_number(self, low_limit, high_limit):
        a = random.randint(low_limit, high_limit)
        b = random.randint(low_limit, high_limit)
        return a, b

    def get_ques(self):
        if self.mode == "dd":
            a, b = self.get_two_random_number(0, 10)
            ques_format_list = [
                "There are {} toy shops in the market, each shop has {} balls. How many balls in total are present in the market ?",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product of {} and {}"
                ]
            self.ques = random.choice(ques_format_list).format(a, b)
            self.ans = a * b
        elif self.mode == "add":
            # a should always be bigger
            a, b = self.get_two_random_number(2, 99)
            while a < b:
                a, b = self.get_two_random_number(2, 99)

            ques_format_list = [
                "In the First battle of Panipat, Babur used a war tactic called as \"Tulughma\", Tulughma meant dividing the whole army into various units, viz. the Left, the Right and the Centre. Babur has a total of {} thousand men how many men does he need in each position according to tulughma",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product of {} and {}"
                ]
            self.ques = random.choice(ques_format_list).format(a, b)
            self.ans = a / b
        elif self.mode == "div":
            # a should always be bigger
            a, b = self.get_two_random_number(2, 99)
            while a < b:
                a, b = self.get_two_random_number(2, 99)

            ques_format_list = [
                "In the First battle of Panipat, Babur used a war tactic called as \"Tulughma\", Tulughma meant dividing the whole army into various units, viz. the Left, the Right and the Centre. Babur has a total of {} thousand men how many men does he need in each position according to tulughma",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product of {} and {}"
                ]
            self.ques = random.choice(ques_format_list).format(a, b)
            self.ans = a / b
        elif self.mode == "elev":
            # a should always be bigger
            a, b = self.get_two_random_number(2, 99)
            while a < b:
                a, b = self.get_two_random_number(2, 99)

            ques_format_list = [
                "In the First battle of Panipat, Babur used a war tactic called as \"Tulughma\", Tulughma meant dividing the whole army into various units, viz. the Left, the Right and the Centre. Babur has a total of {} thousand men how many men does he need in each position according to tulughma",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product of {} and {}"
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
                "In the First battle of Panipat, Babur used a war tactic called as \"Tulughma\", Tulughma meant dividing the whole army into various units, viz. the Left, the Right and the Centre. Babur has a total of {} thousand men how many men does he need in each position according to tulughma",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product of {} and {}"
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
                "In the First battle of Panipat, Babur used a war tactic called as \"Tulughma\", Tulughma meant dividing the whole army into various units, viz. the Left, the Right and the Centre. Babur has a total of {} thousand men how many men does he need in each position according to tulughma",
                "What is the product of {} and {}",
                "Sir Newton sits under the tree every evening. Everytime atleast {} falls on his head. How many apples fall on his head if he sits for {} days",
                "Shree Aryabhatta wants your help. He forgot how to take product of two numbers. What is the product of {} and {}"
            ]
            self.ques = random.choice(ques_format_list).format(a, b)
            self.ans = a / b
            # elif self.mode == "add" :

    def generate_window(self):
        return self.window
window = module.generate_window()
window['vid'].expand(True, True)

inst = vlc.Instance()
list_player = inst.media_list_player_new()
media_list = inst.media_list_new([])
list_player.set_media_list(media_list)
player = list_player.get_media_player()

Videos = {'add':'../assets/videos/add.mp4', 'dd':'../assets/videos/dd.mp4', 'div':'../assets/videos/div.mp4',
        'elev':'../assets/videos/elev.mp4', 'multi':'../assets/videos/multi.mp4', 'sqr5':'../assets/videos/sqr5.mp4'}

while True:
    event, values = window.read()
    print(event, values)
    if event in (gui.WIN_CLOSED, gui.WIN_CLOSE_ATTEMPTED_EVENT, "Exit"):
        break

window.close()
