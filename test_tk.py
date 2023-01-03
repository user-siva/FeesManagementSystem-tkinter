
def open_register():
    login_frame.place_forget()
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    """image = Image.open("register.jpeg")

    # Resize the image using resize() method
    resize_image = image.resize((300, 350))

    img = ImageTk.PhotoImage(resize_image)

    Label(win,image=img,border=0,bg='white').place(x=50,y=90)"""

    frame = Frame(win)
    frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)

    heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white',
                    font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=570, y=15)

    def on_enter(e):
        if(user.get() == 'Name'):
            user.delete(0, 'end')

    def on_leave(e):
        if(len(user.get()) == 0):
            nametic.configure(text=u'\u2717', bg='white', fg='red')
            messagebox.showerror("showerror", "Name cant be a Null")
        else:
            if any(ch.isdigit() for ch in user.get()):
                nametic.configure(text=u'\u2717', bg='white', fg='red')
                messagebox.showerror("showerror", "Name cant be a number")
            else:
                nametic.config(text=u'\u2713', bg='white', fg='green')
        if(len(user.get()) == 0):
            user.insert(0, 'Name')

    user = ttb.Entry(frame, width=55, font=('Arial', 10), bootstyle="primary")
    user.place(x=430, y=120, height=40)
    nametic = Label(frame, text='', bg='white')
    nametic.place(x=430, y=80)

    user.insert(0, 'Name')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    def on_enter(e):
        if(mail.get() == 'Mail Id'):
            mail.delete(0, 'end')

    def on_leave(e):
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, mail.get()):
            mailtic.config(text=u'\u2713', bg='white', fg='green')
        else:
            mailtic.configure(text=u'\u2717', bg='white', fg='red')
            messagebox.showerror("showerror", "Check Email Id ? ")
        if(len(mail.get()) == 0):
            mail.insert(0, 'Mail Id')

    mail = ttb.Entry(frame, width=55, font=('Arial', 10), bootstyle="primary")
    mail.place(x=430, y=185,  height=40)
    mailtic = Label(frame, text='')
    mailtic.place(x=430, y=150)

    mail.insert(0, 'Mail Id')
    mail.bind("<FocusIn>", on_enter)
    mail.bind("<FocusOut>", on_leave)

    def on_enter(e):
        if(password.get() == 'Password'):
            password.delete(0, 'end')
            password.configure(show='*')

    def on_leave(e):
        regex = re.compile(
            r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
        if re.findall(regex, password.get()):
            passtic.config(text=u'\u2713', bg='white', fg='green')
        else:
            passtic.configure(text=u'\u2717', bg='white', fg='red')
            messagebox.showerror(
                "showerror", "password must be one Upper,Lower,Digit and Symbol")
        if(len(password.get()) == 0):
            password.insert(0, 'Password')
            password.configure(show='')

    password = ttb.Entry(frame, width=55, font=(
        'Arial', 10), bootstyle="primary")
    password.place(x=430, y=250, height=40)
    passtic = Label(frame, text='', bg='white')
    passtic.place(x=430, y=220)

    password.insert(0, 'Password')
    password.bind("<FocusIn>", on_enter)
    # password.bind("<FocusOut>",on_leave)

    #Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    def on_enter(e):
        if(cpass.get() == 'Conform Password'):
            cpass.delete(0, 'end')
            cpass.configure(show='*')

    def on_leave(e):
        if(password.get() == cpass.get()):
            cpasstic.config(text=u'\u2713', bg='white', fg='green')
        if(len(cpass.get()) == 0):
            cpass.insert(0, 'Conform Password')
            cpass.configure(show='')

    cpass = ttb.Entry(frame, width=55, font=('Arial', 10), bootstyle="primary")
    cpass.place(x=430, y=315,  height=40)
    cpasstic = Label(frame, text='', bg='white')
    cpasstic.place(x=430, y=290)

    cpass.insert(0, 'Conform Password')
    cpass.bind("<FocusIn>", on_enter)
    cpass.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=317)

    def store():
        inpname = user.get()
        inpmail = mail.get()
        inppassword = password.get()
        inpcpass = cpass.get()
        if(inppassword == inpcpass):

            cursor.execute(
                " CREATE TABLE IF NOT EXISTS User(name  text,mail  text,password  text,isadmin INTEGER NOT NULL DEFAULT 0 )")
            cursor.execute("INSERT INTO User values(?,?,?,?)",
                           (inpname, inpmail, inppassword, 0))
            messagebox.showinfo('Success', "Registration Successfull")
            login_frame.place(width=1500, height=2000)
            frame.place_forget()
            #rows = cursor.execute("SELECT * FROM User")
            # for i in rows:
            # print(i)
        else:
            cpasstic.config(text=u'\u2717', bg='white', fg='red')
            messagebox.showerror("showerror", "password Doesn't Match")

        con.commit()

    resize_img("images\in.png")
    register_img = PhotoImage(file=r"images\in.png")
    submit = ttb.Button(frame, text='SignUp',
                        image=register_img, compound=RIGHT, bootstyle='primary-outline', command=store)
    submit.image = register_img
    submit.place(x=570, y=400, height=40)

    def back():
        login_frame.place(width=1500, height=2000)
        frame.place_forget()
