import PySimpleGUI as gui
import pygame
import pyttsx3

eng = pyttsx3.init()
pygame.mixer.init()


def speak(text):
    eng.say(text)
    eng.runAndWait()


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

north = ['gonorth', 'N', 'n', 'north', 'goforward']
south = ['gosouth', 'S', 's', 'south', 'goback', 'gobackward']
east = ['goeast', 'E', 'e', 'east', 'goright']
west = ['gowest', 'W', 'w', 'west', 'goleft']

# global variables for health bar
maxHealth = 100  # Max Health
healthDashes = 20  # Max Displayed dashes
inventory = "\tInventory\t"

class Scene1:
    def __init__(self):
        self.bargs = {"font": ("SanFracisco", 12, "bold")}
        self.res_args = {"text_color": "red", "font": ("SanFracisco", 9), "key": "response"}

    def first_window(self):
        layout = [
            [gui.T(), gui.Image("../assets/story/Images/Battle-of-Haldighati.png", key="img")],
            [gui.T("""In the year 1576, India was under the rule of the mughal 
emperor Jalalludin Mohammad Akhbar known as \"Akhbar\" 
but, the Rajput kings of Rajasthan were not surrendering
their power to the Mughals.

After many invasions and beneficial proposals by Akhbar,
many Rajput kings surrendered to him. He also sent 
many offers to Rana Pratap but he denied and was adamant.""", **self.bargs, key="text")],
            [gui.OK()]]

        window = gui.Window("test", layout, resizable=True, finalize=True)
        window['text'].expand(True, True)
        return window

    def secondWindow(self):
        layout = [
            [gui.Image("../assets/story/Images/Battle-of-Haldighati.png", key="img")],
            [gui.T("""On 18th June of 1576, a battle took place in Haldighati 
between Maharana Pratap of Mewar and Akhbar's led by 
Maan Singh of Amber.It was a fierce battle. 
Unfortunately,Rana Pratap lost the battle""", **self.bargs, key="text")], [gui.OK()]]
        window = gui.Window("test", layout, finalize=True, resizable=True)
        window['text'].expand(True, True)
        return window

    def thirdWindow(self):
        layout = [
            [gui.T("\t"), gui.Image("../assets/story/Images/Battle-of-Haldighati.png", key="img")],
            [gui.T("""Rana Pratap managed to escape ! To hide he has to 
reach Koriyalli (a safe place towards south western Aravalli Hills ) 
but his way goes through jungles.Now, help Rana Pratap to go through
the jungle to reach Koriyalli a hilly town from Haldighati (south 
of Mewar) safely.
 
Keep in mind some Mughal soldiers may follow you.""", **self.bargs, key="text")], [gui.OK()]]
        window = gui.Window("test", layout, finalize=True, resizable=True)
        window['text'].expand(True, True)
        return window


