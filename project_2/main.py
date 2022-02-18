# First - Create GUI for inputting Students Data
# Second - Storing the Data in DB
# Third - To generate a PDF and put Data from DB on that PDF

import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
import datetime
import pandas as pd
import certificate

win = tk.Tk()
win.geometry("1280x720+0+0")
win.title("Leaving Certificate")
title_label = tk.Label(win, font=("Ariel", 30, "bold"), text="Student's TC Generator",
                       border=12, relief=tk.GROOVE, bg="lightgrey")

tab = ttk.Notebook(win)
detail_frame_main = Frame(tab)
print_frame_main = Frame(tab)

tab.add(detail_frame_main, text="Students Data Entry")
tab.add(print_frame_main, text="Print TC")

detail_frame = tk.LabelFrame(detail_frame_main, font=("Ariel", 25),
                             text="Enter Student Details", border=10)
detail_frame.place(x=10, y=20, width=450, height=650)

data_frame = tk.LabelFrame(detail_frame_main, font=("Ariel", 25),
                           text="Data Frame", border=10)
data_frame.place(x=460, y=20, width=820, height=650)

print_frame = tk.LabelFrame(print_frame_main, font=("Ariel", 25), text="Generate TC", border=10, relief=tk.GROOVE,
                            bg="lightgrey")
print_frame.place(x=430, y=20, width=500, height=650)

tab.pack(expand=TRUE, fill="both")

# == Variables Start == #
register_no = tk.StringVar()
enrolment_no = tk.StringVar()
name = tk.StringVar()
mname = tk.StringVar()
lname = tk.StringVar()
mother_name = tk.StringVar()
caste = tk.StringVar()
place_of_birth = tk.StringVar()
dob = tk.StringVar()
date_w = tk.StringVar()
month = tk.StringVar()
year = tk.StringVar()
last_institute = tk.StringVar()
date_of_admission = tk.StringVar()
course_name = tk.StringVar()
search_by = tk.StringVar()

register_no_2 = tk.StringVar()
d_name = tk.StringVar()
d_enrol_no = tk.StringVar()
d_f_name = tk.StringVar()
d_m_name = tk.StringVar()
d_l_name = tk.StringVar()
p_progress = tk.StringVar()
p_conduct = tk.StringVar()
p_dol = tk.StringVar()
p_reason = tk.StringVar()
p_remark = tk.StringVar()


# == Variables Close == #

# == Functions Start == #
# ====Upper Case======#
def caps(event):
    pass


def caps_2(event):
    pass


# ====ClearPrint=====#
def clear_print(event):
    d_name.set("")
    d_enrol_no.set("")


# ======Convert Date=====#

def date_conv(event):
    pass


def date_conv_2(event):
    pass


# Create a data base
def create_fun():
    con = sqlite3.connect('studb')
    c = con.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS STU_DB(register_no VARCHAR NOT NULL CONSTRAINT table_name_pk PRIMARY KEY ON "
        "CONFLICT REPLACE, enrolment_no "
        "INT NOT NULL, name VARCHAR NOT NULL, mname VARCHAR NOT NULL, lname VARCHAR NOT NULL, mother_name VARCHAR NOT "
        "NULL, caste VARCHAR NOT NULL, place_of_birth VARCHAR NOT NULL, dob DATE NOT NULL, "
        "date_w NOT NULL, month VARCHAR NOT NULL, year VARCHAR NOT NULL, last_institute VARCHAR NOT NULL, "
        "date_of_admission DATE NOT NULL, course_name VARCHAR  NOT NULL)")
    c.execute(
        "CREATE TABLE IF NOT EXISTS STU_TC ( tc_no INTEGER NOT NULL CONSTRAINT STU_TC PRIMARY KEY AUTOINCREMENT, "
        "progress VARCHAR NOT NULL, conduct VARCHAR NOT NULL, dol DATE NOT NULL, reason VARCHAR NOT NULL, remark "
        "VARCHAR NOT NULL, register_no VARCHAR NOT NULL UNIQUE REFERENCES STU_DB)")
    con.commit()
    c.close()


