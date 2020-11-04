from tkinter import *
from tkinter import ttk
from datetime import datetime
import mysql.connector
import coverpage


class forgot():
    def __init__(self):
        self.root = Tk()
        self.forgot_password_section = Frame(self.root, height = 400, width = 1500 ,bd = '7')
        self.forgot_password_section.place(x = 0, y = 250)
        self.username_entry = Entry(self.forgot_password_section, width = 20, font = 'Arial 15')
        self.check_username_button = Button(self.forgot_password_section, text = 'Check Username', font = 'Arial 15', command = self.check_username_func)
        self.password_entry = Entry(self.forgot_password_section, width = 20, font = 'Arial 15')
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Nikhil",
        database = "atm_managment"
        )
        self.mycursor = self.mydb.cursor()

    def initialise(self):
        self.root.title('Forgot Password page')

        self. main_head()
        self.root.geometry('2000x2000')
        self.root.mainloop()

    def main_head(self):
    # Head Frame
    # Head
        head_frame = Frame(self.root, height = 300, width = 1500 ,bd = '7')
        head_frame.pack()
        head_label = Label(head_frame, text = 'WELCOME TO THE BANK SYSTEM', font = 'Times 50')
        head_label.pack()

        #Date
        current_time = datetime.now()
        time_label = Label(head_frame, text = current_time, font = 'Arial 30')
        time_label.config(justify = CENTER)
        time_label.pack()

        self.forgot_pass_check_func()

    def check_username_func(self):
        self.mycursor.execute("SELECT Username, Password FROM users")
        myresult = self.mycursor.fetchall()
        users_list = {}
        for x in myresult:
            users_list[x[0]] = x[1]
        if self.username_entry.get() in users_list:
            confirmed_username_label = Label(self.forgot_password_section, text = 'Username is present', fg = 'red')
            confirmed_username_label.grid(row = 0, column = 2)
            
            self.username_entry['state'] = 'disabled'
            self.check_username_button['state'] = 'disabled'
            password_label = Label(self.forgot_password_section, text = 'Set New Password : ', font = 'Arial 15')
            password_label.grid(row = 3, column = 0, padx = 20, pady = 20)


            self.password_entry.config(show = '*')
            self.password_entry.grid(row = 3, column = 1, padx = 20, pady = 20)

        else:
            confirmed_username_label = Label(self.forgot_password_section, text = 'Username is not present', fg = 'red')
            confirmed_username_label.grid(row = 0, column = 2) 
            
    def login_page_func(self):
        update_db = "UPDATE users SET Password = %s WHERE Username = %s"
        update_value = (self.password_entry.get(), self.username_entry.get())

        self.mycursor.execute(update_db, update_value)
        self.mydb.commit()

        self.root.destroy()
        cover_page_object = coverpage.cover()
        cover_page_object.new_window()
        
    def forgot_pass_check_func(self):
        #info
        username_label = Label(self.forgot_password_section, text = 'Username : ', font = 'Arial 15')
        username_label.grid(row = 0, column = 0, padx = 20, pady = 20)

        self.username_entry.grid(row = 0, column = 1, padx = 20, pady = 20)
        self.check_username_button.grid(row = 1, column = 1, padx = 20, pady = 20)

        login_button = Button(self.forgot_password_section, text = 'Login', font = 'Arial 15', command = self.login_page_func)
        login_button.grid(row = 7, column = 1, padx = 20, pady = 20)

