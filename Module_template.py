#! /usr/bin/env python3 


import PySimpleGUI as gui 
from sys import platform as PLATFORM
import vlc
import winsound
gui.theme("black")

score = 0

def basic_level_window(ques:str):
    args = {"size" : (80, 2), "font" : ("SanFracisco", 14, "bold")}
    global score
    layout = [
                [gui.T("\t\t\t\t\t\tBasic Level Questions ",**args,justification = "c"),gui.T("Score : {}".format(score),size=(50,2),font=("SanFrancisco",14,"bold"),justification="right",key="score")],
                [gui.Image('./assets/Explanation video.png',size=(500,500),key="vid"),gui.T("\t\t",size=(40,2)),gui.T(ques,size=(50,2),font=("SanFrancisco",18,"bold"),key="ques")],
                [gui.B("Play",font=("SanFrancisco",12,"bold")),gui.B("Pause",font=("SanFrancisco",12,"bold")),gui.Input("Enter Answer here: ",key="ans",font=("SanFrancisco",12,"bold")),gui.Button("Enter",font=("SanFrancisco",12,"bold"))],
                [gui.T("",font=("SanFrancisco",8),text_color="red",key="wrong",justification="c",size=(25,1))]
            ]
    window = gui.Window("Ganitansh-GUI",layout,element_justification='center', finalize=True, resizable=True,size=(1700,1700))
    return window




questions = ["What is 79 multiplied by 45 ? ","What is 88 multiplied by 97 ?","what is 18 multiplied by 48 ? ","What is 73 multiplied by 78"]
answers = ["3555","8536","864","5694"]

index = 0 

window = basic_level_window(questions[index])
window['vid'].expand(True,True)

inst = vlc.Instance()
list_player = inst.media_list_player_new()
media_list = inst.media_list_new([])
list_player.set_media_list(media_list)
player = list_player.get_media_player()

if  PLATFORM.startswith('linux'):
	player.set_xwindow(window['vid'].Widget.winfo_id())
else:
	player.set_hwnd(window['vid'].Widget.winfo_id())

n = 1000
media_list.add_media("./assets/dd/dd.mp4")

list_player.set_media_list(media_list)

while True :
	event, values = window.read(timeout=n)       # run with a timeout so that current location can be updated
	print(event, values)
	if event == gui.WIN_CLOSED:
		break
	elif score == 4 : 
		winsound.PlaySound("./assets/Drumroll.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS )
	elif event == "Pause" :
		list_player.pause()
	elif (event == "Play"):
		list_player.play()
		n+=5
	elif (event == "Enter" ): 
		if (values['ans'] == answers[index]):
			score += 1
			winsound.PlaySound("./assets/correct.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
			window['score'].update("score: " + str(score))
			window['wrong'].update("Correct answer",text_color="green")
			window['wrong'].update('') 
			index = ( index + 1 ) % len(questions)
			window['ques'].update(questions[index])
			list_player.next() 
			list_player.pause()
		else:
			print("score = " + str(score))
			window['wrong'].update("Incorrect answer. Try again",text_color="red")

window.close()


