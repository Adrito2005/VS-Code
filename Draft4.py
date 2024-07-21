from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mycon
import tkinter as tk

root = tk.Tk()

root.title("Bookstore Management System")

# Maximize the window to full-screen (cross-platform)
root.attributes('-zoomed', True)



state1 = 'disabled'
state2 = 'disabled'
state3 = 'disabled'
allUser = [] # List To store all User IDs
allEmpId = [] # List To store all Employee IDs
allBid = [] # List To store all Book IDs
num = 0

con = mycon.connect(host="localhost", user="root", password="root",database="projectdb")
cur = con.cursor(buffered=True)

def gettingLoginDetails():
    global role, state1, state2, btn1, btn3, btn4, btn5, state3
    Id = ent1.get()
    name = ent2.get()
    password = ent3.get()
    role = ent4.get()
    if role == 'Admin':
        sqlLoginID = "select empid from empdetail where password = '" + password + "'"
        sqlName = "select name from empdetail where password = '" + password + "'"
        try:
            cur.execute(sqlLoginID)
            for i in cur:
                getLoginID = i[0]
            cur.execute(sqlName)
            for i in cur:
                getName = i[0]

            if (getLoginID == Id and getName == name):
                messagebox.showinfo("SUCCESS", "You have successfully logged in")
                btn1.destroy()
                btn3.destroy()
                btn4.destroy()
                btn5.destroy()
                state1 = 'normal'
                state2 = 'normal'
                state3 = 'normal'
                Menu()
            else:
                messagebox.showerror("Failure", "Can't log in, check your credentials")
        except Exception as e:
            print(e)
            messagebox.showinfo("FAILED", "Please check your credentials")

    else:
         sqlLoginID = "select userid from userdetail where password = '" + password + "'"
         sqlName = "select name from userdetail where password = '" + password + "'"
         try:
             cur.execute(sqlLoginID)
             for i in cur:
                 getLoginID = i[0]
                 cur.execute(sqlName)
             for i in cur:
                getName = i[0]

             if (getLoginID == Id and getName == name):
                 btn1.destroy()
                 btn3.destroy()
                 btn4.destroy()
                 btn5.destroy()
                 state2 = 'normal'
                 state3 = 'normal'
                 Menu()
                 messagebox.showinfo("SUCCESS", "You have successfully logged in")
             else:
                messagebox.showerror("Failure", "Can't log in, check your credentials")
         except:
            messagebox.showinfo("FAILED", "Please check your credentials")

    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)

def Menu():
    global state1, state2, btn1, btn3, btn4, btn5
    btn1 = Button(moduleFrame, text="Add Book Details", font=("arial", 12, 'bold'),compound=LEFT,command=addBooks, state=state1)
    btn1.place(relx=0, rely=0.17, relwidth=1, relheight=0.12)
    btn3 = Button(moduleFrame, text="View Book List", font=("arial", 12, 'bold'),compound=LEFT,command=View, state=state2)
    btn3.place(relx=0, rely=0.32, relwidth=1, relheight=0.12)
    btn4 = Button(moduleFrame, text="Search Book", font=("arial", 12, 'bold'),compound=LEFT,command=searchBook, state=state2)
    btn4.place(relx=0, rely=0.47, relwidth=1, relheight=0.12)
    btn5 = Button(moduleFrame, text="Issue Book to User", font=("arial", 12, 'bold'),compound=LEFT,command=issueBook, state=state1)
    btn5.place(relx=0, rely=0.62, relwidth=1, relheight=0.12)

