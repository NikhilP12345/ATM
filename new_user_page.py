from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import coverpage



class new_user():
    def __init__(self):
        self.root = Tk()
        self.personal_info_section = Frame(self.root, height = 400, width = 1500 ,bd = '7')
        self.username_entry = Entry(self.personal_info_section, width = 20, font = 'Arial 15')
        self.name_entry = Entry(self.personal_info_section, width = 20, font = 'Arial 15')
        self.address_entry = Entry(self.personal_info_section, width = 20, font = 'Arial 15')
        self.pincode_entry = Entry(self.personal_info_section, width = 20, font = 'Arial 15')
        self.phone_no_entry = Entry(self.personal_info_section, width = 20, font = 'Arial 15')
        self.curr_pass_entry = Entry(self.personal_info_section, width = 20, font = 'Arial 15')
        self.gender = StringVar()
        self.date1 = StringVar()
        self.year = StringVar()
        self.months = StringVar()
        self.email_entry = Entry(self.personal_info_section, width = 20, font = 'Arial 15')
        self.revise_label1 = Label(self.personal_info_section, text = 'Your Username should be only alphabet and number', fg = 'red')
        self.revise_label1.grid(row = 0, column = 2)
        self.revise_label2 = Label(self.personal_info_section, text = 'Your name should be only alphabet', fg = 'red')
        self.revise_label2.grid(row = 1, column = 2)
        self.revise_label3 = Label(self.personal_info_section, text = 'Your address should be only alphabet and number', fg = 'red')
        self.revise_label3.grid(row = 2, column = 2)
        self.revise_label4 = Label(self.personal_info_section, text = 'Your pincode should be only number', fg = 'red')
        self.revise_label4.grid(row = 3, column = 2)
        self.revise_label5 = Label(self.personal_info_section, text = 'Your phone no should be only number', fg = 'red')
        self.revise_label5.grid(row = 4, column = 2)
        self.revise_label6 = Label(self.personal_info_section, text = 'Please enter the password', fg = 'red')
        self.revise_label6.grid(row = 5, column = 2)
        self.revise_label7 = Label(self.personal_info_section, text = 'You did not follow correct instruction', fg = 'red')
        self.revise_label7.grid(row = 6, column = 2)
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Nikhil",
        database = "atm_managment"
        )
        self.mycursor = self.mydb.cursor()


    def new_user_initialise(self):
        self.root.title('New User Page')
        self.head_frame_func()
        
        
        self.root.geometry('2000x2000')
        self.root.mainloop()

    def head_frame_func(self):
        #Head Frame
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

        #New user heading
        new_label = Label(head_frame, text = 'NEW USER', font = 'Arial 30')
        new_label.config(justify = CENTER)
        new_label.pack(pady = 20)

        self.personal_grid_label()



    #Personal Information Section
    #personal grid
    def personal_grid_label(self):
        
        self.personal_info_section.place(x = 0, y = 250)
        #info
        username_label = Label(self.personal_info_section, text = 'Username : ', font = 'Arial 15')
        username_label.grid(row = 0, column = 0, padx = 20, pady = 20)

        name_label = Label(self.personal_info_section, text = 'Name : ', font = 'Arial 15')
        name_label.config(justify = LEFT)
        name_label.grid(row = 1, column = 0, padx = 20, pady = 20)


        address_label = Label(self.personal_info_section, text = 'Address : ', font = 'Arial 15')
        address_label.grid(row = 2, column = 0, padx = 20, pady = 20)

        pincode_label = Label(self.personal_info_section, text = 'Pincode : ', font = 'Arial 15')
        pincode_label.grid(row = 3, column = 0, padx = 20, pady = 20)

        phone_no_label = Label(self.personal_info_section, text = 'Phone Number : ', font = 'Arial 15')
        phone_no_label.grid(row = 4, column = 0, padx = 20, pady = 20)

        cur_password_label = Label(self.personal_info_section, text = 'Password : ', font = 'Arial 15')
        cur_password_label.grid(row = 5, column = 0, padx = 20, pady = 20)

        gender_label = Label(self.personal_info_section, text = 'Gender : ', font = 'Arial 15')
        gender_label.grid(row = 0, column = 3, padx = 20, pady = 20)
        
        self.gender.set('0')
        rd1 = Radiobutton(self.personal_info_section, text = 'MALE', value = 'MALE', var = self.gender, font = 'Arial 15')
        rd1.grid(row = 0, column = 4, padx = 20, pady = 20)
        rd2 = Radiobutton(self.personal_info_section, text = 'FEMALE', value = 'FEMALE', var = self.gender, font = 'Arial 15')
        rd2.grid(row = 0, column = 5, padx = 20, pady = 20)
    
        date_birth_label = Label(self.personal_info_section, text = 'Date of Birth : ', font = 'Arial 15')
        date_birth_label.grid(row = 1, column = 3, padx = 20, pady = 20)
        Spinbox(self.personal_info_section, from_ = 1, to = 31, textvariable = self.date1, state = 'readonly').grid(row = 1, column = 4)

       
        Spinbox(self.personal_info_section, from_ = 1950, to = 2000, textvariable = self.year, state = 'readonly').grid(row = 1, column = 6)

        
        comboBox = ttk.Combobox(self.personal_info_section, textvariable = self.months, values = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), state = 'readonly')
        comboBox.grid(row = 1, column = 5)

        email_label = Label(self.personal_info_section, text = 'Email : ', font = 'Arial 15')
        email_label.grid(row = 2, column = 3, padx = 20, pady = 20)


        self.personal_grid_entry()


    def check_editing_func(self):
        temp = 0
        if re.search("^[A-Za-z0-9_-]*$", self.username_entry.get()) and self.username_entry.get() != '':
            self.revise_label1.destroy()
            temp += 1
        else:
            self.revise_label1 = Label(self.personal_info_section, text = 'Your Username should be only alphabet and number', fg = 'red')
            self.revise_label1.grid(row = 0, column = 2)
        
        if re.search("^[A-Za-z]*$", self.name_entry.get()) and self.name_entry.get() != '':
            self.revise_label2.destroy()
            temp += 1
        else:
            self.revise_label2 = Label(self.personal_info_section, text = 'Your name should be only alphabet', fg = 'red')
            self.revise_label2.grid(row = 1, column = 2)

        if re.search("^[A-Za-z0-9_-]*$", self.address_entry.get()) and self.address_entry.get() != '':
            temp += 1
            self.revise_label3.destroy()
        else:
            self.revise_label3 = Label(self.personal_info_section, text = 'Your address should be only alphabet and number', fg = 'red')
            self.revise_label3.grid(row = 2, column = 2)

        if re.search("^[0-9]*$", self.pincode_entry.get()) and self.pincode_entry.get() != '':
            temp += 1
            self.revise_label4.destroy()
        else:
            self.revise_label4 = Label(self.personal_info_section, text = 'Your pincode should be only number', fg = 'red')
            self.revise_label4.grid(row = 3, column = 2)

        if re.search("^[0-9]*$", self.phone_no_entry.get()) and self.phone_no_entry.get() != '':
            temp += 1
            self.revise_label5.destroy()
        else:
            self.revise_label5 = Label(self.personal_info_section, text = 'Your phone no should be only number', fg = 'red')
            self.revise_label5.grid(row = 4, column = 2)

        if self.curr_pass_entry.get() != '':
            temp += 1
            self.revise_label6.destroy()
            g = self.gender.get()
            d = self.date1.get()
            m = self.months.get()
            y = self.year.get()

        else:
            self.revise_label6 = Label(self.personal_info_section, text = 'Please enter the password', fg = 'red')
            self.revise_label6.grid(row = 5, column = 2)

        if temp == 6:
            self.revise_label7.destroy()
            editing_check = messagebox.askquestion('Editing Checking', 'Do you want to edit?')
            if editing_check == 'Yes':
                #edit again
                pass
            else:
                DateBirth = self.date1.get() + " " + self.months.get() + " " + self.year.get() 
                new_row = "INSERT INTO users (Username, Name, Address, Pincode, PhoneNo, Password, Gender, DateOfBirth, Email, Balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (self.username_entry.get(), self.name_entry.get(), self.address_entry.get(), self.pincode_entry.get(), self.phone_no_entry.get(), self.curr_pass_entry.get(), self.gender.get(), DateBirth, self.email_entry.get(), 0)
                self.mycursor.execute(new_row, val)
                self.mydb.commit()
                self.send_email_func()
                self.root.destroy()
                cover_page_object = coverpage.cover()
                cover_page_object.new_window()
        else:
            self.revise_label7 = Label(self.personal_info_section, text = 'You did not follow correct instruction', fg = 'red')
            self.revise_label7.grid(row = 6, column = 2)

    def send_email_func(self):
        email = 'panksnoobchouhan@gmail.com'
        password = 'Pankajnoob123'
        send_to_email = str(self.email_entry.get())
        subject = 'CREATION OF NEW USER' # The subject line
        message = """WELCOME TO OUR BANK SYSTEM
        YOU ARE THE USER OF OUR BANK AND FULLY AVAIL THE FACILITY OF OUR BANK """

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
        


    def personal_grid_entry(self):
        
        self.username_entry.grid(row = 0, column = 1, padx = 20, pady = 20)
        self.name_entry.grid(row = 1, column = 1, padx = 20, pady = 20)
        self.address_entry.grid(row = 2, column = 1, padx = 20, pady = 20)
        self.pincode_entry.grid(row = 3, column = 1, padx = 20, pady = 20)
        self.phone_no_entry.grid(row = 4, column = 1, padx = 20, pady = 20)
        self.curr_pass_entry.config(show = '*')
        self.curr_pass_entry.grid(row = 5, column = 1, padx = 20, pady = 20)
        self.email_entry.grid(row = 2, column = 4, padx = 30, pady = 20)

        submit_button = Button(self.personal_info_section, text = 'Submit', font = 'Arial 15', command = self.check_editing_func)
        submit_button.grid(row = 6, column = 1, padx = 20)


# a = new_user()
# a.new_user_initialise()