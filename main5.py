from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.title("Denomination counter")
root.cofigure(bg="light blue")
root. geometry("650x400")

upload=Image.open("app_img.jpg")
upload=ImageTk.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root, image=image,bg='ligh blue')
label.place(x=180,y=20)
label1=Label(root,text="hey User! Welcom to Denomination Conter Application.",bg="light blue")
label1.place(relx=0.5,y=340,anchor=CENTER)

def msg():
  msgbox=messagebox.showinfo("Alert",Do you want to calculate the denomination count?)
   if msgbox=='ok':
   topwin()