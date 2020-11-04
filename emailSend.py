import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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



















sender_email = "testingniks6@gmail.com"
receiver_email = "pariharnikhil92@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
html = """\
<table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" style="border-collapse: collapse; border: none;">

    <!-- START HEADER/BANNER -->

    <tbody>
        <tr>
            <td align="center">
                <table class="col-600" width="600" border="0" align="center" cellpadding="0" cellspacing="0">
                    <tbody>
                        <tr>
                            <td align="center" valign="top" background="https://drive.google.com/uc?id=1eSqvTMNpzRDSWzNpet_elFaxhmJzngzS&export=download" bgcolor="#66809b" style="background-size:cover; background-position:top;height:400;  display: block;
                            margin-left: auto;
                            margin-right: auto;
                            width: 100%;">
                                <table class="col-600" width="600" height="200" border="0" align="center" cellpadding="0" cellspacing="0">

                                    <tbody>
                                        <tr>
                                            <td height="40"></td>
                                        </tr>


                                        <tr>
                                            <!-- <td align="center" style="line-height: 0px;">
                                            <img style="display:block; line-height:0px; font-size:0px; border:0px;" src="https://designmodo.com/demo/emailtemplate/images/logo.png" width="109" height="103" alt="logo">
                                        </td>
                                    </tr>
    
    
    
                                    <tr>
                                        <td align="center" style="font-family: 'Raleway', sans-serif; font-size:37px; color:#ffffff; line-height:24px; font-weight: bold; letter-spacing: 7px;">
                                            EMAIL <span style="font-family: 'Raleway', sans-serif; font-size:37px; color:#ffffff; line-height:39px; font-weight: 300; letter-spacing: 7px;">TEMPLATE</span>
                                        </td>
                                    </tr>
    
    
    
    
    
                                    <tr>
                                        <td align="center" style="font-family: 'Lato', sans-serif; font-size:15px; color:#ffffff; line-height:24px; font-weight: 300;">
                                            A creative email template for your email campaigns, promotions <br>and products across different email platforms.
                                        </td>
                                    </tr> -->


                                            <tr>
                                                <td height="50"></td>
                                            </tr>
                                    </tbody>
                                </table>
                            </td>
                            </tr>
                    </tbody>
                </table>
            </td>
            </tr>


            <!-- END HEADER/BANNER -->


            <!-- START 3 BOX SHOWCASE -->

            <tr>
                <td align="center">
                    <table class="col-600" width="600" border="0" align="center" cellpadding="0" cellspacing="0" style="margin-left:20px; margin-right:20px;">
                        <tbody>
                            <tr>
                                <td height="35"></td>
                            </tr>

                            <tr>
                                <td align="center" style="font-size:35px; font-weight: bold; color:#2a3a4b;"><span style="font-size: 35px;">
                                    Reckon 3.0
                                </span> </td>
                            </tr>

                            <tr>
                                <td height="10"></td>
                            </tr>
                            <tr>
                                <td align="center" style="font-size:24px; font-weight: bold; color:#2a3a4b;">&nbsp;<strong>Be the change maker</strong></td>
                            </tr>
                            <tr>
                                <td height="10"></td>
                            </tr>
                            <tr>
                                <td align="center" style="font-size:22px; font-weight: bold; color:#2a3a4b;"><strong>20 to 22 March 2020</strong></td>
                            </tr>
                            <!-- <tr>
                            <td align="center" style="font-family: 'Lato', sans-serif; font-size:14px; color:#757575; line-height:24px; font-weight: 300;">
                                Prepare some  flat icons of your choice. You can place your content below.<br>
                                Make sure it's awesome.
                            </td>
                        </tr> -->

                        </tbody>
                    </table>
                </td>
            </tr>

            <tr>
                <td align="center">
                    <table class="col-600" width="600" border="0" align="center" cellpadding="0" cellspacing="0">
                        <tbody>
                            <tr>
                                <td height="10"></td>
                            </tr>
                            <tr>
                                <td>


                                    <table width="287" border="0" align="left" cellpadding="0" cellspacing="0" class="col2" style="">
                                        <tbody>
                                            <tr>
                                                <td align="center">
                                                    <table class="insider" width="598" border="0" align="center" cellpadding="0" cellspacing="4">



                                                        <tbody>

                                                            <tr>
                                                                <td height="5"></td>
                                                            </tr>


                                                            <tr>
                                                                <td style="font-family: 'Lato', sans-serif; font-size:14px; color:#7f8c8d; line-height:24px; font-weight: 300;">
                                                                    <span style="text-align: justify; padding-right: 10px; padding-left: 10px; display: flex;
                                                        justify-content: flex-start;">
                         
                                                            I hope this mail finds you in the best of your working spirit. Since Hire a Camp is known to provide empowerment and support at all levels.It would be great if you collaborate with us and support us in our event.<br><br> I am
                                                            reaching out to inform you that Jodhpur Institute of Engineering and Technology is organising RECKON 3.0 - A 36-hour Hackathon' from 20th-22nd March 2020, aimed for students to express their true potential and bring their innovative
                                                            ideas to life. We strongly believe in the ideology of innovation and the spirit to shape a thriving future society. For the past two years, 800+ participants registered their idea from various parts of India and 300+ students
                                                            were shortlisted to attend RECKON. We were able to collaborate with 20+ startups and tech giants to provide opportunities like internships, jobs, investments to the participants and incubation for the 10 teams under Ted-Start
                                                            along with cash prizes and swags as a token of appreciation for the participants.<br><br> With the success of RECKON 1.0 and RECKON 2.0, this year we are organising RECKON 3.0 and like to open the ocean of ample opportunities
                                                            by expanding your collaboration with our team. We are expecting 500+ techies from all over India to come under a single roof and unleash their creativity to make astounding innovations and deal with real-life interests the
                                                            world is facing.  I request you to kindly extend your supporting hand to discuss a chance of collaboration and sponsorship and make this event even more impacting and successful. We are also inviting problem statements from
                                                            organisations and I would be grateful if you also provide yours.
                                                    <br><br> Looking forward to a positive response.
                                                    <br><br> Thank You<br> Navdeep Singh Sodha<br> (+91)-7023129515
                                                    <br> Company and Public Relations<br> Team RECKON<br>
                                
                                
                                               
                                                        </span>
                                                                </td>
                                                            </tr>

                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>





                                    <table width="1" height="20" border="0" cellpadding="0" cellspacing="0" align="left">
                                        <tbody>
                                            <tr>
                                                <td height="20" style="font-size: 0;line-height: 0;border-collapse: collapse;">
                                                    <p style="padding-left: 24px;">&nbsp;</p>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>


                                    <!-- <table class="col3" width="183" border="0" align="left" cellpadding="0" cellspacing="0">
                                    <tbody><tr>
                                        <td height="30"></td>
                                    </tr>
                                    <tr>
                                        <td align="center">
                                            <table class="insider" width="133" border="0" align="center" cellpadding="0" cellspacing="0">
    
                                                <tbody><tr align="center" style="line-height:0px;">
                                                    <td>
                                                        <img style="display:block; line-height:0px; font-size:0px; border:0px;" src="https://designmodo.com/demo/emailtemplate/images/icon-team.png" width="69" height="78" alt="icon">
                                                    </td>
                                                </tr>
    
    
                                                <tr>
                                                    <td height="15"></td>
                                                </tr>
    
    
                                                <tr align="center">
                                                    <td style="font-family: 'Raleway', sans-serif; font-size:20px; color:#2b3c4d; line-height:24px; font-weight: bold;">Our Team</td>
                                                </tr>
    
    
                                                <tr>
                                                    <td height="10"></td>
                                                </tr>
    
    
                                                <tr align="center">
                                                        <td style="font-family: 'Lato', sans-serif; font-size:14px; color:#757575; line-height:24px; font-weight: 300;">Place some cool text here.</td>
                                                </tr>
    
    
    
                                            </tbody></table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td height="30"></td>
                                    </tr>
                                </tbody></table>
     -->

                                    <!--     
                                <table width="1" height="20" border="0" cellpadding="0" cellspacing="0" align="left">
                                    <tbody><tr>
                                        <td height="20" style="font-size: 0;line-height: 0;border-collapse: collapse;">
                                            <p style="padding-left: 24px;">&nbsp;</p>
                                        </td>
                                    </tr>
                                </tbody></table> -->



                                    <!-- <table class="col3" width="183" border="0" align="right" cellpadding="0" cellspacing="0">
                                    <tbody><tr>
                                        <td height="30"></td>
                                    </tr>
                                    <tr>
                                        <td align="center">
                                            <table class="insider" width="133" border="0" align="center" cellpadding="0" cellspacing="0">
    
                                                <tbody><tr align="center" style="line-height:0px;">
                                                    <td>
                                                        <img style="display:block; line-height:0px; font-size:0px; border:0px;" src="https://designmodo.com/demo/emailtemplate/images/icon-portfolio.png" width="69" height="78" alt="icon">
                                                    </td>
                                                </tr>
    
    
                                                <tr>
                                                    <td height="15"></td>
                                                </tr>
    
    
                                                <tr align="center">
                                                    <td style="font-family: 'Raleway',  sans-serif; font-size:20px; color:#2b3c4d; line-height:24px; font-weight: bold;">Our Portfolio</td>
                                                </tr>
    
    
                                                <tr>
                                                    <td height="10"></td>
                                                </tr>
    
    
                                                <tr align="center">
                                                    <td style="font-family: 'Lato', sans-serif; font-size:14px; color:#757575; line-height:24px; font-weight: 300;">Place some cool text here.</td>
                                                </tr>
    
                                            </tbody></table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td height="30"></td>
                                    </tr>
                                </tbody></table> -->


                                </td>
                            </tr>
                        </tbody>

                        <!-- START FOOTER -->

                        <tr>
                            <td align="center">
                                <table align="center" width="100%" border="0" cellspacing="0" cellpadding="0">
                                    <tbody>
                                        <tr>
                                            <td height="50"></td>
                                        </tr>
                                        <tr>
                                            <td align="center" bgcolor="#999999" height="185">
                                                <table class="col-600" width="600" border="0" align="center" cellpadding="0" cellspacing="0">
                                                    <tbody>
                                                        <tr>
                                                            <td height="25"></td>
                                                        </tr>

                                                        <tr>
                                                            <td align="center" style="font-family: 'Raleway',  sans-serif; font-size:26px; font-weight: 500; color:white;">Follow us for some cool stuffs!!!</td>
                                                        </tr>


                                                        <tr>
                                                            <td height="25"></td>
                                                        </tr>



                                                    </tbody>
                                                </table>
                                                <table align="center" width="35%" border="0" cellspacing="0" cellpadding="0">
                                                    <tbody>
                                                        <tr>
                                                            <!-- <td align="center" width="30%">&nbsp;</td> -->
                                                            <td align="center" width="30%" style="vertical-align: top;">
                                                                <a href="https://twitter.com/RECKONjiet" target="_blank"> <img src="https://drive.google.com/uc?id=1OjdPoUAd5Wh6mPreDgM6R98S-zbTKUHJ&export=download"> </a>
                                                            </td>
                                                            <!-- <td align="center" width="30%"><span>&nbsp;</span></td> -->
                                                            <td align="center" class="margin" width="30%" style="vertical-align: top;">
                                                                <a href="https://www.linkedin.com/company/reckonjiet" target="_blank"> <img src="https://drive.google.com/uc?id=1m9Vuurx6zJhxKAgjVFFqaYPaD1aEtuBI&export=download"></a>
                                                            </td>
                                                            <!-- <td align="center" width="30%"><span>&nbsp;</span></td> -->
                                                            <td align="center" width="30%" style="vertical-align: top;">
                                                                <a href="http://www.reckon.jietjodhpur.ac.in/" target="_blank"> <img src="https://drive.google.com/uc?id=1p_XX10IVKhreICMaha5JwoXMOzvFy-vO&export=download"> </a>
                                                            </td>
                                                            <!-- <td align="center" width="30%"><span>&nbsp;</span></td> -->
                                                            <td align="center" width="30%" style="vertical-align: top;">
                                                                <a href="https://www.instagram.com/reckon_x/?hl=en" target="_blank"> <img src="https://drive.google.com/uc?id=1RfJuhjiY7w_kQ_YwB5k0C5bOLYS-F2Ye&export=download"> </a>
                                                            </td>
                                                            <!-- <td align="center" width="30%"><span>&nbsp;</span></td> -->
                                                            <!-- <td align="center" width="30%" style="vertical-align: top;">
                                                                <a href="https://twitter.com/RECKONjiet" target="_blank"> <img src="https://drive.google.com/a/jietjodhpur.ac.in/uc?authuser=2&id=1OjdPoUAd5Wh6mPreDgM6R98S-zbTKUHJ&export=download"> </a>
                                                            </td> -->
                                                        </tr>
                                                    </tbody>
                                                </table>



                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
    </tbody>
    </table>
    </td>
    </tr>

    <!-- END FOOTER -->



</table>
</td>
</tr>

<tr>
    <td height="5"></td>
</tr>


<!-- END 3 BOX SHOWCASE -->
<!-- START FOOTER -->
""".format(password = password)

# Turn these into plain/html MIMEText objects
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part2)

# Create secure connection with server and send email
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(
#         sender_email, receiver_email, message.as_string()
#     )
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(sender_email,password)
smtpserver.sendmail(sender_email,receiver_email,message.as_string())
print("Sent")
smtpserver.close()