# Fetch the data from data base
def fetch_data():
    con = sqlite3.connect('studb')
    c = con.cursor()
    c.execute("SELECT * FROM STU_DB")
    rows = c.fetchall()
    if len(rows) != 0:
        stu_table.delete(*stu_table.get_children())
        for row in rows:
            stu_table.insert('', tk.END, values=row)
    con.commit()
    c.close()


def get_name():
    rn = register_no_2.get()
    certificate.r_no(rn)
    con = sqlite3.connect('studb')
    c = con.cursor()
    x = register_no_2.get()
    c.execute("SELECT name FROM STU_DB WHERE register_no=?", [x])
    d_f_name = c.fetchone()
    c.execute("SELECT mname FROM STU_DB WHERE register_no=?", [x])
    d_m_name = c.fetchone()
    c.execute("SELECT lname FROM STU_DB WHERE register_no=?", [x])
    d_l_name = c.fetchone()
    c.execute("SELECT enrolment_no FROM STU_DB WHERE register_no=?", [x])
    d_enrolment_no = c.fetchone()
    display_name.insert(END, f'{d_f_name[0]} {d_m_name[0]} {d_l_name[0]}')
    display_enroll.insert(END, d_enrolment_no[0])
    con.commit()
    con.close()


def save_leaving_info():
    con = sqlite3.connect('studb')
    c = con.cursor()
    c.execute("INSERT INTO STU_TC (progress, conduct, dol, reason, remark, register_no) VALUES(?, ?, ?, ?, ?, ?)",
              (p_progress.get(), p_conduct.get(), p_dol.get(), p_reason.get(), p_remark.get(), register_no_2.get()))
    con.commit()
    c.close()


def add_fun():
    if register_no.get() == "" or enrolment_no.get() == "" or name.get() == "" or mname.get == "" or lname.get() == "" \
            or mother_name.get() == "" or caste.get() == "" or place_of_birth.get() == "" or dob.get() == "" \
            or date_w.get() == "" or month.get() == "" or year.get() == "" or last_institute.get() == "" \
            or date_of_admission.get() == "" or course_name.get() == "":
        messagebox.showerror("ERROR!", "All fields are Mandatory")
    else:
        con = sqlite3.connect('studb')
        c = con.cursor()
        c.execute("INSERT INTO STU_DB VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (register_no.get(), enrolment_no.get(), name.get(), mname.get(), lname.get(), mother_name.get(),
                   caste.get(), place_of_birth.get(),
                   dob.get(), date_w.get(), month.get(), year.get(), last_institute.get(), date_of_admission.get(),
                   course_name.get()))
        con.commit()
        fetch_data()
        c.close()


def get_cursor(event):
    cursor_row = stu_table.focus()
    content = stu_table.item(cursor_row)
    row = content['values']
    register_no.set(row[0])
    enrolment_no.set(row[1])
    name.set(row[2])
    mname.set(row[3])
    lname.set(row[4])
    mother_name.set(row[5])
    caste.set(row[6])
    place_of_birth.set(row[7])
    dob.set(row[8])
    date_w.set(row[9])
    month.set(row[10])
    year.set(row[11])
    last_institute.set(row[12])
    date_of_admission.set(row[13])
    course_name.set(row[14])


def clear():
    cursor_row = stu_table.focus()
    content = stu_table.item(cursor_row)
    row = content['values']
    register_no.set("")
    enrolment_no.set("")
    name.set("")
    mname.set("")
    lname.set("")
    mother_name.set("")
    caste.set("")
    place_of_birth.set("")
    dob.set("")
    date_w.set("")
    month.set("")
    year.set("")
    last_institute.set("")
    date_of_admission.set("")
    course_name.set("")
    register_no_2.set("")


def update_fun():
    con = sqlite3.connect('studb')
    c = con.cursor()
    c.execute(
        "UPDATE STU_DB SET register_no=?, enrolment_no=?, name=?, mname=?, lname=?, mother_name=?, caste=?, "
        "place_of_birth=?, dob=?,  date_w=?, month=?, year=?, last_institute=?, date_of_admission=?, course_name=? "
        "WHERE register_no=?",
        (register_no.get(), enrolment_no.get(), name.get(), mname.get(), lname.get(), mother_name.get(), caste.get(),
         place_of_birth.get(), dob.get(), date_w.get(), month.get(), year.get(),
         last_institute.get(), date_of_admission.get(), course_name.get(), register_no.get()))
    con.commit()
    fetch_data()
    c.close()
    clear()


