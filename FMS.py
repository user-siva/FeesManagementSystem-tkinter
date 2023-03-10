import ttkbootstrap as ttb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, filedialog
from tkinter.ttk import Scrollbar
from PIL import Image
import pandas as pd
import sqlite3
from fpdf import FPDF
import re
import io
import datetime

win = ttb.Window(themename="litera")

# w, h = win.winfo_screenwidth(), win.winfo_screenheight()
win.geometry("800x800")
win.state("zoomed")

login_frame = Frame(win)
login_frame.place(width=1500, height=2000)

#img = Image.open('coins.jpeg')

#img1 = ImageTk.PhotoImage(img)
limg = Label(login_frame)
#limg.image = img1
#limg.place(x=0, y=0)


def resize_img(img):
    image = Image.open(img)
    image = image.resize((25, 25))
    image.save(img)
    return image


def login():
    uname = username_ent.get()
    pwd = password_ent.get()

    if uname == '' or pwd == '':
        messagebox.showerror("Error", "fill the empty field")
    else:
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        # cursor = con.execute(
        # "INSERT into User(name,mail,password,isadmin) values('admin','admin@tec.com','admintec',1)")
        con.commit()
        a = con.execute('SELECT * FROM User')
        for i in a:
            print(i)
        cursor = con.execute(
            'SELECT * from User where name=? and password=?', (uname, pwd))
        data = cursor.fetchone()
        if data:
            print("Login Sucsess")
            print(data)
            if data[3] == 0:
                login_frame.place_forget()
                # tab.place(width=1600, height=50)
                # tree.pack()
                # tree_frame.place(x=50, y=80)
                cashier.place(width=1500, height=900)
            elif data[3] == 1:
                login_frame.place_forget()
                tab.place(width=1600, height=200)
                tree.pack()
                tree_frame.place(x=50, y=130)
                # det_btn.place_forget()

        else:
            messagebox.showinfo('Wrong', "Incorrect username or password")


head = Label(login_frame, text='Login', font=('Arial', 30))
head.place(x=1100, y=160)
user_label1 = Label(login_frame, text='Username:', font=(
    'Arial', 20), fg='green').place(x=1000, y=220)
username_ent = ttb.Entry(login_frame, bootstyle="primary", width=28)
username_ent.focus_set()
username_ent.place(x=1150, y=230)

pass_label1 = Label(login_frame, text='Password:', font=(
    'Arial', 20), fg='green').place(x=1000, y=270)
password_ent = ttb.Entry(login_frame, bootstyle="primary", width=28, show='*')
password_ent.place(x=1150, y=280)

resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\enter.png")
img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\enter.png")
sub_button = ttb.Button(login_frame, text='Login      ', image=img, compound=RIGHT,
                        bootstyle=(SUCCESS, OUTLINE), command=login)
