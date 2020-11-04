from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import mysql.connector
import coverpage
import after_login_page


class print_class():
    
    def __init__(self):
        self.root = Tk()
        self.print_frame = Frame(self.root, height = 400, width = 1500 ,bd = '7')
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Nikhil",
        database = "atm_managment"
        )
        self.mycursor = self.mydb.cursor()


        
    def initialise(self):
        
        self.root.title('Withdraw')
        self.head_frame()

        self.root.geometry('2000x2000')
        self.root.mainloop()

    def head_frame(self):
        head_frame = Frame(self.root, height = 300, width = 1500 ,bd = '7')
        head_frame.pack()
        head_label = Label(head_frame, text = 'WELCOME TO THE BANK SYSTEM', font = 'Times 50')
        head_label.pack()

        #Date
        current_time = datetime.now()
        time_label = Label(head_frame, text = current_time, font = 'Arial 30')
        time_label.config(justify = CENTER)
        time_label.pack()

        #Login heading
        deposit_head = Label(head_frame, text = 'PRINT BALANCE PAGE', font = 'Arial 30')
        deposit_head.config(justify = CENTER)
        deposit_head.pack(pady = 20)

        self.print_current_func()

    def print_current_func(self):
        self.print_frame.place(x = 0, y = 250)

        print_current_label = Label(self.print_frame, text = 'Your Current Balance is : ', font = 'Arial 30')
        print_current_label.grid(row = 0, column = 0, padx = 20, pady = 20)

        current_user = (coverpage.username_head, )
        current_db = "SELECT Balance FROM users WHERE Username = %s"
        self.mycursor.execute(current_db, current_user)
        myresult = self.mycursor.fetchall()
        users_list = {}
        for x in myresult:
            users_list[coverpage.username_head] = x[0]
        int_var = IntVar()
        int_var.set(users_list[coverpage.username_head])
        print_current_label = Label(self.print_frame, textvariable = int_var, font = 'Arial 30')
        print_current_label.grid(row = 0, column = 1, padx = 20, pady = 20)

        after_login_page_button = Button(self.print_frame, text = 'RETURN TO OPERATION PAGE', font = 'Arial 30', command = self.print_balance_func)
        after_login_page_button.grid(row = 1, column = 2, padx = 20, pady = 40)

    def print_balance_func(self):
        self.root.destroy()
        after_login_object = after_login_page.operation()
        after_login_object.initialise()