### Add Book ######
def bookRegister():
    global en1, en2, en3, en4
    bid = en1.get()
    title = en2.get()
    title = title.title()
    subject = en3.get()
    subject = subject.title()
    author = en4.get()
    author = author.title()

    insertBooks = "insert into books (bid,title,subject,author) values('" + bid + "','" + title + "','" + subject + "','" + author + "')"
    print(insertBooks, "*****")
    if bid == "" or title == "" or subject == "" or author == "":
        messagebox.showinfo("Error", "Please fill all the details")
    else:
        try:
            cur.execute(insertBooks)
            con.commit()
            messagebox.showinfo("Sucess", "Book added")

        except:
            messagebox.showinfo("Error", "Can't add data into Database")
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
def addBooks():
    global en1, en2, en3, en4, lb1, lb2, lb3, lb4, SubmitBtn, lb, num

    destroyAll()

    lb = Label(displayFrame, text='Add Book Details', font=("Times New Roman", 26, 'bold'), bg='white')
    lb.place(relx=0.34, rely=0)
    # Book ID
    lb1 = Label(displayFrame, text="Book ID : ", font=("arial", 12, 'bold'), bg='white')
    lb1.place(relx=0.05, rely=0.2)

    en1 = Entry(displayFrame, font=("arial", 12, 'bold'), bg='#FFDFA4')
    en1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Title
    lb2 = Label(displayFrame, text="Title : ", font=("arial", 12, 'bold'), bg='white')
    lb2.place(relx=0.09, rely=0.35)

    en2 = Entry(displayFrame, font=("arial", 12, 'bold'), bg='#FFDFA4')
    en2.place(relx=0.3, rely=0.35, relwidth=0.62)

    # Book Subject

    lb3 = Label(displayFrame, text="Subject :", font=("arial", 12, 'bold'), bg='white')
    lb3.place(relx=0.05, rely=0.5)

    en3 = Entry(displayFrame, font=("arial", 12, 'bold'), bg='#FFDFA4')
    en3.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Book Author

    lb4 = Label(displayFrame, text="Author : ", font=("arial", 12, 'bold'), bg='white')
    lb4.place(relx=0.05, rely=0.65)

    en4 = Entry(displayFrame, font=("arial", 12, 'bold'), bg='#FFDFA4')
    en4.place(relx=0.3, rely=0.65, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(displayFrame, text="SUBMIT", font=("arial", 12, 'bold'), bg='white', command=bookRegister)
    SubmitBtn.place(relx=0.65, rely=0.8, relwidth=0.18, relheight=0.08)

    num = 1

### Issue Book ###
def issue():
     # global lb1,lb2,lb3,en1,en2,en3,status,scroll_y,issue_table,num
     bid = en1.get()
     issueto = en2.get()
     issueby = en3.get()

     extractBid = "select bid from books"
     try:
         cur.execute(extractBid)
         con.commit()
         for i in cur:
            allBid.append(i[0])
         if bid in allBid:
             checkAvail = "select status from books where bid = '" + bid + "'"
             cur.execute(checkAvail)
             con.commit()
             for i in cur:
                check = i[0]

             if check == 'Available':
                status = True
             else:
                status = False
         else:
            messagebox.showinfo("Error", "Book ID not present")
     except:
         messagebox.showinfo("Error", "Can't fetch Book IDs")

     extractUser = "select userid from userdetail"
     try:
         cur.execute(extractUser)
         con.commit()
         for i in cur:
             allUser.append(i[0])

         if issueto in allUser:
            pass
         else:
             messagebox.showinfo("Error", "User ID not present")
     except:
        messagebox.showinfo("Error", "Can't fetch User ID")
     extractEmpID = "select empid from empdetail"

     try:
         cur.execute(extractEmpID)
         con.commit()
         for i in cur:
             allEmpId.append(i[0])

         if issueby in allEmpId:
             pass
         else:
             messagebox.showinfo("Error", "Emp ID not present")
     except:
         messagebox.showinfo("Error", "Can't fetch Emp IDs")

     issueSql = "insert into orderdetail values ('" + bid + "','" + issueto + "','" + issueby + "')"

     updateStatus = "update books set status = 'sold' where bid = '" + bid + "'"
     try:
         if bid in allBid and issueto in allUser and issueby in allEmpId and status == True:
             cur.execute(issueSql)
             con.commit()
             cur.execute(updateStatus)
             con.commit()
             messagebox.showinfo("Success", " Issued Book successfully")

         else:
             allBid.clear()
             allEmpId.clear()
             allUser.clear()
             return
     except:
         messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

     en1.delete(0, END)
     en2.delete(0, END)
     en3.delete(0, END)

     allBid.clear()
     allEmpId.clear()
     allUser.clear()

def issueBook():
    global en1, en2, en3, issueBtn, lb1, lb2, lb3, en1, en2, en3, lb, num, issuedBooks
    destroyAll()

    lb = Label(displayFrame, text="Issue Book to User", font=('Times New Roman', 26, 'bold'), bg='white')
    lb.place(relx=0.27, rely=0)
    # Book ID
    lb1 = Label(displayFrame, text="Book ID : ", font=('arial', 12, 'bold'), bg='white')
    lb1.place(relx=0.05, rely=0.2)
    en1 = Entry(displayFrame, font=('arial', 12, 'bold'), bg='#FFDFA4')
    en1.place(relx=0.4, rely=0.2, relwidth=0.55)

    # Issued To Roll Number
    lb2 = Label(displayFrame, text="Ordered By (User ID) : ", font=('arial', 12, 'bold'), bg='white')
    lb2.place(relx=0.05, rely=0.4)
    en2 = Entry(displayFrame, font=('arial', 12, 'bold'), bg='#FFDFA4')
    en2.place(relx=0.4, rely=0.4, relwidth=0.55)

    # Issued By Employee Number
    lb3 = Label(displayFrame, text="Issued By(Admin ID) : ", font=('arial', 12, 'bold'), bg='white')
    lb3.place(relx=0.05, rely=0.6)

    en3 = Entry(displayFrame, font=('arial', 12, 'bold'), bg='#FFDFA4')
    en3.place(relx=0.4, rely=0.6, relwidth=0.55)

    # Issue Button
    issueBtn = Button(displayFrame, text="Issue Order", bg='white', font=("arial", 12, 'bold'), command=issue)
    issueBtn.place(relx=0.7, rely=0.75, relwidth=0.18, relheight=0.08)

    # View Issued Books
    issuedBooks = Button(displayFrame, text="View Ordered Books", bg='white', font=("arial", 12, 'bold'),command=displayissuedbooks)
    issuedBooks.place(relx=0.15, rely=0.75, relwidth=0.28, relheight=0.08)

    num=3

### Search Book ###
def search():
    global SearchBtn, labelFrame, lb1, en1, scroll_y, books_table, num
    sub = en1.get()
    sub = sub.title()
    destroyAll()
    scroll_y = Scrollbar(displayFrame, orient=VERTICAL)
    books_table = ttk.Treeview(displayFrame, columns=("bid", "title", "subject", "author", "status"),yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=books_table.yview)
    books_table.heading("bid", text="Book ID")
    books_table.heading("title", text="Title")
    books_table.heading("subject", text="Subject")
    books_table.heading("author", text="Author")
    books_table.heading("status", text="Status")
    books_table["show"] = "headings"
    books_table.column("bid", width=50)
    books_table.column("title", width=50)
    books_table.column("subject", width=50)
    books_table.column("author", width=50)
    books_table.column("status", width=50)
    books_table.pack(fill=BOTH, expand=1)
    num = 7
    searchSql = "select * from books where subject = '" + sub + "'"
    try:
        cur.execute(searchSql)
        con.commit()
        rows = cur.fetchall()
        for row in rows:
            books_table.insert('', END, values=row)
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

def searchBook():
    global en1, SearchBtn, lb1, headingLabel, num
    destroyAll()

    headingLabel = Label(displayFrame, text="Search Book", font=("Times New Roman", 26, 'bold'), bg='white')
    headingLabel.place(relx=0.35, rely=0.05)

    # Book ID to Delete
    lb1 = Label(displayFrame, text="Enter Subject : ", font=("arial", 12, 'bold'), bg='white')
    lb1.place(relx=0.05, rely=0.4)

    en1 = Entry(displayFrame, font=("arial", 12, 'bold'), bg='#FFDFA4')
    en1.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Submit Button
    SearchBtn = Button(displayFrame, text="Search", font=('arial', 12, 'bold'), bg='white', command=search)
    SearchBtn.place(relx=0.66, rely=0.55, relwidth=0.18, relheight=0.08)
    num = 6

##Destroy all Widgets##
def destroyAll():
    if num == 1:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        lb4.destroy()
        en3.destroy()
        en4.destroy()
        SubmitBtn.destroy()
    elif num == 2:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        SubmitBtn.destroy()
    elif num == 3:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        en3.destroy()
        issueBtn.destroy()
        issuedBooks.destroy()
    elif num == 4:
        scroll_y.destroy()
        issue_table.destroy()
    elif num == 5:
        en1.destroy()
        en2.destroy()
        lb1.destroy()
        lb2.destroy()
        headingLabel.destroy()
    elif num == 6:
        en1.destroy()
        lb1.destroy()
        headingLabel.destroy()
        SearchBtn.destroy()
    elif num == 7 or num == 8:
        scroll_y.destroy()
        books_table.destroy()
    else:
        pass

## View Books ###
def View():
    global scroll_y, books_table, num, headingLabel
    destroyAll()
    scroll_y = Scrollbar(displayFrame, orient=VERTICAL)
    books_table = ttk.Treeview(displayFrame, columns=("bid", "title", "subject", "author", "status"),
     yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=books_table.yview)
    books_table.heading("bid", text="Book ID")
    books_table.heading("title", text="Title")
    books_table.heading("subject", text="Subject")
    books_table.heading("author", text="Author")
    books_table.heading("status", text="Status")
    books_table["show"] = "headings"
    books_table.column("bid", width=50)
    books_table.column("title", width=50)
    books_table.column("subject", width=50)
    books_table.column("author", width=50)
    books_table.column("status", width=50)
    books_table.pack(fill=BOTH, expand=1)
    num = 8
    getBooks = "select * from books "
    try:
        cur.execute(getBooks)
        con.commit()
        rows = cur.fetchall()
        for row in rows:
            books_table.insert('', END, values=row)
    except:
        messagebox.showinfo("Error", "Can't fetch data from database")

### Frames ####
headingFrame = Frame(root, bd=20, relief=RIDGE)
headingFrame.place(relx=0, rely=0, relwidth=1, relheight=0.2)
heading = Label(headingFrame, font=('Arial', 32, 'bold'), text="Bookstore Management System")
heading.place(relx=0, rely=0.2)

moduleFrame = Frame(root, bd=20, relief=RIDGE)
moduleFrame.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.8)

