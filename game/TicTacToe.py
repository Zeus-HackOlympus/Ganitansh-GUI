import PySimpleGUI as gui

NewTheme = {'BACKGROUND': '#709053',
                'TEXT': '#fff4c9',
                'INPUT': '#c7e78b',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#c7e78b',
                'BUTTON': ('white', '#709053'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

gui.theme_add_new('Custom Theme',NewTheme)
gui.theme('Custom Theme')


class BOARD:
    def __init__(self):

        bargs = {"pad" : (1,0),"size" : (16,8),"background_color":"dark blue","relief":"raised"}
        self.pos = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.verified = False
        self.layout = [
            [gui.T("Maths Tic Tac Toe",(20,2),font=("LibreBaskerville",22,"italic"),justification="center",auto_size_text=True)],
            [gui.T(" "*4+"0"),gui.T("",**bargs,key="(0,0)"),gui.T("",**bargs,key="(0,1)"),gui.T("",**bargs,key="(0,2)")],
            [gui.T(" "*4+"1"),gui.T("",**bargs,key="(1,0)"), gui.T("",**bargs,key="(1,1)"), gui.T("",**bargs,key="(1,2)")],
            [gui.T(" "*4+"2"),gui.T("",**bargs,key="(2,0)"), gui.T("",**bargs,key="(2,1)"), gui.T("",**bargs,key="(2,2)")],
            [gui.T()],
            [gui.T("Type Number:"),gui.I("")],
            [gui.T("X axis block: "),gui.I("")],
            [gui.T("Y axis block: "),gui.I("")],
            [gui.OK()]
        ]
        self.winner = False

        self.window = gui.Window("Tic Tac Toe",self.layout,resizable=True)

    def get_values(self):
        try :
            self.num = int(value[0])
            self.x = int(value[1])
            self.y = int(value[2])
        except:
            pass
    def check_values(self):

        if hasattr(self,"num"):
            if self.num < 0 or self.num > 9 :
                gui.PopupOK("number should be between 0-9")
        else: gui.PopupOK("Please enter value for number")

        if hasattr(self,"x"):
                if self.x > 2 or self.x < 0 :
                    gui.PopupOK("X axis block number should be between 0-2")
        else: gui.PopupOK("Please enter value for X axis block")

        if hasattr(self, "y"):
            if self.y > 2 or self.y < 0:
                gui.PopupOK("Y axis block number should be between 0-2")
        else:
            gui.PopupOK("Please enter value for Y axis block")

        if hasattr(self,"x") and hasattr(self,"y") :
            if self.x == 1 and self.y == 1 :
                if self.num == 5 :
                    gui.popup("Starting number at the middle can't be 5")

    def update(self):
        if (self.x == 0 and self.y == 0):
            self.window['(0,0)'].update(self.num)
            self.pos[0][0] = self.num
        elif (self.x == 0 and self.y == 1):
            self.window['(0,1)'].update(self.num)
            self.pos[0][1] = self.num
        elif (self.x == 0 and self.y == 2):
            self.window['(0,2)'].update(self.num)
            self.pos[0][2] = self.num
        elif (self.x == 1 and self.y == 0):
            self.window['(1,0)'].update(self.num)
            self.pos[0][3] = self.num
        elif (self.x == 1 and self.y == 1):
            self.window['(1,1)'].update(self.num)
            self.pos[1][1] = self.num
        elif (self.x == 1 and self.y == 2):
            self.window['(1,2)'].update(self.num)
            self.pos[1][2] = self.num
        elif (self.x == 2 and self.y == 0):
            self.window['(2,0)'].update(self.num)
            self.pos[2][0] = self.num
        elif (self.x == 2 and self.y == 1):
            self.window['(2,1)'].update(self.num)
            self.pos[2][1] = self.num
        elif (self.x == 2 and self.y == 2):
            self.window['(2,2)'].update(self.num)
            self.pos[2][2] = self.num

    def check_winner(self):
        # check vertical
        for i in range(0,3):
            if self.pos[i][0] + self.pos[i][1] + self.pos[i][2] == 15 :
                self.winner = True
        # check horizontal
        for i in range(0,3) :
            if self.pos[i][i] + self.pos[i][i+1]  + self.pos[i][i+2] == 15 :
                self.winner = True

        # check diagonal
        if self.pos[0][0] + self.pos[1][1] + self.pos[2][2] == 15 :
            self.winner = True

        elif self.pos[0][2] + self.pos[1][1] + self.pos[2][0] == 15 :
            self.winner = True



    # def check if valid x and y input or not
def main():
    board = BOARD()

    while True:
        event, value = board.window.read()
        print(event, value)
        board.get_values()
        board.check_values()
        board.update()
        if (board.verified):
            board.check_values()
        if (board.winner): gui.popup("Player wins")
        if event in (gui.WIN_CLOSED, gui.WIN_CLOSED, "Exit"):
            break

    board.window.close()
if __name__ == '__main__':
    main()