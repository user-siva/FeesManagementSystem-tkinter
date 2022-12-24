import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, filedialog
from tkinter.ttk import Treeview, Scrollbar
from PIL import Image, ImageTk
import numpy
import pandas as pd
import sqlite3
from fpdf import FPDF
import ast
import re
import datetime
import io
import win32api

ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")

win = ctk.CTk()

# w, h = win.winfo_screenwidth(), win.winfo_screenheight()
# win.geometry("%dx%d+0+0" % (w, h))
win.state("zoomed")

login_frame = Frame(win)
login_frame.place(width=1500, height=2000)

img = Image.open('coins.jpeg')

img1 = ImageTk.PhotoImage(img)
limg = Label(login_frame, image=img1)
limg.image = img1
limg.place(x=0, y=0)


def login():
    uname = username_ent.get()
    pwd = password_ent.get()

    if uname == '' or pwd == '':
        messagebox.showerror("fill the empty field")
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
                # tree_frame.place(x=50, y=60)
                cashier.place(width=900, height=900)
            elif data[3] == 1:
                login_frame.place_forget()
                tab.place(width=1600, height=50)
                tree.pack()
                tree_frame.place(x=50, y=60)

        else:
            print("Wrong")


def open_register():
    login_frame.place_forget()
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    """image = Image.open("register.jpeg")

    # Resize the image using resize() method
    resize_image = image.resize((300, 350))

    img = ImageTk.PhotoImage(resize_image)

    Label(win,image=img,border=0,bg='white').place(x=50,y=90)"""

    frame = Frame(win, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white',
                    font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

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

    user = Entry(frame, width=25, fg="black", borderwidth=0,
                 highlightthickness=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    nametic = Label(frame, text='', bg='white')
    nametic.place(x=300, y=80)

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

    mail = Entry(frame, width=25, fg="black", borderwidth=0,
                 highlightthickness=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    mail.place(x=30, y=150)
    mailtic = Label(frame, text='', bg='white')
    mailtic.place(x=300, y=150)

    mail.insert(0, 'Mail Id')
    mail.bind("<FocusIn>", on_enter)
    mail.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

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

    password = Entry(frame, width=25, fg="black", borderwidth=0,
                     highlightthickness=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    password.place(x=30, y=220)
    passtic = Label(frame, text='', bg='white')
    passtic.place(x=300, y=220)

    password.insert(0, 'Password')
    password.bind("<FocusIn>", on_enter)
    # password.bind("<FocusOut>",on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

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

    cpass = Entry(frame, width=25, fg="black", borderwidth=0,
                  highlightthickness=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    cpass.place(x=30, y=290)
    cpasstic = Label(frame, text='', bg='white')
    cpasstic.place(x=300, y=290)

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

    submit = ctk.CTkButton(frame, text='SignUp', bg='#2effff', command=store)
    submit.place(x=30, y=350)


head = Label(login_frame, text='Login', font=('Arial', 30), fg='blue')
head.place(x=1100, y=160)
user_label1 = Label(login_frame, text='Username:', font=(
    'Arial', 20), fg='green').place(x=1000, y=220)
username_ent = Entry(login_frame, width=15, font=('Arial', 15), borderwidth=1,
                     highlightthickness=0, bg='white', highlightbackground='green')
username_ent.place(x=1150, y=230)

pass_label1 = Label(login_frame, text='Password:', font=(
    'Arial', 20), fg='green').place(x=1000, y=270)
password_ent = Entry(login_frame, borderwidth=1, highlightthickness=0,
                     bg='white', width=15, font=('Arial', 15), show='*')
password_ent.place(x=1150, y=280)

register_button = Button(login_frame, text='Register', width=10, fg='red', bd=1, font=(
    'Arial', 15), command=open_register).place(x=1010, y=330, height=40)
submit_button = Button(login_frame, text='Submit', width=10, fg='blue', bd=1, font=(
    'Arial', 15), command=login).place(x=1180, y=330, height=40)

tab = Frame(win)
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


search_entry = ctk.CTkEntry(tab, width=250)
search_entry.place(x=880, y=10)

search_btn = ctk.CTkButton(tab, text='Search', command=search, width=100)
search_btn.place(x=1145, y=10)

tree_frame = Frame(win)
# tree_frame.place(x=50, y=60)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=BOTH)

tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scroll.set, height=30, selectmode="extended")
# tree.pack()

tree_scroll.config(command=tree.yview)


# db = sqlite3.connect('script.db')
db = sqlite3.connect('data.db')

# TreeView


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


deptdrop = ctk.CTkOptionMenu(
    tab, values=["CSE", "ECE", "EEE", "MECH", "CIVIL"])
deptdrop.place(x=350, y=10)
deptdrop.set("select a Department")

yeardrop = ctk.CTkOptionMenu(
    tab, values=["1 Year", "2 Year", "3 Year", "4 Year"])
yeardrop.place(x=510, y=10)
yeardrop.set("select a year")


def cpdf():
    deptname = deptdrop.get()
    yearval = yeardrop.get()[0]

    datas = db.execute(
        "SELECT * FROM Sheet1 Where Department=? AND Year=?", (deptname, yearval))
    pdf = FPDF()
    pdf.add_page()
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


cpdf = ctk.CTkButton(tab, text='GetPdf', command=cpdf)
cpdf.place(x=655, y=10)


import_btn = ctk.CTkButton(
    tab, bg='red', text='Import Data', command=import_data)
import_btn.place(x=50, y=10)


def backup():
    conn = sqlite3.connect('data.db')
    with io.open('fee_details_backup.sql', 'w') as p:

        for line in conn.iterdump():

            p.write('%s\n' % line)
    print(' Backup performed successfully!')
    print(' Data Saved as backupdatabase_dump.sql')

    conn.close()


backup_btn = ctk.CTkButton(
    tab, bg='red', text='Backup', command=backup, width=100)
backup_btn.place(x=1260, y=10)

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
        l = ctk.CTkLabel(profile, width=100, text=col[0], fg='blue')
        l.grid(row=b, column=0, padx=50, pady=5, sticky='nsew')
        b += 1
    c = 0
    for col in data.description[12:]:
        l = ctk.CTkLabel(profile, width=100, text=col[0], fg='blue')
        l.grid(row=c, column=4, padx=50, pady=5, sticky='nsew')
        c += 1
    for i in data:
        for k in range(len(i)):
            if k == 0:
                index_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                index_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                index_ent.insert(END, i[k])
            if k == 1:
                roll_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                roll_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                roll_ent.insert(END, i[k])
                rollnum = i[k]
                roll_no = i[k]
            if k == 2:
                name_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                name_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                name_ent.insert(END, i[k])
                name = i[k]
            if k == 3:
                reg_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                reg_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                reg_ent.insert(END, i[k])
            if k == 4:
                year_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                year_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                year_ent.insert(END, i[k])
                year = i[k]
            if k == 5:
                dept_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                dept_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                dept_ent.insert(END, i[k])
                dept = i[k]
            if k == 6:
                py_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                py_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                py_ent.insert(END, i[k])
                pyb = i[k]
            if k == 7:
                ad_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                ad_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                ad_ent.insert(END, i[k])
                adfee = i[k]
            if k == 8:
                tu_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                tu_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                tu_ent.insert(END, i[k])
                tufee = i[k]
            if k == 9:
                bus_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                bus_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                bus_ent.insert(END, i[k])
                busfee = i[k]
            if k == 10:
                hos_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                hos_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                hos_ent.insert(END, i[k])
                hosfee = i[k]
            if k == 11:
                tot_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                tot_ent.grid(row=j, column=1, padx=5, pady=5, sticky='nsew')
                tot_ent.insert(END, i[k])
                totfee = i[k]
            if k == 12:
                fgg_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                fgg_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                fgg_ent.insert(END, i[k])
                fgg = i[k]
            if k == 13:
                pmss_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                pmss_ent.grid(row=j-12, column=8, padx=5,
                              pady=5, sticky='nsew')
                pmss_ent.insert(END, i[k])
                pmss = i[k]
            if k == 14:
                gov_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                gov_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                gov_ent.insert(END, i[k])
                gov = i[k]
            if k == 15:
                other_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                other_ent.grid(row=j-12, column=8, padx=5,
                               pady=5, sticky='nsew')
                other_ent.insert(END, i[k])
                other = i[k]
            if k == 16:
                ket_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                ket_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                ket_ent.insert(END, i[k])
                ket = i[k]
            if k == 17:
                pay_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                pay_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                pay_ent.insert(END, i[k])
                pay = i[k]
            if k == 18:
                sctot_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                sctot_ent.grid(row=j-12, column=8, padx=5,
                               pady=5, sticky='nsew')
                sctot_ent.insert(END, i[k])
                sctot = i[k]
            if k == 19:
                rem_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                rem_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                rem_ent.insert(END, i[k])
                rem = i[k]
            if k == 20:
                paid_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                paid_ent.grid(row=j-12, column=8, padx=5,
                              pady=5, sticky='nsew')
                paid_ent.insert(END, i[k])
                paid = i[k]
            if k == 21:
                bal_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                bal_ent.grid(row=j-12, column=8, padx=5, pady=5, sticky='nsew')
                bal_ent.insert(END, i[k])
                bal = i[k]
            if k == 22:
                totf_ent = ctk.CTkEntry(profile, width=400, fg='blue')
                totf_ent.grid(row=j-12, column=8, padx=5,
                              pady=5, sticky='nsew')
                totf_ent.insert(END, i[k])
                totfpaid = i[k]
            if k == 23:
                cbal_ent = ctk.CTkEntry(profile, width=400, fg='blue')
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
    sub_btn = ctk.CTkButton(
        win, text="Update", command=submit_record)
    sub_btn.place(x=600, y=500)

    bill_frame = Frame(win)

    def bill_details():
        data = db.execute(
            '''SELECT * from Bill Where Rollno = ?''', (roll_no,))
        j = 3
        li = []
        lis = []
        dis = {}
        for i in data:
            for k in range(1, len(i)):
                e = ctk.CTkEntry(bill_frame, width=400, fg='blue')
                e.grid(row=j, column=k, padx=5, pady=5, sticky='nsew')
                e.insert(END, i[k])
                lis.append(e.get())
            j += 1
        li.append(lis)

        print("lis:", li)

        def back_bill():
            bill_frame.pack_forget()
            display_profile(roll_no)
            profile.pack(pady=30)

        back_bill = ctk.CTkButton(
            bill_frame, pady=20, text="Back", command=back_bill)
        back_bill.grid(row=0, column=1)

        def update_bill():
            db = sqlite3.connect('data.db')
            data = db.execute(
                'SELECT * from Bill Where Rollno = ?', (roll_no,))
            d = None
            j = 0
            for i in data:
                billno = i[1]
                d = db.execute('SELECT * FROM bill WHERE billno=?', (billno,))
                print("billno", billno)
                # print(li[i])
                # print(li[j][0].get())
                j += 1

        update_bill = ctk.CTkButton(
            bill_frame, pady=20, text="Update", command=update_bill)
        update_bill.grid(row=10, column=3)

        bill_frame.pack()
        Getpdf.place_forget()
        sub_btn.place_forget()
        profile.pack_forget()
        back.place_forget()
        tab.place_forget()
        det_btn.place_forget()

    det_btn = ctk.CTkButton(
        win, text="Bill Details", command=bill_details)
    det_btn.place(x=1000, y=500)

    def getpdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)

        pdf.cell(200, 40, txt="FEES INFO", ln=1, align='C')

        pdf.cell(200, 20, txt=f"Rollno : {rollnum}", border=1, ln=2, align='L')
        pdf.cell(200, 20, txt=f"Name : {name}", border=1, ln=2, align='L')
        pdf.cell(200, 20, txt=f"Year : {year}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Department : {dept}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Previous Year Balance : {pyb}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Admission Fees         : {adfee}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Tution Fees            : {tufee}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Bus Fees               : {busfee}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Hostel Fees            : {hosfee}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Total Fees             : {totfee}", border=1, ln=2, align='L')

        pdf.cell(200, 40, txt="SCHOLARSHIP INFO", ln=1, align='C')

        pdf.cell(
            200, 20, txt=f"FGG                    : {fgg}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"PMSS                   : {pmss}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"7.5% GQ                : {gov}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Other scholarships     : {other}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"KET Scholarship        : {ket}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Student to Pay         : {pay}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Scholarship Total      : {sctot}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Remaining Fees         : {rem}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Fees Paid              : {paid}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Balance                : {bal}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Total Fees Paid        : {totfpaid}", border=1, ln=2, align='L')
        pdf.cell(
            200, 20, txt=f"Current Balance        : {cbal}", border=1, ln=2, align='L')

        roll = roll_ent.get()
        pdf.output(roll+".pdf")
        messagebox.showinfo('Success', 'Report Successfully saved')
    Getpdf = ctk.CTkButton(
        win, text="Get Pdf", command=getpdf)
    Getpdf.place(x=800, y=500)

    def back():
        tab.place(width=1600, height=50)
        back.place_forget()
        Getpdf.place_forget()
        sub_btn.place_forget()
        profile.pack_forget()
        # db.close()
        # profile.pack_forget()
        tree_frame.place(x=50, y=60)
        # tab.place()

    back = ctk.CTkButton(
        win, text="Back", command=back)
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


deptdrop = ctk.CTkOptionMenu(
    cashier, values=["CSE", "ECE", "EEE", "MECH", "CIVIL"])
deptdrop.place(x=350, y=10)
deptdrop.set("select a Department")

yeardrop = ctk.CTkOptionMenu(
    cashier, values=["1 Year", "2 Year", "3 Year", "4 Year"])
yeardrop.place(x=510, y=10)
yeardrop.set("select a year")


def ccpdf():
    deptname = deptdrop.get()
    yearval = yeardrop.get()[0]

    datas = db.execute(
        "SELECT * FROM Sheet1 Where Department=? AND Year=?", (deptname, yearval))
    pdf = FPDF()
    pdf.add_page()
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


cpdf = ctk.CTkButton(cashier, text='GetPdf', command=ccpdf)
cpdf.place(x=655, y=10)

head = Label(cashier, text='Billing System', font=('Courier', 23))
head.place(x=540, y=100)


roll_label = ctk.CTkLabel(cashier, text='Roll No')
roll_label.place(x=420, y=180)
roll = ctk.CTkEntry(cashier, border=0, width=300)
roll.place(x=530, y=180, height=25)


billno_label = ctk.CTkLabel(cashier, text="Bill No")
billno_label.place(x=420, y=230)
billno = ctk.CTkEntry(cashier, border=0, width=300)
billno.place(x=530, y=230, height=25)

amount_label = ctk.CTkLabel(cashier, text="Amount")
amount_label.place(x=420, y=280)
amount = ctk.CTkEntry(cashier, border=0, width=300)
amount.place(x=530, y=280, height=25)


def submit():
    con.execute(
        '''CREATE TABLE IF NOT EXISTS bill (rollno int,billno int,date date,amount int)''')
    rollno_ = roll.get()
    billno_ = billno.get()
    amount_ = amount.get()
    # tkinter.messagebox.showinfo('Print',rollno_)
    x = datetime.datetime.now()
    date_ = x.strftime("%x").replace('/', '.')
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
    cbal = int(tot)-cbal
    db.execute("UPDATE Sheet1 SET balance=?,Total_Fees_paid=?,Current_Balance=? WHERE rollno=?",
               (bal, tot, cbal, rollno_))
    b = db.execute('SELECT * FROM Sheet1 where rollno=?', (rollno_,))
    for i in b:
        print(i)
    res = con.execute('''SELECT * FROM bill''')
    for i in res:
        r = i[0]
        print(i)
    con.commit()
    con.close()
    w = Tk()
    w.geometry('300x300')
    rollno_ = 'Roll No: '+rollno_
    billno_ = "Bill No: "+billno_
    amount_ = "Amount: "+amount_
    a_label = ctk.CTkLabel(w, text=rollno_)
    a_label.place(x=20, y=20)
    b_label = ctk.CTkLabel(w, text=billno_)
    b_label.place(x=20, y=70)
    c_label = ctk.CTkLabel(w, text=amount_)
    c_label.place(x=20, y=120)

    def print_bill():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=20, style="BI")
        pdf.set_text_color(7, 145, 134)
        pdf.cell(200, 40, txt=f"Bill :  {billno_}", ln=1, align='C')
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)

        pdf.cell(
            200, 10, txt=f"Roll No                 : {rollno_}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Bill No                 : {billno_}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Date                : {date_}", border=1, ln=2, align='L')
        pdf.cell(
            200, 10, txt=f"Amount                 : {amount_}", border=1, ln=2, align='L')
        n = roll.get()+"_"+billno.get()+"_"+'.pdf'
        pdf.output(n)
        print(n)
        with io.open(n) as file:
            if file:
                win32api.ShellExecute(0, "print", file, None, ".", 0)
    btn = ctk.CTkButton(w, text='print', command=print_bill)
    btn.place(x=50, y=170)
    w.geometry('300x300')
    w.mainloop()


submit_btn = ctk.CTkButton(cashier, text='Submit', command=submit)
submit_btn.place(x=690, y=340, height=30)


win.mainloop()