headingLabel = Label(moduleFrame, text="MENU", font=("Times New Roman", 26, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=0.15)

dFrame = Frame(root, bd=20, relief=RIDGE)
dFrame.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)

displayFrame = Frame(dFrame, bd=10, relief=SOLID, bg='white')
displayFrame.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.9)

#### Interface for login ###

# ID
lb1 = Label(headingFrame, text='Unique ID:', font=('arial', 12, 'bold'))
lb1.place(relx=0.63, rely=0.01)

ent1 = Entry(headingFrame, font=('arial', 12, 'bold'))
ent1.place(relx=0.7, rely=0.01, relwidth=0.15)

# Name
lb2 = Label(headingFrame, text='Name:', font=('arial', 12, 'bold'))
lb2.place(relx=0.63, rely=0.25)

ent2 = Entry(headingFrame, font=('arial', 12, 'bold'))
ent2.place(relx=0.7, rely=0.25, relwidth=0.15)

# Password
lb3 = Label(headingFrame, text='Password:', font=('arial', 12, 'bold'))
lb3.place(relx=0.63, rely=0.48)

ent3 = Entry(headingFrame, font=('arial', 12, 'bold'), show="\u2022")
ent3.place(relx=0.7, rely=0.48, relwidth=0.15)

# Role Combobox

lb4 = Label(headingFrame, text='Role:', font=('arial', 12, 'bold'))
lb4.place(relx=0.63, rely=0.73)

ent4 = ttk.Combobox(headingFrame, font=('arial', 12, 'bold'), state='readonly', width=23)
ent4['value'] = ('', 'Admin', 'User')
ent4.current(0)
ent4.place(relx=0.7, rely=0.73, relwidth=0.15)

loginBtn = Button(headingFrame, text="LOGIN", font=("arial", 10, 'bold'),command=gettingLoginDetails)
loginBtn.place(relx=0.87, rely=0.4, relwidth=0.1)

Menu()
root.mainloop()