class Scene2_Introduction_to_game():
    def __init__(self):
        self.bargs = {"font": ("SanFracisco", 12, "bold")}
        self.reponse_args = {"text_color": "red", "font": ("SanFracisco", 9), "key": "response", "size": (50, 1)}

    def healthbar(self, health):
        dashConvert = int(maxHealth / healthDashes)
        currentDashes = int(health / dashConvert)
        remainingHealth = healthDashes - currentDashes

        healthDisplay = '█' * currentDashes
        remainingDisplay = ' ' * remainingHealth
        percent = str(int((health / maxHealth) * 100)) + "%"

        return "|" + healthDisplay + remainingDisplay + "|" + "\n" + "         " + percent

    def first_window(self):
        layout = [
            [gui.Image("../assets/story/Images/forest.png")],
            [gui.T("\t   HP: "), gui.T(self.healthbar(100), text_color="white", key="HP")],
            [gui.T("""This is a text based game.This is a text based
game that will require the use of both imagination 
and Mathematics. On answering each question correct,
you will get to know some interesting facts about 
Indian culture.""", **self.bargs)],
            [gui.OK()]
        ]
        window = gui.Window("test", layout, resizable=True, finalize=True)
        return window

    def second_window(self):
        layout = [
            [gui.Image("../assets/story/Images/forest.png")],
            [gui.T("\t\tHP: "), gui.T(self.healthbar(100), text_color="white", key="HP")],
            [gui.T("""In order to move through the game you can only
enter action commands that should include 'a verb' and
'a noun'.Such as: Go east, go west, go south, go north,
take <object>, attack <object>, open <object>, etc

In the text box below : """, **self.bargs)],
            [gui.I("Enter Commands here: "), gui.OK()]
        ]
        window = gui.Window("test", layout, resizable=True, finalize=True)
        return window

    def third_window(self):
        layout = [
            [gui.T("\t"), gui.Image("../assets/story/Images/forest.png")],
            [gui.T("\t\tHP: "), gui.T(self.healthbar(100), text_color="white", key="HP")],
            [gui.T("""The day dawned crisp and clear, you find yourself in a dense forest : 
-> Towards your north you see a path covered with leaves 
-> towards your west you see a wooden hut,
-> towards your south you see a similar path as the path towards north
-> towards east there is a cliff.

What do you do?            
""", **self.bargs)], [gui.I("Enter Commands here: ", key="command"), gui.OK()], [gui.T("", **self.reponse_args)]]
        window = gui.Window("test", layout, finalize=True, resizable=True)
        pygame.mixer.music.load("../assets/story/music/Scary_forest.ogg")
        pygame.mixer.music.play()
        return window

    def fourth_window(self):
        layout = [
            [gui.Image("../assets/story/Images/house-with-wooden-door.png")],
            [gui.T("\t\tHP: "), gui.T(self.healthbar(100), text_color="white", key="HP")],
            [gui.T("""You reach the front of the house.\nIn Front of you stands a wooden door. What do you do ?""",
                   **self.bargs)],
            [gui.Input("Enter Command here", key="command"), gui.OK()],
            [gui.T("", **self.reponse_args)]
        ]
        window = gui.Window("test", layout, resizable=True, finalize=True)
        return window

    def fifth_window(self):
        layout = [
            [gui.T("\t\t"),gui.Image("../assets/story/Images/inside_room.png")],
            [gui.T("\t\tHP: "), gui.T(self.healthbar(100), text_color="white", key="HP")],
            [gui.T("""You see a wooden table in front you. On the table lies:
- a lantern, 
- a bow and arrow and,
- a slice a bread.

On the floor you see a rugged carpet and a huge box lying in the corner of the room.
You try to open the box but its locked. The lock can only be opened with a 4 digit 
combination.Beneath the box you find a yellow weathered paper which has something 
written on it. It reads,""",**self.bargs,key="text")],
            [gui.Input("Enter Command here", key="command"), gui.OK()],
            [gui.T("", **self.reponse_args)]
        ]
        window = gui.Window("test", layout, resizable=True, finalize=True)
        return window
    def sixth_window(self):
        layout = [
            [gui.Image("../assets/story/Images/note.png")],
            [gui.T("\t\tHP: "), gui.T(self.healthbar(100), text_color="white", key="HP")],
            [gui.Input("Enter Command here", key="command"), gui.OK()],
            [gui.T("", **self.reponse_args)]
        ]
        window = gui.Window("test", layout, resizable=True, finalize=True)
        return window
    def seventh_window(self):
        layout = [
            [gui.Image("../assets/story/Images/sword_and_medicines.png")],
            [gui.T("""The box opens and you find a magnificent sword lying inside
The box also contains medicines. You take the sword  and put it around your waist.
Now you can view your inventory from inventory button and you also have earned a 
fun fact. Use the button to read it
""",**self.bargs)],
            [gui.I("Enter commands here: "),gui.OK()],
            [gui.B("Inventory"),gui.B("Fun Fact",key="fact")]
        ]
        window = gui.Window("test",layout,resizable=True,finalize=True)
        return  window
    def eighth_window(self):
        layout = [
            [gui.Image("../assets/story/Images/bow_and_arrow_etc.png")],
            [gui.T("""In front of you is the table with, 
- Bow and arrow
- Lantern 
- Slice of bread""",**self.bargs,key="text")],
            [gui.I("Enter commands here: ",key="command"),gui.OK()],
            [gui.B("Inventory"),gui.B("Fun Fact",key="fact")],
            [gui.T("",**self.reponse_args)]
        ]
        window = gui.Window("test",layout,resizable=True,finalize=True)
        return window
    def ninth_window(self):
        layout = [
            [gui.Image("../assets/story/Images/closed-trapdoor.png")],
            [gui.T("""It is written on the trapdoor, : """,**self.bargs, key="text")],
            [gui.I("Enter commands here: ", key="command"), gui.OK()],
            [gui.B("Inventory"), gui.B("Fun Fact", key="fact")],
            [gui.T("", **self.reponse_args)]
        ]
        window = gui.Window("test", layout, resizable=True, finalize=True)
        return window
    def tenth_window(self):
        layout = [
            [gui.Image("../assets/story/Images/trapdoor-ques.png")],
            [gui.I("Enter commands here: ", key="command"), gui.OK()],
            [gui.B("Inventory"), gui.B("Fun Fact", key="fact")],
            [gui.T("", **self.reponse_args)]
        ]
        window = gui.Window("test", layout, resizable=True, finalize=True)
        return window


