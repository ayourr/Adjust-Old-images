from tkinter import *
from app import *
import pyperclip
##################### The app logic (functions) ###########################

topx, topy, botx, boty = 0, 0, 0, 0
rect_id = None


def get_mouse_posn(event):
    global topy, topx
    topx, topy = event.x, event.y
def update_sel_rect(event):
    global rect_id
    global topy, topx, botx, boty

    botx, boty = event.x, event.y
    c.coords(rect_id, topx, topy, botx, boty)  # Update selection rect.


def command_Browse():
    #picture3 =sample(min(boty, topy),max(boty, topy),min(botx, topx),max(botx, topx))
    global picture3
    picture3 = open_img()
    c.itemconfigure(picture2, image = picture3)

def sample_area():
    global pic4
    pic4 =sample(min(boty, topy),max(boty, topy),min(botx, topx),max(botx, topx))
    c.itemconfigure(picture2, image = pic4)
    print("done")

def copy_text () :
    text =ocr(min(boty, topy),max(boty, topy),min(botx, topx),max(botx, topx))
    pyperclip.copy(text)
    print(text)
############## The GUI Logic #######################
gui = Tk()

gui.title("Adjust Old Photos")
gui.configure(background="grey")

buttonLabel = Label(gui,text="Choose your old Photo :")
buttonLabel.place(relx=0.01,rely=0.02)

browse=Button(gui, text ='open image', width=20,command =command_Browse)
browse.place(relx=0.1,rely=0.017)

changeArea = Button(gui,text="Choose the area to change",width=20)
changeArea.place(relx=0.1,rely=0.27)

sampleArea = Button(gui,text="Choose the sample area",width=20,command = sample_area)
sampleArea.place(relx=0.1,rely=0.2)


change = Button(gui,text="Copy Text",width=20 , command =copy_text)
change.place(relx=0.1,rely=0.34)

###########################################################################

image= ImageTk.PhotoImage(im_test)
c = Canvas(gui, width=800, height=800)
c.place(relx=0.4,rely=0)
picture2=c.create_image(0,0,image=image,anchor="nw")

rect_id = c.create_rectangle(topx, topy, topx, topy,
                                  dash=(2,2), fill='', outline='black')
c.bind('<Button-1>', get_mouse_posn)
c.bind('<B1-Motion>', update_sel_rect)

gui.geometry("1500x850")
gui.mainloop()
