from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import after_login_page
import coverpage
import print_current



class withdraw_class():
    
    def __init__(self):
        self.root = Tk()
        self.withdraw_frame = Frame(self.root, height = 400, width = 1500 ,bd = '7')
        self.withdraw_entry = Entry(self.withdraw_frame, width = 15, font = 'Arial 30')
        self.warning_label = Label(self.withdraw_frame, text = 'Can only be numbers', font = 'Arial 20', fg = 'red')
        self.warning_label1 = Label(self.withdraw_frame, text = 'not enough balance for withdraw', font = 'Arial 20', fg = 'red')
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
        deposit_head = Label(head_frame, text = 'WITHDRAW PAGE', font = 'Arial 30')
        deposit_head.config(justify = CENTER)
        deposit_head.pack(pady = 20)

        self.deposit_func()

    def deposit_func(self):
        self.withdraw_frame.place(x = 0, y = 250)

        withdraw_label = Label(self.withdraw_frame, text = 'Enter The Withdraw Money : ', font = 'Arial 30')
        withdraw_label.grid(row = 0, column = 0, padx = 20, pady = 20)

        self.withdraw_entry.grid(row = 0, column = 1, padx = 20, pady = 20)

        self.warning_label.grid(row = 0, column = 2, padx = 20, pady = 20)

        withdraw_button = Button(self.withdraw_frame, text = 'WITHDRAW', font = 'Arial 25', command = self.withdraw_amount_func)
        withdraw_button.grid(row = 1, column = 0, padx = 10, pady = 40)

        return_to_oper = Button(self.withdraw_frame, text = 'RETURN OPERATION', font = 'Arial 25', command = self.return_oper_func)
        return_to_oper.grid(row = 1, column = 1, padx = 10, pady = 40, sticky = 'W')

        exit_button = Button(self.withdraw_frame, text = 'EXIT APPLICATION', font = 'Arial 25', command = self.exit_app_func)
        exit_button.grid(row = 1, column = 2, padx = 20, pady = 40, sticky = 'W')

    def withdraw_amount_func(self):
        temp = 0
        if re.search("^[0-9]*$", str(self.withdraw_entry.get())) and str(self.withdraw_entry.get()) != '':
            self.warning_label.destroy()
            temp +=1
        else:
            self.warning_label = Label(self.withdraw_frame, text = 'Can only be numbers', font = 'Arial 20', fg = 'red')
            self.warning_label.grid(row = 0, column = 2, padx = 20, pady = 20)

        if temp == 1:
            check_var = messagebox.askquestion('Withdraw', 'Do you want to Withdraw the current amount ?', icon = 'warning')
            if check_var == 'yes':
                user_db = (coverpage.username_head, )
                balance_db = "SELECT Balance FROM users WHERE Username = %s"
                self.mycursor.execute(balance_db, user_db)
                myresult = self.mycursor.fetchall()
                users_list = {}
                for x in myresult:
                    users_list[coverpage.username_head] = x[0]
                if users_list[coverpage.username_head] > int(self.withdraw_entry.get()):
                    self.warning_label1.destroy()
                    users_list[coverpage.username_head] = users_list[coverpage.username_head] - int(self.withdraw_entry.get())
                    update_db = "UPDATE users SET Balance = %s WHERE Username = %s"
                    update_value = (users_list[coverpage.username_head], coverpage.username_head)
                    self.mycursor.execute(update_db, update_value)
                    self.mydb.commit()
                    self.update_email_func(users_list[coverpage.username_head])
                    self.root.destroy()
                    print_object = print_current.print_class()
                    print_object.initialise()
                else:
                    self.warning_label1.grid(row = 2, column = 1, padx = 20, pady = 20)

    def update_email_func(self, amount_username):
        user_db1 = (coverpage.username_head, )
        email_db = "SELECT Email FROM users WHERE Username = %s"
        self.mycursor.execute(email_db, user_db1)
        myresult = self.mycursor.fetchall()
        email_list = {}
        for x in myresult:
            email_list[coverpage.username_head] = x[0] 
        
        email = 'panksnoobchouhan@gmail.com'
        password = 'Pankajnoob123'
        send_to_email = email_list[coverpage.username_head]
        subject = 'WITHDRAW OF PAYMENT' # The subject line
        message = 'You WITHDRAW: ' + str(self.withdraw_entry.get()) + '             ' + 'Your current amount is now: ' + str(amount_username)

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        # Attach the message to the MIMEMultipart object
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
        server.sendmail(email, send_to_email, text)
        server.quit()  

    def return_oper_func(self):
        self.root.destroy()
        after_login_object = after_login_page.operation()
        after_login_object.initialise()

    def exit_app_func(self):
        exit_var = messagebox.askquestion('Exit', 'Do you want to exit the application, Transcation will be lost', icon = 'warning')
        if exit_var == 'yes':
            self.root.destroy()