def delete_fun():
    con = sqlite3.connect('studb')
    c = con.cursor()
    x = register_no.get()
    c.execute("DELETE FROM STU_DB WHERE register_no=?", [x])
    con.commit()
    c.close()
    fetch_data()
    clear()


def search_data():
    pass


# == Functions Close == #

# == Data Entry Start == #
# Register No.
register_no_lbl = tk.Label(detail_frame, text="Register No.", font=("Ariel", 10), bg="lightgrey")
register_no_lbl.grid(row=0, column=0, padx=2, pady=2)
register_no_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=register_no)
register_no_ent.grid(row=0, column=1, padx=2, pady=2)

# Enrolment No.
enrolment_no_lbl = tk.Label(detail_frame, text="Enrolment No.", font=("Ariel", 10), bg="lightgrey")
enrolment_no_lbl.grid(row=1, column=0, padx=2, pady=2)
enrolment_no_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=enrolment_no)
enrolment_no_ent.grid(row=1, column=1, padx=2, pady=2)

# Student's First Name
stu_name_lbl = tk.Label(detail_frame, text="First Name", font=("Ariel", 10), bg="lightgrey")
stu_name_lbl.grid(row=2, column=0, padx=2, pady=2)
stu_name_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=name)
stu_name_ent.grid(row=2, column=1, padx=2, pady=2)
stu_name_ent.bind("<KeyRelease>", caps)

# Student's Middle Name
stu_mname_lbl = tk.Label(detail_frame, text="Middle Name", font=("Ariel", 10), bg="lightgrey")
stu_mname_lbl.grid(row=3, column=0, padx=2, pady=2)
stu_mname_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=mname)
stu_mname_ent.grid(row=3, column=1, padx=2, pady=2)
stu_mname_ent.bind("<KeyRelease>", caps)

# Student's Last Name
stu_lname_lbl = tk.Label(detail_frame, text="Last Name", font=("Ariel", 10), bg="lightgrey")
stu_lname_lbl.grid(row=4, column=0, padx=2, pady=2)
stu_lname_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=lname)
stu_lname_ent.grid(row=4, column=1, padx=2, pady=2)
stu_lname_ent.bind("<KeyRelease>", caps)

# Student's Mother Name
stu_moname_lbl = tk.Label(detail_frame, text="Mother's Name", font=("Ariel", 10), bg="lightgrey")
stu_moname_lbl.grid(row=5, column=0, padx=2, pady=2)
stu_moname_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=mother_name)
stu_moname_ent.grid(row=5, column=1, padx=2, pady=2)
stu_moname_ent.bind("<KeyRelease>", caps)

# Caste
caste_lbl = tk.Label(detail_frame, text="Caste", font=("Ariel", 10), bg="lightgrey")
caste_lbl.grid(row=6, column=0, padx=2, pady=2)
caste_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=caste)
caste_ent.grid(row=6, column=1, padx=2, pady=2)
caste_ent.bind("<KeyRelease>", caps)

# Place of Birth
place_of_birth_lbl = tk.Label(detail_frame, text="Place of Birth", font=("Ariel", 10), bg="lightgrey")
place_of_birth_lbl.grid(row=7, column=0, padx=2, pady=2)
place_of_birth_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=place_of_birth)
place_of_birth_ent.grid(row=7, column=1, padx=2, pady=2)
place_of_birth_ent.bind("<KeyRelease>", caps)

# Date of Birth
dob_lbl = tk.Label(detail_frame, text="Date of Birth", font=("Ariel", 10), bg="lightgrey")
dob_lbl.grid(row=8, column=0, padx=2, pady=2)
dob_ent = DateEntry(detail_frame, width=29, background='blue', date_pattern='dd/mm/yyyy',
                    foreground='white', borderwidth=5, font=("Ariel", 10), textvariable=dob)
dob_ent.grid(row=8, column=1, padx=2, pady=2)
dob_ent.bind("<FocusOut>", date_conv)

