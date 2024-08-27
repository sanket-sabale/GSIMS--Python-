# https://www.youtube.com/watch?v=-4AflOla39o&t=5s

__author__ = "macaw"
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

main = Tk()
main.geometry("1920x1080+0+0")
main.title("PLUTO PROJECTs")
# main.resizable(0, 0)
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def inventory():
    main.withdraw()
    os.system("python inventory.py")
    main.deiconify()


def saleBill():
    main.withdraw()
    os.system("python saleBill.py")
    main.deiconify()

canvas_widget = Canvas(main, width=800, height=500)
canvas_widget.pack(fill="both", expand=True)
canvas_widget.configure(bg='#97dbd6')

f1=("Times", 50)
f2=("Arial Black", 15)
f3=("Arial Black", 5)
label1 = Label(main)
label1.place(rely=0.100, width=1500, height=100)
label1.configure(text="Grocery Shop Inventory Management")
label1.configure(bg='#97dbd6')
label1.configure(fg='#172b52')
label1.configure(font= f1)

# label2 = Label(main)
# label2.place(relx=0.350, rely=0.230, width=900, height=50)
# label2.configure(text="Pluto technology & services pvt.ltd.")
# label2.configure(bg='#97dbd6')
# label2.configure(font="-family {Poppins} -size 20")

button1 = Button(main)
button1.place(relx=0.316, rely=0.446, width=146, height=70)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(text="INVENTORY")
button1.configure(activebackground="#d7e8f7")
button1.configure(cursor="hand2")
button1.configure(foreground="#defcff")
button1.configure(background="#172b52")
button1.configure(font=f2)
button1.configure(borderwidth="0")
button1.configure(command=inventory)

button2 = Button(main)
button2.place(relx=0.566, rely=0.446, width=146, height=70)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(text="SALE BILL")
button2.configure(activebackground="#d7e8f7")
button2.configure(cursor="hand2")
button2.configure(foreground="#defcff")
button2.configure(background="#172b52")
button2.configure(font=f2)
button2.configure(borderwidth="0")
button2.configure(command=saleBill)


label2 = Label(main)
label2.place(rely=0.7, width=1800, height=20)
label2.configure(text="-Programed by sanket----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
label2.configure(bg='#112240')
label2.configure(fg='#97dbd6')
label2.configure(anchor=W)
label2.configure(font=f3)

main.mainloop()
