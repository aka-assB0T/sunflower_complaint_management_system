from pathlib import Path
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

from complaintListing import ComplaintListing
from configdb import ConnectionDatabase


APP_DIR = Path(__file__).resolve().parent
IMAGE_PATH = APP_DIR / 'assets' / 'a.png'


def submit_page():
    home_root.destroy()
    conn = ConnectionDatabase()
    root = Tk()
    root.geometry('1500x750+10+10')
    root.title('Complaint Management System')
    root.configure(bg='#341C10')

    style = Style()
    style.theme_use('classic')
    for widget_style in ['TLabel', 'TButton', 'TRadioButton']:
        style.configure(widget_style, bg='blue')

    style.configure('TButton', font=('Product Sans', 20, 'bold'), borderwidth='4')
    style.map(
        'TButton',
        foreground=[('active', '!disabled', 'green')],
        background=[('active', 'white')],
    )

    button_submit = Button(root, text='Submit Now')
    button_submit.grid(row=5, column=2)

    Label(root, text='Firstname:', font=('Product Sans', 22)).grid(row=0, column=0, padx=50, pady=30)
    Label(root, text='Lastname:', font=('Product Sans', 22)).grid(row=1, column=0, padx=50, pady=30)
    Label(root, text='Address:', font=('Product Sans', 22)).grid(row=2, column=0, padx=50, pady=30)
    Label(root, text='Gender:', font=('Product Sans', 22)).grid(row=3, column=0, padx=50, pady=30)
    Label(root, text='Write Your Complaint :', font=('Product Sans', 22)).grid(row=4, column=0, padx=50, pady=30)

    first_name = Entry(root, width=40, font=('Product Sans', 18, 'bold'))
    first_name.grid(row=0, column=1, columnspan=2)

    last_name = Entry(root, width=40, font=('Product Sans', 18, 'bold'))
    last_name.grid(row=1, column=1, columnspan=2)

    address = Entry(root, width=40, font=('Product Sans', 18, 'bold'))
    address.grid(row=2, column=1, columnspan=2)

    gender_group = StringVar()
    Radiobutton(root, text='Male', value='male', variable=gender_group).grid(row=3, column=1)
    Radiobutton(root, text='Female', value='female', variable=gender_group).grid(row=3, column=2)

    comment = Text(root, width=60, height=7, font=('Product Sans', 18))
    comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    def save_data():
        message = conn.Add(
            first_name.get(),
            last_name.get(),
            address.get(),
            gender_group.get(),
            comment.get(1.0, 'end'),
        )
        first_name.delete(0, 'end')
        last_name.delete(0, 'end')
        address.delete(0, 'end')
        comment.delete(1.0, 'end')
        showinfo(title='Add Information', message=message)

    button_submit.config(command=save_data)
    root.mainloop()



def view_page():
    home_root.destroy()
    view_root = Tk()
    view_root.geometry('1500x750+10+10')
    view_root.title('Complaint Management System')
    view_root.configure(bg='#341C10')

    def admin_login(username, password):
        admin_username = 'u1'
        admin_password = '123'

        if admin_username == username and admin_password == password:
            ComplaintListing()
        else:
            showerror(title='Error!', message='Invalid Login')

    Label(view_root, text='Username:', font=('Product Sans', 22)).grid(row=7, column=0, padx=40, pady=40)
    username = Entry(view_root, width=40, font=('Product Sans', 22))
    username.grid(row=7, column=1, columnspan=2)

    Label(view_root, text='Password:', font=('Product Sans', 22)).grid(row=8, column=0, padx=10, pady=10)
    password = Entry(view_root, width=40, font=('Product Sans', 22), show='*')
    password.grid(row=8, column=1, columnspan=2)

    style = Style()
    style.configure('TButton', font=('Product Sans', 20, 'bold'), borderwidth='4')
    style.map(
        'TButton',
        foreground=[('active', '!disabled', 'green')],
        background=[('active', 'white')],
    )

    button_login = Button(view_root, text='Login')
    button_login.grid(row=20, column=5)
    button_login.config(command=lambda: admin_login(username.get(), password.get()))

    view_root.mainloop()


home_root = Tk()
home_root.geometry('1500x750+10+10')
home_root.title('Complaint Management System')
home_root.resizable(False, False)
home_root.configure(bg='#6FE7FF')

photo = PhotoImage(file=str(IMAGE_PATH))

label = Label(home_root, image=photo)
label.pack()

style = Style()
style.configure('TButton', font=('Product Sans', 20, 'bold'), borderwidth='4')
style.map(
    'TButton',
    foreground=[('active', '!disabled', 'green')],
    background=[('active', 'black')],
)

submit_button = Button(home_root, text='Submit a Complaint', command=submit_page)
submit_button.place(x=100, y=620)

view_button = Button(home_root, text='View Complaints', command=view_page)
view_button.place(x=1100, y=100)

home_root.mainloop()