# Date
dob_date_wo_lbl = tk.Label(detail_frame, text="Date of Birth (In Words)", font=("Ariel", 10), bg="lightgrey")
dob_date_wo_lbl.grid(row=9, column=0, padx=2, pady=2)
dob_date_wo_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=date_w)
dob_date_wo_ent.grid(row=9, column=1, padx=2, pady=2)
dob_date_wo_ent.bind("<KeyRelease>", caps)

# Month
dob_month_wo_lbl = tk.Label(detail_frame, text="Month of Birth (In Words)", font=("Ariel", 10), bg="lightgrey")
dob_month_wo_lbl.grid(row=10, column=0, padx=2, pady=2)
dob_month_wo_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=month)
dob_month_wo_ent.grid(row=10, column=1, padx=2, pady=2)
dob_month_wo_ent.bind("<KeyRelease>", caps)

# Year
dob_year_wo_lbl = tk.Label(detail_frame, text="Year of Birth (In Words)", font=("Ariel", 10), bg="lightgrey")
dob_year_wo_lbl.grid(row=11, column=0, padx=2, pady=2)
dob_year_wo_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=year)
dob_year_wo_ent.grid(row=11, column=1, padx=2, pady=2)
dob_year_wo_ent.bind("<KeyRelease>", caps)

# Last Institute
last_inst_lbl = tk.Label(detail_frame, text="Last Institute", font=("Ariel", 10), bg="lightgrey")
last_inst_lbl.grid(row=12, column=0, padx=2, pady=2)
last_inst_ent = tk.Entry(detail_frame, width=30, bd=5, font=("Ariel", 10), textvariable=last_institute)
last_inst_ent.grid(row=12, column=1, padx=2, pady=2)
last_inst_ent.bind("<KeyRelease>", caps)

# Date of Admission
date_admission_lbl = tk.Label(detail_frame, text="Date of Admission", font=("Ariel", 10), bg="lightgrey")
date_admission_lbl.grid(row=13, column=0, padx=2, pady=2)
date_admission_ent = DateEntry(detail_frame, width=29, background='blue', date_pattern='dd/mm/yyyy',
                               foreground='white', borderwidth=5, font=("Ariel", 10), textvariable=date_of_admission)
date_admission_ent.grid(row=13, column=1, padx=2, pady=2)
date_admission_ent.bind("<FocusOut>", date_conv)

# Course Name
course_lbl = tk.Label(detail_frame, text="Course Name", font=("Ariel", 10), bg="lightgrey")
course_lbl.grid(row=14, column=0, padx=2, pady=2)
course_ent = ttk.Combobox(detail_frame, font=("Ariel", 10), textvariable=course_name)
course_ent['values'] = ("CIVIL ENGINEERING",
                        "COMPUTER SCIENCE AND ENGINEERING",
                        "ELECTRONICS AND TELECOMMUNICATION",
                        "MECHANICAL ENGINEERING")
course_ent.config(width=29)
course_ent.grid(row=14, column=1, padx=2, pady=2)
course_ent.bind("<KeyRelease>", caps)
# == Data Entry Close == #

# ====PrintTC=====#
# Register No.
register_no_p_lbl = tk.Label(print_frame, text="Enter Register No.", font=("Ariel", 10), bg="lightgrey")
register_no_p_lbl.grid(row=0, column=0, padx=2, pady=2)
register_no_p_ent = tk.Entry(print_frame, width=30, bd=5, font=("Ariel", 10), textvariable=register_no_2)
register_no_p_ent.grid(row=0, column=1, padx=2, pady=2)
register_no_p_ent.bind("<FocusIn>", clear_print)

# Printing Info
display_frame = tk.Frame(print_frame, bg="white", bd=5, relief=tk.GROOVE)
display_frame = tk.LabelFrame(print_frame, font=("Ariel", 16), text="Student Info", border=5,
                              relief=tk.GROOVE,
                              bg="white")
display_frame.place(x=0, y=80, width=480, height=100)

