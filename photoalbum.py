from tkinter import *

photoList = ["GIF/jeju1.gif", "GIF/jeju2.gif","GIF/jeju3.gif","GIF/jeju4.gif","GIF/jeju5.gif","GIF/jeju6.gif","GIF/jeju7.gif","GIF/jeju8.gif","GIF/jeju9.gif","GIF/jeju10.gif","GIF/jeju11.gif","GIF/jeju12.gif","GIF/jeju13.gif","GIF/jeju14.gif"]

window=Tk()
window.geometry("700x480")
a = 0
def nextPhoto():
    a = a + 1
    photo.configure(file=photoList[a])

def previousPhoto():
    a = a - 1
    photo.configure(file=photoList[a])
    
buttonPrevious=Button(window, text="<< 이전",  command=previousPhoto)
buttonNext=Button(window, text="다음 >>", command=nextPhoto)
photo=PhotoImage(file="GIF/jeju1.gif")
labelPhoto=Label(window, image=photo)


buttonPrevious.place(x=250, y=10)
buttonNext.place(x=400, y=10)
labelPhoto.pack(pady=50)

window.mainloop()