class eventLoops:
    def __init__(self):
        self.scene1 = Scene1()
        self.scene2 = Scene2_Introduction_to_game()
        self.resume = True
        self.revive = False
        self.box_close = True
        self.note_found = False
        self.fact =    """
            Famous Mathematicians of Ancient India
Name- Baudhayana
Born- 800 BCE
Books- Sulba Sutra
Notable Contributions to maths- 
1. Value of pi was first calculated by him
2. Concepts of pythagoreas theorum
3. Ideas about finding square roots
"""
    def scene1_first(self):
        window = self.scene1.first_window()
        while True:
            event, values = window.read()
            print(event, values)
            if event in (gui.WIN_CLOSED, gui.WIN_CLOSE_ATTEMPTED_EVENT, "Exit"):
                self.resume = False
                break
            elif event == "OK":
                self.resume = True
                window.close()
                break

                # window = second_window()

    def scene2_second(self):
        window = self.scene1.secondWindow()
        while True:
            event, values = window.read()
            print(event, values)
            if event in (gui.WIN_CLOSED, gui.WIN_CLOSE_ATTEMPTED_EVENT, "Exit"):
                self.resume = False
                break
            elif event == "OK":
                self.resume = True
                window.close()
                break

    def scene3_third(self):
        window = self.scene1.thirdWindow()
        while True:
            event, values = window.read()
            print(event, values)
            if event in (gui.WIN_CLOSED, gui.WIN_CLOSE_ATTEMPTED_EVENT, "Exit"):
                self.resume = False
                break
            elif event == "OK":
                self.resume = True
                window.close()
                break

    def scene4_intro_of_game(self):
        self.revive = False
        window = self.scene2.first_window()
        while True:
            event, values = window.read()
            print(event, values)
            if event in (gui.WIN_CLOSED, gui.WIN_CLOSE_ATTEMPTED_EVENT, "Exit"):
                self.resume = False
                break
            if event == "OK":
                self.resume = True
                window.close()
                break
        window.close()

    def scene5_commands_intro(self):
        window = self.scene2.second_window()
        while True:
            event, values = window.read()
            print(event, values)
            if event in (gui.WIN_CLOSED, gui.WIN_CLOSE_ATTEMPTED_EVENT, "Exit"):
                self.resume = False
                break
            if event == "OK":
                self.resume = True
                window.close()
                break
        window.close()

    def scene_6_game_starts(self):
        window = self.scene2.third_window()
        pygame.mixer.music.load("../assets/story/music/death.ogg")
        while True:
            event, values = window.read()
            print(event, values)
            if event in (gui.WIN_CLOSED, gui.WIN_CLOSE_ATTEMPTED_EVENT, "Exit"):
                self.resume = False
                break
            elif event == "OK" and str(values['command']).replace(' ', '').lower() in east:
                self.resume = False
                window['HP'].update(self.scene2.healthbar(0))
                gui.popup("""
YOU DIED, you went over the cliff 
If you want to start again enter 'revive' 
""", text_color="red")
                pygame.mixer.music.play()

            elif event == "OK" and str(values['command']).replace(' ', '').lower() in west:
                self.resume = True
                break
            elif event == "OK" and str(values['command']).replace(' ', '').lower() in south:
                pass
            elif event == "OK" and str(values['command']).replace(' ', '').lower() in north:
                pass
            elif event == "OK" and str(values['command']).replace(' ', '').lower() == 'revive':
                window['HP'].update(self.scene2.healthbar(100))
                self.revive = True
                self.resume = False
            else:
                window['response'].update("Invalid command")
        window.close()

    def scene_7_outside_door(self):
        window = self.scene2.fourth_window()
        pygame.mixer.music.load("../assets/story/music/door.ogg")
        while True:
            event, values = window.read()
            print(event, values)
            if event in (gui.WIN_CLOSED, gui.WIN_CLOSE_ATTEMPTED_EVENT, "Exit"):
                self.resume = False
                break
            elif event == "OK" and str(values['command']).replace(' ', '').lower() == "opendoor":
                self.resume = True
                pygame.mixer.music.play()
                break
            elif event == "OK" and "go" in str(values['command']).replace(' ', '').lower():
                pass
            else:
                window['response'].update("Invalid command")
        window.close()
    def scene_8_inside_house(self):
        window = self.scene2.fifth_window()
        while True :
            event, values = window.read()
            print(event,values)
            if event in (gui.WIN_CLOSED,gui.WIN_CLOSE_ATTEMPTED_EVENT,"Exit"):
                break
            elif event == "OK" and str(values['command']).replace(' ','').lower() == "openbox":
                if self.box_close:
                    window['text'].update("""You try to open the box but its locked. The lock can only be opened with
a 4 digit combination. Beneath the box you find a yellow weathered paper
which has something written on it. It reads""")
                    self.note_found = True
            elif self.note_found :
                break
            window.close()
    def scene_9_note_in_house(self):
        window = self.scene2.sixth_window()
        while True:
            event, values = window.read()
            if event in (gui.WIN_CLOSED,gui.WIN_CLOSE_ATTEMPTED_EVENT,"Exit"):
                self.resume = False
                break
            if event == "OK" and str(values['command']).replace(' ','') == "8000" :
                global inventory
                inventory += "\nSword\nMedicines"
                print(inventory)
                self.resume = True
                break
            else :
                window['response'].update("Invalid Command or Answer")
        window.close()
    def scene_10_contents_in_box(self):
        window = self.scene2.seventh_window()
        global inventory
        while True :
            event, values = window.read()
            print(event,values)
            if event in (gui.WIN_CLOSED,gui.WIN_CLOSE_ATTEMPTED_EVENT,"Exit"):
                self.resume = False
                break
            elif event == "Inventory" :
                gui.popup_ok(inventory)
            elif event == "fact" :
                gui.popup_ok(self.fact)
            elif event == "OK" :
                self.resume = True
                break
        window.close()
    def scene_11_filling_inventory(self):
        global inventory
        window = self.scene2.eighth_window()
        pygame.mixer.music.load("../assets/story/music/death.ogg")
        self.inventory = ["Sword","Medicines"]
        while True :
            event, values = window.read()
            if event in (gui.WIN_CLOSED,gui.WIN_CLOSE_ATTEMPTED_EVENT,"Exit"):
                self.resume = False
                break
            elif event == "Inventory" :
                gui.popup_ok(inventory)
            elif event == "fact" :
                gui.popup_ok(self.fact)
            elif event == "OK" and str(values['command']).replace(' ','').lower() == "takelantern" :
                window['response'].update("Lantern added to inventory")
                if "Lantern" not in self.inventory :
                    inventory += "\nLantern"
                    self.inventory.append("Lantern")
            elif event == "OK" and str(values['command']).replace(' ','').lower() == "takebowandarrow":
                window['response'].update("Bow and arrow added to inventory")
                if "Bow and arrow" not in self.inventory:
                    inventory += "\nBow and Arrow"
                    self.inventory.append("Bow and Arrow")
            elif event == "OK" and str(values['command']).replace(' ','').lower() == "takesliceofbread":
                window['response'].update("Slice of bread added to inventory")
                if "slice of bread" not in self.inventory :
                    inventory += "\nSlice of bread"
                    self.inventory.append("slice of bread")
            elif event == "OK" and str(values['command']).replace(' ','').lower() == "pickcarpet" :
                window['response'].update("YOU DISCOVERED A HIDDEN TRAP DOOR UNDER THE CARPET")
            elif event == "OK" and str(values['command']).replace(' ','').lower() in (west,north,east):
                print("You can't go that way.")
            elif event == "OK" and str(values['command']).replace(' ','').lower() in south :
                window['response'].update("You can go back or north")
                if event == "OK" and str(values['command']).replace(' ','').lower() in north :
                    window['text'].update("The Mughal soldier has now called for reinforcements. Do you really wanna go out there? (Y/N)")
                    if event == "OK" and str(values['command']).replace(' ','').replace("es","") == "y":
                        t = """You open the door and find the Mughal soldiers in a 
triangular formation waiting for you to come out.
You see 3 arrows coming towards you and hear a 
whooshing sound.Your entire life passes by your 
eyes in a flash as you fall to the ground and die
"""
                        gui.popup_ok(t)
                        pygame.mixer.music.play()
            else :
                window['response'].update("Incorrect response",text_color="red")






event = eventLoops()
event.scene1_first()

def first_scene():
    event.scene1_first()
    if event.resume: second_scene()

def second_scene():
    event.scene2_second()
    if event.resume: third_scene()

def third_scene():
    event.scene3_third()
    if event.resume : fourth_scene()

def fourth_scene():
    event.scene4_intro_of_game()
    if event.resume : fifth_scene()

def fifth_scene():
    event.scene5_commands_intro()
    if event.resume : sixth_scene()

def sixth_scene():
    event.scene_6_game_starts()
    if event.revive : fourth_scene()
    elif event.resume : seventh_scene()

def seventh_scene():
    event.scene_7_outside_door()
    if event.resume : eighth_scene()

def eighth_scene():
    event.scene_8_inside_house()
    if event.resume : ninth_scene()

def ninth_scene():
    event.scene_9_note_in_house()
    if event.resume: tenth_scene()

def tenth_scene():
     event.scene_10_contents_in_box()
     if event.resume: eleventh_scene()

def eleventh_scene():
    event.scene_11_filling_inventory()
    # if event.resume: twelth_scene()


if __name__ == '__main__':
    first_scene()