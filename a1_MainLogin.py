# Username = "sanket" Password = "pluto"
from tkinter import *
import os

def mylogin():
    uname = username.get()
    passw = password.get()
    if uname.strip() and passw.strip():
        if username.get() == "sanket" or password.get() == "pluto":
            root.withdraw()
            os.system("python Dashbord.py")
            root.destroy()
        else:
            meassageLabel.configure(text="")
            meassageLabel2.configure(text="Invalid Details. System is going to turn off.")
            # root.after(90000,root.destroy())
    else:
        meassageLabel2.configure(text="")
        meassageLabel.configure(text="Enter Valid Username and Password.")

root = Tk()
root.title("Login")
root.geometry("400x450+500+100")
root.resizable(0, 0)

canvas_widget = Canvas(root, width=800, height=500)
canvas_widget.pack(fill="both", expand=True)
canvas_widget.configure(bg='#e5e6d5')

f4=("Times", 16)
f1=("Times", 15)
f2=("Arial Black", 12)
f3 = ("Courier New",12)

labelusername = Label(root,text="Grocery Shop Inventory Management System")
labelusername.place(relx=0.02,rely=0.05)
labelusername.configure(font=f4)
labelusername.configure(bg='#e5e6d5')
labelusername.configure(fg="#6e5a20")

labelusername = Label(root,text="User name:")
labelusername.place(relx=0.25,rely=0.2)
labelusername.configure(font=f1)
labelusername.configure(bg='#e5e6d5')
username = Entry(root)
username.place(relx=0.25,rely=0.26)
username.configure(font=f3)
username.configure(bg="#fce89d")
username.configure(disabledforeground='black')

labelpassword = Label(root,text="Password:")
labelpassword.place(relx=0.25,rely=0.34)
labelpassword.configure(font=f1)
labelpassword.configure(bg='#e5e6d5')
password = Entry(root)
password.place(relx=0.25,rely=0.4)
password.configure(font=f3)
password.configure(show="*")
password.configure(bg="#fce89d")
password.configure(disabledforeground='black')

login = Button(root,text="Login")
login.place(relx=0.25,rely=0.6)
login.configure(command=mylogin)
login.configure(font=f2)
login.configure(width=18)
login.configure(activebackground="#ad995e")
login.configure(bg="#e0cb8d")

meassageLabel = Label(root)
meassageLabel.place(relx=0.17,rely=0.5)
meassageLabel.configure(font=f1)
meassageLabel.configure(bg='#e5e6d5')
meassageLabel.configure(fg="#8c1616")

meassageLabel2 = Label(root)
meassageLabel2.place(relx=0.05,rely=0.8)
meassageLabel2.configure(font=f1)
meassageLabel2.configure(bg='#e5e6d5')
meassageLabel2.configure(fg="#8c1616")

root.mainloop()