display_name_lbl = tk.Label(display_frame, text="Name", bg="white", font=("Ariel", 10))
display_name_lbl.grid(row=1, column=0, padx=2, pady=2)
display_name = tk.Entry(display_frame, width=45, bd=5, font=("Ariel", 10), textvariable=d_name)
display_name.grid(row=1, column=1, padx=2, pady=2)

display_enrolment_lbl = tk.Label(display_frame, text="Enrollment No.", bg="white", font=("Ariel", 10))
display_enrolment_lbl.grid(row=2, column=0, padx=2, pady=2)
display_enroll = tk.Entry(display_frame, width=45, bd=5, font=("Ariel", 10), textvariable=d_enrol_no)
display_enroll.grid(row=2, column=1, padx=2, pady=2)

display_frame_2 = tk.Frame(print_frame, bg="white", bd=5, relief=tk.GROOVE)
display_frame_2 = tk.LabelFrame(print_frame, font=("Ariel", 16), text="Enter Leaving Information", border=5,
                                relief=tk.GROOVE,
                                bg="white")
display_frame_2.place(x=0, y=180, width=480, height=200)

progress_lbl = tk.Label(display_frame_2, text="Progress", bg="white", font=("Ariel", 10))
progress_lbl.grid(row=0, column=0, padx=2, pady=2)
progress_ent = tk.Entry(display_frame_2, width=45, bd=5, font=("Ariel", 10), textvariable=p_progress)
progress_ent.grid(row=0, column=1, padx=2, pady=2)
progress_ent.bind("<KeyRelease>", caps_2)

conduct_lbl = tk.Label(display_frame_2, text="Conduct", bg="white", font=("Ariel", 10))
conduct_lbl.grid(row=1, column=0, padx=2, pady=2)
conduct_ent = tk.Entry(display_frame_2, width=45, bd=5, font=("Ariel", 10), textvariable=p_conduct)
conduct_ent.grid(row=1, column=1, padx=2, pady=2)
conduct_ent.bind("<KeyRelease>", caps_2)

date_of_leaving_lbl = tk.Label(display_frame_2, text="Date of Leaving", font=("Ariel", 10), bg="white")
date_of_leaving_lbl.grid(row=2, column=0, padx=2, pady=2)
date_of_leaving_ent = DateEntry(display_frame_2, width=44, background='blue', date_pattern='dd/mm/yyyy',
                                foreground='white', borderwidth=5, font=("Ariel", 10), textvariable=p_dol)
date_of_leaving_ent.grid(row=2, column=1, padx=2, pady=2)
date_of_leaving_ent.bind("<FocusOut>", date_conv_2)

reason_lbl = tk.Label(display_frame_2, text="Reason", bg="white", font=("Ariel", 10))
reason_lbl.grid(row=3, column=0, padx=2, pady=2)
reason_ent = tk.Entry(display_frame_2, width=45, bd=5, font=("Ariel", 10), textvariable=p_reason)
reason_ent.grid(row=3, column=1, padx=2, pady=2)
reason_ent.bind("<KeyRelease>", caps_2)

remark_lbl = tk.Label(display_frame_2, text="Remark", bg="white", font=("Ariel", 10))
remark_lbl.grid(row=4, column=0, padx=2, pady=2)
remark_ent = tk.Entry(display_frame_2, width=45, bd=5, font=("Ariel", 10), textvariable=p_remark)
remark_ent.grid(row=4, column=1, padx=2, pady=2)
remark_ent.bind("<KeyRelease>", caps_2)
# ================= #


# ==== Buttons ==== #

btn_frame = tk.Frame(detail_frame, bg="white", bd=10, relief=tk.GROOVE)
btn_frame.place(x=45, y=480, width=340, height=120)

# Add Record
add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=5, font=("Ariel", 12), width=13, command=add_fun)
add_btn.grid(row=0, column=0, padx=8, pady=5)

# Update Record
update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=5, font=("Ariel", 12), width=13, command=update_fun)
update_btn.grid(row=0, column=1, padx=8, pady=5)

# Delete Record
delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=5, font=("Ariel", 12), width=13, command=delete_fun)
delete_btn.grid(row=1, column=0, padx=8, pady=5)

# Clear Record
clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=5, font=("Ariel", 12), width=13, command=clear)
clear_btn.grid(row=1, column=1, padx=8, pady=5)

