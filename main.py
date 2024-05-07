from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


total_lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
               '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
               ']', '^', '_', '`', '{', '|', '}', '~']
def generate():
    password_entry.delete(0,END)
    random.shuffle(total_lista)
    password = ''.join(total_lista[:10])
    password_entry.insert(0, password)
    pyperclip.copy(password)

def add():
    site = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        site:{
        'email':email,
        'password':password
        }
    }
    if len(site) ==0 or len(password) == 0:
        messagebox.showinfo(title='Opps', message='Some of the windows are empty!!')
    else:

        try:
            with open('accounts.json', 'r') as file:
                #readinf the old data
                data = json.load(file)

        except FileNotFoundError:

            with open('accounts.json', 'w') as file:
                #saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # updating the old data
            data.update(new_data)
            with open('accounts.json', 'w') as file:
                #saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, 'eli3602021@gmail.com')

def search():

        try:
            with open('accounts.json','r') as data:
                data = json.load(data)
                key = data[website_entry.get()]
        except FileNotFoundError:
            messagebox.showerror(title='error', message='Record do not found.')

        else:

            messagebox.showinfo(title=website_entry.get(), message=f"Email: {key['email']}\nPassword: {key['password']}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('My Pass')
icon= PhotoImage(file='icon.png')
window.iconphoto(True, icon)
logo = PhotoImage(file='logo.png')
window.config(padx=50,pady=50)

image_label = Label(window,image=logo)
image_label.grid(column=1, row=0)

website_label = Label(window,text='WebSite:')

website_label.grid(column=0, row=1)

website_entry = Entry(window)
website_entry.grid(column=1, row=1,sticky='news', padx=10, pady=2)
website_entry.focus()
search_button = Button(window, text='Search',command=search)
search_button.grid(column=2,row=1,sticky='news', padx=10, pady=2)

email_label = Label(window, text='Email/Username:')
email_label.grid(column=0, row=2)
email_entry = Entry(window)
email_entry.grid(column=1, row=2 ,columnspan=2,sticky='news', padx=10, pady=2)
email_entry.insert(0, 'eli3602021@gmail.com')

password_label = Label(window, text='Password:')
password_label.grid(column=0, row=3)
password_entry = Entry(window,text='sdfs')
password_entry.grid(column=1, row=3,sticky='news', padx=10, pady=2)


generator_buttom = Button(window, text='Generate Password', command=generate)
generator_buttom.grid(column=2,row=3,sticky='news', padx=10, pady=2)

add_buttom = Button(window, text='Add', command=add)
add_buttom.grid(column=1,row=4,columnspan=2, sticky='news', padx=10, pady=2)


window.mainloop()
