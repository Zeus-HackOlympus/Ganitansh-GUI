import PySimpleGUI as gui

class BOARD:
    def __init__(self):

        bargs = {"pad" : (1,0),"size" : (16,8),"background_color":"dark blue","relief":"raised"}
        self.pos = [
            [],
            [],
            []
        ]
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
        # check horizontal
        for i in range(0,2)
            for col in self.pos[i] :
                    if


    # def check if valid x and y input or not
board = BOARD()

while True :
    event,value = board.window.read()
    print(event,value)
    board.get_values()
    board.check_values()
    board.update()
    if event in (gui.WIN_CLOSED,gui.WIN_CLOSED,"Exit"):
        break


board.window.close()
