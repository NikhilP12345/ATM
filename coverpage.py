from tkinter import *
from tkinter import ttk
from datetime import datetime
import mysql.connector
import new_user_page
import forgot_password
import after_login_page

username_head = ' '
class cover():
    def __init__(self):
        self.root = Tk()
        self.login_frame = Frame(self.root, height = 400, width = 900 ,bd = '7')
        self.user_entry = Entry(self.login_frame, width = 20, font = 'Arial 30')
        self.pass_entry = Entry(self.login_frame, width = 20, font = 'Arial 30')
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Nikhil",
        database = "atm_managment"
        )
        self.mycursor = self.mydb.cursor()
    
    def new_window(self):
        self.root.title('Bank login page')

        self.head_frame_func()
        
        self.root.geometry('2000x2000')
        self.root.mainloop()



    def head_frame_func(self):
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

        self.login_func()
    

    #LOGIN FRAME
    def login_func(self):

        self.login_frame.place(x = 0, y = 250)
        user_label = Label(self.login_frame, text = 'Username : ', font = 'Arial 30')
        user_label.grid(row = 0, column = 0, padx = 20, pady = 20)

        pass_label = Label(self.login_frame, text = 'Password : ', font = 'Arial 30')
        pass_label.grid(row = 1, column = 0, padx = 20, pady = 20)

        self.user_entry.insert(INSERT, 'Username')
        self.user_entry.grid(row = 0, column = 1, padx = 20, pady = 20)

        self.pass_entry.config(show = '*')
        self.pass_entry.grid(row = 1, column = 1, padx = 20, pady = 20)

        login_button = Button(self.login_frame, text = 'Login', font = 'Arial 30', command = self.after_login)
        login_button.grid(row = 2, column = 0, padx = 20, pady = 20, sticky = W)

        new_button = Button(self.login_frame, text = 'New User', font = 'Arial 30', command = self.cover_page_func)
        new_button.grid(row = 2, column = 1, padx = 20, pady = 20, sticky = W)

        forgot_button = Button(self.root, text = 'Forgot Password', font = 'Arial 30', width = 20, command = self.forgot_pass_func)
        forgot_button.place(x = 600, y = 458)

        bank_image = PhotoImage(file = '2.png')
        lbl_image = Label(self.root, image = bank_image)
        lbl_image.place(x = 1000, y = 250)

    def cover_page_func(self):
        self.root.destroy()
        new_user_object = new_user_page.new_user()
        new_user_object.new_user_initialise()
        
    def forgot_pass_func(self):
        self.root.destroy()
        forgot_object = forgot_password.forgot()
        forgot_object.initialise()

    def after_login(self):
        global username_head
        self.mycursor.execute("SELECT Username, Password FROM users")
        myresult = self.mycursor.fetchall()
        users_list = {}
        for x in myresult:
            users_list[x[0]] = x[1]

        for i in range(0,len(users_list)):
            # if self.user_entry.get() in users_list and self.pass_entry.get() == users_list[self.user_entry.get()] and self.user_entry.get() != '' and self.pass_entry.get() != '':
            #     self.root.destroy()
            #     after_login_object = after_login_page.operation()
            #     after_login_object.initialise()

            if (self.user_entry.get() not in users_list) or (self.user_entry.get() == ''):
                warning_label1 = Label(self.login_frame, text = 'Incorrect Username', fg = 'red')
                warning_label1.grid(row = 0, column = 2)

            elif (self.pass_entry.get() != users_list[self.user_entry.get()]) or (self.pass_entry.get() == ''):
                warning_label2 = Label(self.login_frame, text = 'Incorrect Password', fg = 'red')
                warning_label2.grid(row = 1, column = 2)  

            else:
                username_head = self.user_entry.get()
                self.root.destroy()
                after_login_object = after_login_page.operation()
                after_login_object.initialise()








    


# a = cover()
# a.new_window()