# ==== Search Frame ==== #

search_frame = tk.Frame(data_frame, bg="white", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="Enter Register No.", bg="lightgrey", font=("Ariel", 12))
search_lbl.grid(row=0, column=0, padx=12, pady=12)
search_in = tk.Entry(search_frame, width=20, bd=5, font=("Ariel", 12), textvariable=search_by)

search_in.grid(row=0, column=1, padx=12, pady=12)

search_btn = tk.Button(search_frame, text="Search", font=("Ariel", 12), bd=10, width=12, bg="lightgrey",
                       command=search_data)
search_btn.grid(row=0, column=2, padx=12, pady=12)

showall_btn = tk.Button(search_frame, text="Show All", font=("Ariel", 12), bd=10, width=12, bg="lightgrey",
                        command=fetch_data)
showall_btn.grid(row=0, column=3, padx=12, pady=12)

# ===================== #

# ====Print Frame=====#

get_btn = tk.Button(print_frame, text="Get Data", font=("Ariel", 10), bd=10, width=12, bg="lightgrey", command=get_name)
get_btn.grid(row=0, column=3, padx=12, pady=12)

btn_frame_2 = tk.Frame(print_frame, bg="white", bd=10, relief=tk.GROOVE)
btn_frame_2.place(x=30, y=390, width=410, height=100)

get_btn = tk.Button(btn_frame_2, text="Generate TC", font=("Ariel", 12), bd=10, width=16, bg="lightgrey",
                    command=certificate.create_pdf)
get_btn.grid(row=0, column=1, padx=12, pady=12)

get_btn = tk.Button(btn_frame_2, text="Save Info", font=("Ariel", 12), bd=10, width=16, bg="lightgrey",
                    command=save_leaving_info)
get_btn.grid(row=0, column=0, padx=12, pady=12)

# ================= #


# ==== Database Frame ==== #

db_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
db_frame.pack(fill=tk.BOTH, expand=TRUE)

y_scroll = tk.Scrollbar(db_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(db_frame, orient=tk.HORIZONTAL)

stu_table = ttk.Treeview(db_frame, columns=(
    "Register No.", "Enrolment No.", "First Name", "Middle Name", "Last Name", "Mother's Name", "Caste",
    "Place of Birth",
    "Date of Birth", "Date", "Month", "Year", "Last Institute", "Date of Admission",
    "Course Name"),
                         yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=stu_table.yview)
x_scroll.config(command=stu_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

stu_table.heading("Register No.", text="Register No.")
stu_table.heading("Enrolment No.", text="Enrolment No.")
stu_table.heading("First Name", text="First Name")
stu_table.heading("Middle Name", text="Middle Name")
stu_table.heading("Last Name", text="Last Name")
stu_table.heading("Mother's Name", text="Mother's Name")
stu_table.heading("Caste", text="Caste")
stu_table.heading("Place of Birth", text="Place of Birth")
stu_table.heading("Date of Birth", text="Date of Birth")
stu_table.heading("Date", text="Date")
stu_table.heading("Month", text="Month")
stu_table.heading("Year", text="Year")
stu_table.heading("Last Institute", text="Last Institute")
stu_table.heading("Date of Admission", text="Date of Admission")
stu_table.heading("Course Name", text="Course Name")

stu_table['show'] = 'headings'

stu_table.column("Register No.", width=100)
stu_table.column("Enrolment No.", width=100)
stu_table.column("First Name", width=100)
stu_table.column("Middle Name", width=100)
stu_table.column("Last Name", width=100)
stu_table.column("Mother's Name", width=100)
stu_table.column("Caste", width=100)
stu_table.column("Place of Birth", width=100)
stu_table.column("Date of Birth", width=100)
stu_table.column("Date", width=100)
stu_table.column("Month", width=100)
stu_table.column("Year", width=100)
stu_table.column("Last Institute", width=300)
stu_table.column("Date of Admission", width=100)
stu_table.column("Course Name", width=300)

stu_table.pack(fill=tk.BOTH, expand=TRUE)

create_fun()
fetch_data()
stu_table.bind("<ButtonRelease-1>", get_cursor)

win.mainloop()
