import PySimpleGUI as gui

NewTheme = {'BACKGROUND': "#26867d",
            'TEXT': '#ffffff',
            'INPUT': '#c7e78b',
            'TEXT_INPUT': '#000000',
            'SCROLL': '#c7e78b',
            'BUTTON': ('white', '#709053'),
            'PROGRESS': ('#01826B', '#D0D0D0'),
            'BORDER': 1,
            'SLIDER_DEPTH': 0,
            'PROGRESS_DEPTH': 0}

gui.theme_add_new('Custom Theme', NewTheme)
gui.theme('Custom Theme')

player1_img = {"0": "../assets/images/0_1.png",
               "1": "../assets/images/1_1.png",
               "2": "../assets/images/2_1.png",
               "3": "../assets/images/3_1.png",
               "4": "../assets/images/4_1.png",
               "5": "../assets/images/5_1.png",
               "6": "../assets/images/6_1.png",
               "7": "../assets/images/7_1.png",
               "8": "../assets/images/8_1.png",
               "9": "../assets/images/9_1.png"}
player2_img = {"0": "../assets/images/0_2.png",
               "1": "../assets/images/1_2.png",
               "2": "../assets/images/2_2.png",
               "3": "../assets/images/3_2.png",
               "4": "../assets/images/4_2.png",
               "5": "../assets/images/5_2.png",
               "6": "../assets/images/6_2.png",
               "7": "../assets/images/7_2.png",
               "8": "../assets/images/8_2.png",
               "9": "../assets/images/9_2.png"}
default_block = '../assets/images/default_block.png'

pos = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

layout = [
    [gui.T("Maths Tic Tac Toe", (20, 2), font=("LibreBaskerville", 22, "italic"), justification="center",
           auto_size_text=True)],
    [gui.T("0"), gui.Image(default_block, key="(0,0)"), gui.Image(default_block, key="(0,1)"),
     gui.Image(default_block, key="(0,2)")],
    [gui.T("1"), gui.Image(default_block, key="(1,0)"), gui.Image(default_block, key="(1,1)"),
     gui.Image(default_block, key="(1,2)")],
    [gui.T("2"), gui.Image(default_block, key="(2,0)"), gui.Image(default_block, key="(2,1)"),
     gui.Image(default_block, key="(2,2)")],
    [gui.T()],
    [gui.T("Type Number:"), gui.I("")],
    [gui.T("X axis block: "), gui.I("")],
    [gui.T("Y axis block: "), gui.I("")],
    [gui.OK(), gui.B("go back")]
]

window = gui.Window("Tic Tac Toe", layout, size=(320, 480))
winner = False
tie = True
turn = 1


def check_winner():
    global winner, pos
    first_1 = 0 if pos[0][0] is None else pos[0][0]
    second_1 = 0 if pos[0][1] is None else pos[0][1]
    third_1 = 0 if pos[0][2] is None else pos[0][2]
    if first_1 + second_1 + third_1 == 15:
        winner = True

    first_1 = 0 if pos[1][0] is None else pos[1][0]
    second_1 = 0 if pos[1][1] is None else pos[1][1]
    third_1 = 0 if pos[1][2] is None else pos[1][2]
    if first_1 + second_1 + third_1 == 15:
        winner = True
    first_1 = 0 if pos[2][0] is None else pos[2][0]
    second_1 = 0 if pos[2][1] is None else pos[2][1]
    third_1 = 0 if pos[2][2] is None else pos[2][2]
    if first_1 + second_1 + third_1 == 15:
        winner = True
    first_2 = 0 if pos[0][0] is None else pos[0][0]
    second_2 = 0 if pos[1][0] is None else pos[1][0]
    third_2 = 0 if pos[2][0] is None else pos[2][0]
    if first_2 + second_2 + third_2 == 15:
        winner = True
    first_2 = 0 if pos[0][1] is None else pos[0][1]
    second_2 = 0 if pos[1][1] is None else pos[1][1]
    third_2 = 0 if pos[2][1] is None else pos[2][1]
    if first_2 + second_2 + third_2 == 15:
        winner = True
    first_2 = 0 if pos[0][2] is None else pos[0][2]
    second_2 = 0 if pos[1][2] is None else pos[1][2]
    third_2 = 0 if pos[2][2] is None else pos[2][2]
    if first_2 + second_2 + third_2 == 15:
        winner = True

    first_3 = 0 if pos[0][0] is None else pos[0][0]
    second_3 = 0 if pos[1][1] is None else pos[1][1]
    third_3 = 0 if pos[1][2] is None else pos[2][2]
    if first_3 + second_3 + third_3 == 15:
        winner = True
    first_4 = 0 if pos[0][2] is None else pos[0][2]
    second_4 = 0 if pos[1][1] is None else pos[1][1]
    third_4 = 0 if pos[2][0] is None else pos[2][0]
    if first_4 + second_4 + third_4 == 15:
        winner = True


def check_tie():
    global tie
    for i in range(0, 2):
        for j in range(0, 2):
            if pos[i][j] is None:
                tie = False

    # def check if valid x and y input or not


while True:
    event, value = window.read()
    print(event, value, "\n", pos,turn,winner)
    if event in (gui.WIN_CLOSED, gui.WIN_CLOSE_ATTEMPTED_EVENT, "Exit"):
        break
    elif event == "OK":
        num = value[0]
        row = value[1]
        col = value[2]
        if (row == '1' and col == '1'  )and (int(num) == 5) and turn == 1: 
            gui.popup_ok("Cant start with 5 in middle")
        elif turn % 2 != 0:
            window["(" + row + "," + col + ")"].update(player1_img[num])
            pos[int(row)][int(col)] = int(num)
            turn += 1
        elif turn % 2 == 0:
            window["(" + row + "," + col + ")"].update(player2_img[num])
            pos[int(row)][int(col)] = int(num)
            turn += 1

    check_tie()
    check_winner()
    if winner:
        gui.PopupOK("Player {} wins".format((turn - 1) % 2))
    if tie:
        gui.PopupOK("Game ties")

window.close()
if __name__ == '__main__':
    main()