sub_button.place(x=1180, y=330, height=40)


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

    heading = Label(frame, text='Sign up',
                    font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.config(fg="#57a1f8", bg='white')
    heading.place(x=570, y=15)

    def on_enter(e):
        if(user.get() == 'Name'):
            user.delete(0, 'end')

    def on_leave(e):
        if(len(user.get()) == 0):
            user.insert(0, 'Name')
            nametic.configure(text=u'\u2717', bg='white', fg='red')
            uerr = "Name can't be Null           "
        else:
            if any(ch.isdigit() for ch in user.get()):
                nametic.configure(text=u'\u2717', bg='white', fg='red')
                uerr = "Name can't be Number          "

            else:
                nametic.config(text=u'\u2713', bg='white', fg='green')
                uerr = "                                                                     "
                global uerr1
                uerr1 = True

        usererror = Label(frame, text=uerr, font=(
            'Microsoft Yahei UI Light', 8, 'bold'))
        usererror.config(fg="red")
        usererror.place(x=435, y=160)

        if uerr1 and merr1 and perr1 and cerr1:
            submit.config(state='normal')
        else:
            submit.config(state='disabled')

    user = ttb.Entry(frame, width=55, font=('Arial', 10), bootstyle="primary")
    user.place(x=430, y=120, height=40)
    # user.focus_set()
    nametic = Label(frame, text='', bg='white')
    nametic.place(x=830, y=125)

    user.insert(0, 'Name')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    def on_enter(e):
        if(mail.get() == 'Mail Id'):
            mail.delete(0, 'end')

    def on_leave(e):
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, mail.get()):
            mailtic.config(text=u'\u2713', bg='white', fg='green')
            merr = "                               "
            global merr1
            merr1 = True
        else:
            mailtic.configure(text=u'\u2717', bg='white', fg='red')
            merr = "Invalid Mail Id"
            if(len(mail.get()) == 0):
                mail.insert(0, 'Mail Id')

        mailerror = Label(frame, text=merr, font=(
            'Microsoft Yahei UI Light', 8, 'bold'))
        mailerror.config(fg="red")
        mailerror.place(x=435, y=225)

        if uerr1 and merr1 and perr1 and cerr1:
            submit.config(state='normal')
        else:
            submit.config(state='disabled')

    mail = ttb.Entry(frame, width=55, font=('Arial', 10), bootstyle="primary")
    mail.place(x=430, y=185,  height=40)
    mailtic = Label(frame, text='')
    mailtic.place(x=830, y=190)

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
            perr = "                                                                                                  "
            global perr1
            perr1 = True
        else:
            passtic.configure(text=u'\u2717', bg='white', fg='red')
            perr = "Password Must Contains [0-9],[a-z],[A-Z],Symbol and length is 8"
        if(len(password.get()) == 0):
            password.insert(0, 'Password')
            password.configure(show='')

        passerror = Label(frame, text=perr, font=(
            'Microsoft Yahei UI Light', 8, 'bold'))
        passerror.config(fg="red")
        passerror.place(x=435, y=290)

        if uerr1 and merr1 and perr1 and cerr1:
            submit.config(state='normal')
        else:
            submit.config(state='disabled')

    password = ttb.Entry(frame, width=55, font=(
        'Arial', 10), bootstyle="primary")
    password.place(x=430, y=250, height=40)
    passtic = Label(frame, text='', bg='white')
    passtic.place(x=830, y=255)

    password.insert(0, 'Password')
    password.bind("<FocusIn>", on_enter)
    password.bind("<FocusOut>", on_leave)

    #Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    def on_enter(e):
        if(cpass.get() == 'Confirm Password'):
            cpass.delete(0, 'end')
            cpass.configure(show='*')

    def on_leave(e):
        if(password.get() == cpass.get()):
            cpasstic.config(text=u'\u2713', bg='white', fg='green')
            cerr = "                                                 "
            global cerr1
            cerr1 = True
        else:
            cerr = "Password Doesn't Match"
        if(len(cpass.get()) == 0):
            cpass.insert(0, 'Confirm Password')
            cpass.configure(show='')

        cpasserror = Label(frame, text=cerr, font=(
            'Microsoft Yahei UI Light', 8, 'bold'))
        cpasserror.config(fg="red")
        cpasserror.place(x=435, y=355)

        if uerr1 and merr1 and perr1 and cerr1:
            submit.config(state='normal')
        else:
            submit.config(state='disabled')

    cpass = ttb.Entry(frame, width=55, font=('Arial', 10), bootstyle="primary")
    cpass.place(x=430, y=315,  height=40)
    cpasstic = Label(frame, text='', bg='white')
    cpasstic.place(x=830, y=320)

    cpass.insert(0, 'Confirm Password')
    cpass.bind("<FocusIn>", on_enter)
    #cpass.bind("<FocusOut>", on_leave)
    cpass.bind("<KeyRelease>", on_leave)

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

    submit = ttb.Button(frame, text='SignUp',
                        bootstyle=(SUCCESS, OUTLINE), command=store)
    submit.place(x=570, y=400, height=40)
    submit.config(state="disabled")

    # def back_register():
    #    frame.place_forget()
    #   login_frame.place(width=1500, height=2000)

    # resize_img("images\previous.png")
    #previous_img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\previous.png")
    # back = ttb.Button(
    # frame, text="Back", bootstyle='danger-outline', image=previous_img, compound=LEFT, command=back_register)
    #back.image = previous_img
    #back.place(x=40, y=10, height=40)


resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\big.png")
user_img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\big.png")
register_button = ttb.Button(login_frame, text='Register   ', image=user_img, compound=RIGHT,
                             command=open_register)
register_button.place(x=1010, y=330, height=40)
register_button.image = user_img
tab = ttb.Frame(win)
# tab.place(width=1600, height=50)


def search():
    query = search_entry.get()
    selections = []
    for child in tree.get_children():
        print(tree.item(child)['values'])
        if str(query) in str(tree.item(child)['values'][1]):
            # print(tree.item(child)['values'])
            selections.append(child)
    print('search completed')
    tree.selection_set(selections)
    tree.see(selections[0])


search_entry = ttb.Entry(tab, width=38)
search_entry.focus_set()
search_entry.place(x=880, y=10, height=40)

resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\search.png")
search_img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\search.png")
search_btn = ttb.Button(tab, text='Search    ', image=search_img, bootstyle='ingo-outline',
                        compound=RIGHT, command=search)
search_btn.place(x=1130, y=10)


tree_frame = Frame(win)


tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=BOTH)

tree = ttb.Treeview(
    tree_frame, yscrollcommand=tree_scroll.set, height=35, bootstyle='info', selectmode="extended")


tree_scroll.config(command=tree.yview)


db = sqlite3.connect('data.db')


def import_data():
    filename = filedialog.askopenfilename(title="Open a File", filetype=(
        ("xlxs files", ".*xlsx"), ("All Files", "*.")))
    if filename:
        filename = r"{}".format(filename)
        dfs = pd.read_excel(filename, sheet_name=None)
        print(dfs)
        for table, df in dfs.items():
            df.to_sql(table, db, if_exists='append')
            db.commit()
        messagebox.showinfo('Success', "Data successfully added")
        a = db.execute('SELECT * FROM SHEET1')
        for i in a:
            print(i)


varlist = StringVar(tab)
deptdrop = ttk.OptionMenu(
    tab, varlist, "Select a Department", "CSE", "ECE", "EEE", "MECH", "CIVIL")
deptdrop.place(x=350, y=10, height=40)

opt = StringVar(tab)
yeardrop = ttk.OptionMenu(
    tab, opt, "Select Year", "1 Year", "2 Year", "3 Year", "4 Year")
yeardrop.place(x=510, y=10, height=40)


