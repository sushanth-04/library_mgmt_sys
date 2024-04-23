from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = f"INSERT INTO {bookTable} VALUES ('{bid}','{title}','{author}','{status}')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except pymysql.Error as e:
        messagebox.showinfo("Error", f"Error: {e}")

    root.destroy()


def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.geometry("600x600")
    root.configure(bg='#1e272e')

    # Add your own database name and password here to reflect in the code
    mypass = "Password"
    mydatabase = "LMS"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"  # Book Table

    headingLabel = Label(root, text="Add Books", bg='#2c3e50', fg='white', font=('Courier', 20))
    headingLabel.pack(pady=20)

    labelFrame = Frame(root, bg='#2c3e50')
    labelFrame.pack(pady=20, padx=20)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID:", bg='#2c3e50', fg='white', font=('Courier', 12))
    lb1.grid(row=0, column=0, padx=10, pady=10)

    bookInfo1 = Entry(labelFrame, font=('Courier', 12))
    bookInfo1.grid(row=0, column=1, padx=10, pady=10)

    # Title
    lb2 = Label(labelFrame, text="Title:", bg='#2c3e50', fg='white', font=('Courier', 12))
    lb2.grid(row=1, column=0, padx=10, pady=10)

    bookInfo2 = Entry(labelFrame, font=('Courier', 12))
    bookInfo2.grid(row=1, column=1, padx=10, pady=10)

    # Author
    lb3 = Label(labelFrame, text="Author:", bg='#2c3e50', fg='white', font=('Courier', 12))
    lb3.grid(row=2, column=0, padx=10, pady=10)

    bookInfo3 = Entry(labelFrame, font=('Courier', 12))
    bookInfo3.grid(row=2, column=1, padx=10, pady=10)

    # Status
    lb4 = Label(labelFrame, text="Status (Avail/Issued):", bg='#2c3e50', fg='white', font=('Courier', 12))
    lb4.grid(row=3, column=0, padx=10, pady=10)

    bookInfo4 = Entry(labelFrame, font=('Courier', 12))
    bookInfo4.grid(row=3, column=1, padx=10, pady=10)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', font=('Courier', 12), command=bookRegister)
    SubmitBtn.pack(pady=20)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', font=('Courier', 12), command=root.destroy)
    quitBtn.pack(pady=10)

    root.mainloop()
