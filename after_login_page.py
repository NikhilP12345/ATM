from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import coverpage
import deposit
import withdraw
import print_current


class operation():
    
    def __init__(self):
        self.root = Tk()
        self.options_frame = Frame(self.root, height = 400, width = 1500 ,bd = '7')

        
    def initialise(self):
        
        self.root.title('operation_page')
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
        after_login = Label(head_frame, text = 'OPERATION PAGE', font = 'Arial 30')
        after_login.config(justify = CENTER)
        after_login.pack(pady = 20)

        self.options_func()

    def options_func(self):
        self.options_frame.place(x = 0, y = 250)

        deposit = Label(self.options_frame, text = 'Deposit : ', font = 'Arial 25')
        deposit.grid(row = 0, column = 0, padx = 20, pady = 20)

        withdraw = Label(self.options_frame, text = 'Withdraw : ', font = 'Arial 25')
        withdraw.grid(row = 1, column = 0, padx = 20, pady = 20)

        print_balance = Label(self.options_frame, text = 'Print Current_balance : ', font = 'Arial 25')
        print_balance.grid(row = 2, column = 0, padx = 20, pady = 20)

        return_to_login = Label(self.options_frame, text = 'Return To Login Page : ', font = 'Arial 25')
        return_to_login.grid(row = 3, column = 0, padx = 20, pady = 20)

        exit_application = Label(self.options_frame, text = 'Exit Application : ', font = 'Arial 25')
        exit_application.grid(row = 4, column = 0, padx = 20, pady = 20)     

        self.entry_func()

    def entry_func(self):
        deposit_button = Button(self.options_frame, text = 'DEPOSIT', font = 'Arial 25', command = self.deposit_func)
        deposit_button.grid(row = 0, column = 1, padx = 20)

        withdraw_button = Button(self.options_frame, text = 'WITHDRAW', font = 'Arial 25', command = self.withdraw_func)
        withdraw_button.grid(row = 1, column = 1, padx = 20)

        print_button = Button(self.options_frame, text = 'PRINT CURRENT BALANCE', font = 'Arial 25', command = self.print_func)
        print_button.grid(row = 2, column = 1, padx = 20)

        return_button = Button(self.options_frame, text = 'RETURN TO LOGIN', font = 'Arial 25', command = self.return_func)
        return_button.grid(row = 3, column = 1, padx = 20)

        exit_button = Button(self.options_frame, text = 'EXIT THE APPLICATION', font = 'Arial 25', command = self.exit_func)
        exit_button.grid(row = 4, column = 1, padx = 20)

    def deposit_func(self):
        self.root.destroy()
        deposit_object = deposit.deposit_class()
        deposit_object.initialise()
        pass

    def withdraw_func(self):
        self.root.destroy()
        withdraw_object = withdraw.withdraw_class()
        withdraw_object.initialise()

    def print_func(self):
        self.root.destroy()
        print_object = print_current.print_class()
        print_object.initialise()

    def return_func(self):
        self.root.destroy()
        cover_page_object = coverpage.cover()
        cover_page_object.new_window()
    
    def exit_func(self):
        exit_var = messagebox.askquestion('Exit', 'Do you want to exit the application, Transcation will be lost', icon = 'warning')
        if exit_var == 'yes':
            self.root.destroy()





# a = operation()
# a.initialise()