def cpdf():
    deptname = varlist.get()
    yearval = opt.get()[0]

    datas = db.execute(
        "SELECT * FROM Sheet1 Where Department=? AND Year=?", (deptname, yearval))
    pdf = FPDF()
    pdf.add_page()
    pdf.image(r'images/header_word1.jpg', w=190)
    for row in datas:
        pdf.set_font("Arial", size=20, style="BI")
        pdf.set_text_color(7, 145, 134)
        pdf.cell(200, 40, txt=f"NAME     :  {row[2]}", ln=1, align='C')
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)

        pdf.cell(
            200, 10, txt=f"Rollno                 : {row[1]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Year                   : {row[4]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Department             : {row[5]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Previous Year Balance  : {row[6]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Admission Fees         : {row[7]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Tution Fees            : {row[8]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Bus Fees               : {row[9]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Hostel Fees            : {row[10]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Total Fees             : {row[11]}", border=1, ln=2, align='L')

        pdf.cell(200, 30, txt="SCHOLARSHIP INFO", ln=1, align='C')

        pdf.cell(
            200, 10, txt=f"FGG                    : {row[12]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"PMSS                   : {row[13]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"7.5% GQ                : {row[14]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Other scholarships     : {row[15]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"KET Scholarship        : {row[16]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Student to Pay         : {row[17]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Scholarship Total      : {row[18]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Remaining Fees         : {row[19]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Fees Paid              : {row[20]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Balance                : {row[21]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Total Fees Paid        : {row[22]}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Current Balance        : {row[23]}", border=1, ln=2, align='L')

    pdf.output(yearval+"year"+"_"+deptname+".pdf")
    messagebox.showinfo("Success", "Report successfully saved")


resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\download (1).png")
pdf_img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\download (1).png")
cpdf = ttb.Button(tab, text='GetPdf', image=pdf_img,
                  compound=RIGHT, bootstyle='success', command=cpdf)
cpdf.place(x=635, y=10)

resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\import.png")
import_img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\import.png")
import_btn = ttb.Button(
    tab, text='Import Data    ', bootstyle='danger', image=import_img, compound=RIGHT, command=import_data)
import_btn.place(x=50, y=10)


def backup():
    conn = sqlite3.connect('data.db')
    with io.open('fee_details_backup.sql', 'w') as p:

        for line in conn.iterdump():

            p.write('%s\n' % line)
    print(' Backup performed successfully!')
    print(' Data Saved as backupdatabase_dump.sql')

    conn.close()


resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\cloud.png")
backup_img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\cloud.png")
backup_btn = ttb.Button(
    tab, text='Backup', command=backup, image=backup_img, compound=RIGHT, bootstyle='info')
backup_btn.place(x=760, y=10)


def admin_logout():
    tab.place_forget()
    tree.pack_forget()
    tree_frame.place_forget()
    login_frame.place(width=1500, height=2000)


resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\logout.png")
logout_img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\logout.png")
logout_btn = ttb.Button(
    tab, text='Logout', command=admin_logout, image=logout_img, compound=RIGHT, bootstyle='danger-outline')
logout_btn.place(x=1260, y=10, height=40)

data = db.execute('''SELECT * from Sheet1''')

cols = [i[0] for i in data.description]

tree['columns'] = cols[:6]
tree["show"] = "headings"

for col in tree["column"]:
    tree.heading(col, text=col)


for student in data:
    tree.insert("", "end", values=student)

# tree.pack()

# Profile page
profile = Frame(win)

roll_no = 0


def display_profile(id):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    #fdata = cur.execute('SELECT * FROM bill WHERE Rollno = ?', (id,))
    data = db.execute('''SELECT * from Sheet1 Where Rollno = ?''', (id,))
    j = 0
    b = 0
    for col in data.description[:12]:
        l = Label(profile, width=20, text=col[0])
        l.grid(row=b, column=0, padx=50, pady=5, sticky='nsew')
        b += 1
    c = 0
    for col in data.description[12:]:
        l = Label(profile, width=20, text=col[0])
        l.grid(row=c, column=4, padx=50, pady=5, sticky='nsew')
        c += 1
    for i in data:
        for k in range(len(i)):
            if k == 0:
                index_ent = ttb.Entry(profile, width=60)
                index_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                index_ent.insert(END, i[k])
            if k == 1:
                roll_ent = ttb.Entry(profile, width=60)
                roll_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                roll_ent.insert(END, i[k])
                rollnum = i[k]
                roll_no = i[k]
            if k == 2:
                name_ent = ttb.Entry(profile, width=60)
                name_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                name_ent.insert(END, i[k])
                name = i[k]
            if k == 3:
                reg_ent = ttb.Entry(profile, width=60)
                reg_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                reg_ent.insert(END, i[k])
            if k == 4:
                year_ent = ttb.Entry(profile, width=60)
                year_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                year_ent.insert(END, i[k])
                year = i[k]
            if k == 5:
                dept_ent = ttb.Entry(profile, width=60)
                dept_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                dept_ent.insert(END, i[k])
                dept = i[k]
            if k == 6:
                py_ent = ttb.Entry(profile, width=60)
                py_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                py_ent.insert(END, i[k])
                pyb = i[k]
            if k == 7:
                ad_ent = ttb.Entry(profile, width=60)
                ad_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                ad_ent.insert(END, i[k])
                adfee = i[k]
            if k == 8:
                tu_ent = ttb.Entry(profile, width=60)
                tu_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                tu_ent.insert(END, i[k])
                tufee = i[k]
            if k == 9:
                bus_ent = ttb.Entry(profile, width=60)
                bus_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                bus_ent.insert(END, i[k])
                busfee = i[k]
            if k == 10:
                hos_ent = ttb.Entry(profile, width=60)
                hos_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                hos_ent.insert(END, i[k])
                hosfee = i[k]
            if k == 11:
                tot_ent = ttb.Entry(profile, width=60)
                tot_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                tot_ent.insert(END, i[k])
                totfee = i[k]
            if k == 12:
                fgg_ent = ttb.Entry(profile, width=60)
                fgg_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                fgg_ent.insert(END, i[k])
                fgg = i[k]
            if k == 13:
                pmss_ent = ttb.Entry(profile, width=60)
                pmss_ent.grid(row=j-12, column=8, padx=5,
                              pady=5, sticky='nsew')
                pmss_ent.insert(END, i[k])
                pmss = i[k]
            if k == 14:
                gov_ent = ttb.Entry(profile, width=60)
                gov_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                gov_ent.insert(END, i[k])
                gov = i[k]
            if k == 15:
                other_ent = ttb.Entry(profile, width=60)
                other_ent.grid(row=j-12, column=8, padx=5,
                               pady=5, sticky='nsew')
                other_ent.insert(END, i[k])
                other = i[k]
            if k == 16:
                ket_ent = ttb.Entry(profile, width=60)
                ket_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                ket_ent.insert(END, i[k])
                ket = i[k]
            if k == 17:
                pay_ent = ttb.Entry(profile, width=60)
                pay_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                pay_ent.insert(END, i[k])
                pay = i[k]
            if k == 18:
                sctot_ent = ttb.Entry(profile, width=60)
                sctot_ent.grid(row=j-12, column=8, padx=5,
                               pady=5, sticky='nsew')
                sctot_ent.insert(END, i[k])
                sctot = i[k]
            if k == 19:
                rem_ent = ttb.Entry(profile, width=60)
                rem_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                rem_ent.insert(END, i[k])
                rem = i[k]
            if k == 20:
                paid_ent = ttb.Entry(profile, width=60)
                paid_ent.grid(row=j-12, column=8, padx=5,
                              pady=5, sticky='nsew')
                paid_ent.insert(END, i[k])
                paid = i[k]
            if k == 21:
                bal_ent = ttb.Entry(profile, width=60)
                bal_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                bal_ent.insert(END, i[k])
                bal = i[k]
            if k == 22:
                totf_ent = ttb.Entry(profile, width=60)
                totf_ent.grid(row=j-12, column=8, padx=5,
                              pady=5, sticky='nsew')
                totf_ent.insert(END, i[k])
                totfpaid = i[k]
            if k == 23:
                cbal_ent = ttb.Entry(profile, width=60)
                cbal_ent.grid(row=j-12, column=8, padx=5,
                              pady=5, sticky='nsew')
                cbal_ent.insert(END, i[k])
                cbal = i[k]
            j += 1

    def submit_record():
        rollno = roll_ent.get()
        data = (roll_ent.get(), name_ent.get(), reg_ent.get(), year_ent.get(), dept_ent.get(), py_ent.get(), ad_ent.get(), tu_ent.get(), bus_ent.get(), hos_ent.get(), tot_ent.get(),
                fgg_ent.get(), pmss_ent.get(), gov_ent.get(), other_ent.get(), ket_ent.get(), pay_ent.get(), sctot_ent.get(), rem_ent.get(), paid_ent.get(), bal_ent.get(), totf_ent.get(), cbal_ent.get(), rollno)
        query = db.execute("UPDATE Sheet1 SET Rollno=?,Name=?,Regno=?,Year=?,Department=?,Previous_Year_Balance=?,Admission_Fees=?,Tuition_Fees=?,Bus_Fees=?,Hostel_Fees=?,Total_Fees=?,FGG=?,PMSS=?,Govt_Quota=?,Other_Scholarships=?,KET_Scholarship=?,Student_To_pay=?,Scholarship_Total=?,Remaining_Fees=?,Fees_Paid=?,Balance=?,Total_Fees_Paid=?,Current_Balance=? Where Rollno=?", data)
        db.commit()
        q = db.execute("SELECT * FROM Sheet1")
        messagebox.showinfo('Success', "Data updated Successfully")

    resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\circular.png")
    update_img1 = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\circular.png")
    sub_btn = ttb.Button(
        win, text="Update    ", bootstyle='success-outline', image=update_img1, compound=RIGHT, command=submit_record)
    sub_btn.image = update_img1
    sub_btn.place(x=600, y=500)

    bill_frame = ScrolledFrame(win)

    def bill_details():
        Getpdf.place_forget()
        sub_btn.place_forget()
        profile.pack_forget()
        back.place_forget()
        tab.place_forget()
        det_btn.place_forget()
        bill_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)

        data = db.execute(
            '''SELECT * from Bill Where Rollno = ?''', (roll_no,))
        j = 3
        li = []
        lis = []

        for i in data:
            for k in range(1, len(i)):
                e = ttb.Entry(bill_frame, width=60)
                e.grid(row=j, column=k+1, padx=5, pady=5, sticky='nsew')
                e.insert(END, i[k])
                lis.append(e)
            li.append(lis)
            lis = []
            j += 1

        def back_bill():
            bill_frame.pack_forget()
            display_profile(roll_no)
            profile.pack(pady=30)

        resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\previous.png")
        previous_img1 = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\previous.png")
        back_bill = ttb.Button(
            bill_frame, text="Back", bootstyle='danger-outline', image=previous_img1, compound=LEFT, command=back_bill)
        back.image = previous_img1
        back_bill.grid(row=0, column=1, sticky='')
        back_bill.grid_columnconfigure((0, 1, 2), weight=1)

        def update_bill():

            db = sqlite3.connect('data.db')

            for i in li:
                billno = i[0].get()
                date = i[1].get()
                amount = i[2].get()
                print("billno:", billno, "date:", date, "amount:", amount)
                d = (roll_no, billno, date, amount, billno)
                print("d:", d)
                db.execute(
                    "UPDATE Bill SET rollno=?,billno=?,date=?,amount=? WHERE billno=?", d)
                db.commit()
        resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\circular.png")
        update_img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\circular.png")
        update_bill = ttb.Button(
            bill_frame, text="Update   ", bootstyle='success-outline', image=update_img, compound=RIGHT, command=update_bill)
        update_bill.image = update_img
        if len(li) > 0:

            billno_label = ttb.Label(
                bill_frame, text='    Bill No:', bootstyle='dark', font=('Arial', 15))
            billno_label.grid(row=1, column=2, sticky='nsew')

            date_label = ttb.Label(bill_frame, text='    Date:',
                                   bootstyle='dark', font=('Arial', 15))
            date_label.grid(row=1, column=3, sticky='nsew')

            amount_label = ttb.Label(bill_frame, text='    Amount:',
                                     bootstyle='dark', font=('Arial', 15))
            amount_label.grid(row=1, column=4, sticky='nsew')
            update_bill.grid(row=j+5, column=4)
        else:
            info_label = Label(bill_frame, text="No Bills")
            info_label.grid(row=3, column=2)

    resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\report.png")
    det_img1 = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\report.png")
    det_btn = ttb.Button(
        win, text="Bill Details   ", command=bill_details, image=det_img1, compound=RIGHT, bootstyle='warning')
    det_btn.image = det_img1
    det_btn.place(x=1000, y=500)

    def getpdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.image(r'images/header_word1.jpg', w=190)
        pdf.cell(200, 40, txt="FEES INFO", ln=1, align='C')

        pdf.cell(180, 20, txt=f"Rollno : {rollnum}", border=1, ln=2, align='L')
        pdf.cell(180, 20, txt=f"Name : {name}", border=1, ln=2, align='L')
        pdf.cell(180, 20, txt=f"Year : {year}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Department : {dept}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Previous Year Balance : {pyb}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Admission Fees         : {adfee}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Tution Fees            : {tufee}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Bus Fees               : {busfee}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Hostel Fees            : {hosfee}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Total Fees             : {totfee}", border=1, ln=2, align='L')

        pdf.cell(200, 40, txt="SCHOLARSHIP INFO", ln=1, align='C')

        pdf.cell(
            180, 20, txt=f"FGG                    : {fgg}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"PMSS                   : {pmss}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"7.5% GQ                : {gov}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Other scholarships     : {other}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"KET Scholarship        : {ket}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Student to Pay         : {pay}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Scholarship Total      : {sctot}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Remaining Fees         : {rem}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Fees Paid              : {paid}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Balance                : {bal}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Total Fees Paid        : {totfpaid}", border=1, ln=2, align='L')
        pdf.cell(
            180, 20, txt=f"Current Balance        : {cbal}", border=1, ln=2, align='L')

        roll = roll_ent.get()
        pdf.output(roll+".pdf")
        messagebox.showinfo('Success', 'Report Successfully saved')

    resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\download (1).png")
    pdf_img1 = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\download (1).png")
    Getpdf = ttb.Button(
        win, text="Get Pdf    ", bootstyle='success', image=pdf_img1, compound=RIGHT, command=getpdf)
    Getpdf.image = pdf_img1
    Getpdf.place(x=800, y=500)

    def back():
        tab.place(width=1600, height=200)
        back.place_forget()
        det_btn.place_forget()
        Getpdf.place_forget()
        sub_btn.place_forget()
        profile.pack_forget()
        # db.close()
        # profile.pack_forget()
        tree_frame.place(x=50, y=80)
        # tab.place()

    resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\previous.png")
    previous_img2 = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\previous.png")
    back = ttb.Button(
        win, text="Back", bootstyle='danger-outline', image=previous_img2, compound=LEFT, command=back)
    back.image = previous_img2
    back.place(x=40, y=10)


def select_record(e):
    selected = tree.focus()
    values = tree.item(selected, 'values')
    tree_frame.place_forget()
    tab.place_forget()
    display_profile(values[1])
    profile.pack(pady=30)


tree.bind("<Double-1>", select_record)

# cashier

cashier = Frame(win)

con = sqlite3.connect("data.db")


def cashier_logout():
    cashier.place_forget()
    login_frame.place(width=1500, height=2000)


resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\logout.png")
cas_logout_img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\logout.png")
cashier_logout_btn = ttb.Button(
    cashier, text='Log out', bootstyle='danger-outline', image=cas_logout_img, compound=RIGHT, command=cashier_logout)
cashier_logout_btn.place(x=1255, y=10)


dep_val = StringVar(cashier)
deptdrop = ttk.OptionMenu(
    cashier, dep_val, "Select Department", "CSE", "ECE", "EEE", "MECH", "CIVIL")
deptdrop.place(x=350, y=10, height=40)

year_val = StringVar(cashier)
yeardrop = ttk.OptionMenu(
    cashier, year_val, "Select year", "1 Year", "2 Year", "3 Year", "4 Year")
yeardrop.place(x=510, y=10, height=40)


def ccpdf():
    deptname = dep_val.get()
    print(deptname)
    yearval = year_val.get()[0]
    print(yearval)
    datas = db.execute(
        "SELECT * FROM Sheet1 Where Department=? AND Year=?", (deptname, yearval))
    pdf = FPDF()
    pdf.add_page()
    pdf.image(r'images/header_word1.jpg', w=190)
    for row in datas:
        pdf.set_font("Arial", size=20, style="BI")
        pdf.set_text_color(7, 145, 134)
        pdf.cell(200, 40, txt=f"NAME     :  {row[2]}", ln=1, align='C')
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)

        pdf.cell(
            180, 10, txt=f"Rollno                 : {row[1]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Year                   : {row[4]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Department             : {row[5]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Previous Year Balance  : {row[6]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Admission Fees         : {row[7]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Tution Fees            : {row[8]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Bus Fees               : {row[9]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Hostel Fees            : {row[10]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Total Fees             : {row[11]}", border=1, ln=2, align='L')

        pdf.cell(200, 30, txt="SCHOLARSHIP INFO", ln=1, align='C')

        pdf.cell(
            180, 10, txt=f"FGG                    : {row[12]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"PMSS                   : {row[13]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"7.5% GQ                : {row[14]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Other scholarships     : {row[15]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"KET Scholarship        : {row[16]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Student to Pay         : {row[17]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Scholarship Total      : {row[18]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Remaining Fees         : {row[19]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Fees Paid              : {row[20]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Balance                : {row[21]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Total Fees Paid        : {row[22]}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Current Balance        : {row[23]}", border=1, ln=2, align='L')

    pdf.output(yearval+"year"+"_"+deptname+".pdf")
    messagebox.showinfo("Success", "Report successfully saved")


resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\download (1).png")
pdf_img2 = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\download (1).png")
cpdf = ttb.Button(cashier, text='Get Pdf    ', image=pdf_img2,
                  compound=RIGHT, bootstyle='warning', command=ccpdf)
cpdf.place(x=655, y=10)

head = Label(cashier, text='Billing System', font=('Arial', 30))
head.place(x=540, y=100)


roll_label = Label(cashier, text='Roll No:')
roll_label.place(x=420, y=180)
roll = ttb.Entry(cashier,  width=60)
roll.focus_set()
roll.place(x=530, y=180, height=40)


billno_label = Label(cashier, text="Bill No:")
billno_label.place(x=420, y=230)
billno = ttb.Entry(cashier,  width=60)
billno.place(x=530, y=230, height=40)

date_val = StringVar(cashier)
date_label = Label(cashier, text="Date:")
date_label.place(x=420, y=280)
date_ent = ttb.DateEntry(cashier,  width=60)
date_ent.place(x=530, y=280, height=40)

amount_label = Label(cashier, text="Amount")
amount_label.place(x=420, y=320)
amount = ttb.Entry(cashier,  width=60)
amount.place(x=530, y=320, height=40)


def submit():
    con.execute(
        '''CREATE TABLE IF NOT EXISTS bill (rollno int,billno int,date date,amount int)''')
    rollno_ = roll.get()
    billno_ = billno.get()
    amount_ = amount.get()
    date_ = date_ent.entry.get()
    con.execute('''INSERT INTO bill VALUES(?,?,?,?)''',
                (rollno_, billno_, date_, amount_,))
    con.commit()
    a = db.execute('SELECT * FROM Sheet1 where rollno=?', (rollno_,))
    bal = 0
    tot = 0
    cbal = 0
    to_pay = 0
    totf = 0
    for i in a:
        totf += i[11]
        to_pay += i[17]
        bal += i[21]
        tot += i[22]
        cbal += i[23]

    print("cbal", cbal, "tot", tot, "to_pay", to_pay, "totf", totf, "bal", bal)
    bal = int(to_pay)-int(amount_)
    tot += int(amount_)
    cbal = cbal-int(amount_)
    db.execute("UPDATE Sheet1 SET balance=?,Total_Fees_paid=?,Current_Balance=? WHERE rollno=?",
               (bal, tot, cbal, rollno_))
    db.commit()

    con.commit()
    w = ttb.Window(themename="litera")
    w.geometry('300x300')
    rollno_ = 'Roll No: '+rollno_
    billno_ = "Bill No: "+billno_
    amount_ = "Amount: "+amount_
    a_label = Label(w, text=rollno_)
    a_label.place(x=20, y=20)
    b_label = Label(w, text=billno_)
    b_label.place(x=20, y=70)
    c_label = Label(w, text=amount_)
    c_label.place(x=20, y=120)

    def print_bill():
        now = datetime.datetime.now()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=20, style="BI")
        pdf.set_text_color(7, 145, 134)
        pdf.image(r'images/header_word1.jpg', w=190)
        pdf.cell(200, 40, txt=f"{billno_}", ln=1, align='C')
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)

        pdf.cell(
            180, 10, txt=f"{rollno_}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"{billno_}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Date: {date_}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"{amount_}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Balance amount to be paid by student: {cbal}", border=1, ln=2, align='L')
        pdf.cell(
            180, 10, txt=f"Total Bill paid: {tot}", border=1, ln=2, align='L')
        n = roll.get()+"_"+billno.get()+"_"+'.pdf'
        pdf.output(n)

        # with io.open(n) as file:
        #    if file:
        #        win32api.ShellExecute(0, "print", file, None, ".", 0)
    btn = ttb.Button(w, text='print', bootstyle='danger', command=print_bill)
    btn.place(x=50, y=170)
    w.geometry('300x300')
    w.mainloop()


resize_img(r"C:\Users\Admin\Documents\python\projects\feemanagement\images\upload.png")
upload_img = PhotoImage(file=r"C:\Users\Admin\Documents\python\projects\feemanagement\images\upload.png")
submit_btn = ttb.Button(cashier, text='Submit   ',
                        image=upload_img, compound=RIGHT, bootstyle='primary-outline', command=submit)
submit_btn.place(x=690, y=390, height=40)


win.mainloop()
