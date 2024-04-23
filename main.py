from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# Add your own database name and password here to reflect in the code
mypass = "BVSs@240104"
mydatabase = "LMS"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.geometry("800x600")


# Define function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


# Center the window
center_window(root, 800, 600)

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
n = 1.5  # Adjust the value of n to resize the background image

newImageSizeWidth = int(imageSizeWidth * n)
newImageSizeHeight = int(imageSizeHeight * n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.LANCZOS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(400, 300, image=img)
Canvas1.pack(expand=True, fill=BOTH)

# Heading Frame
headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to Aurora Library", bg='black', fg='white', font=('Helvetica', 20))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Buttons
buttonsFrame = Frame(root, bg="black")
buttonsFrame.place(relx=0.25, rely=0.35, relwidth=0.5, relheight=0.5)

btn1 = Button(buttonsFrame, text="Add Book Details", bg='#FFA500', fg='black', font=('Courier', 12), command=addBook)
btn1.pack(side=TOP, fill=BOTH, padx=10, pady=10)

btn2 = Button(buttonsFrame, text="Delete Book", bg='#FFA500', fg='black', font=('Courier', 12), command=delete)
btn2.pack(side=TOP, fill=BOTH, padx=10, pady=10)

btn3 = Button(buttonsFrame, text="View Book List", bg='#FFA500', fg='black', font=('Courier', 12), command=View)
btn3.pack(side=TOP, fill=BOTH, padx=10, pady=10)

btn4 = Button(buttonsFrame, text="Issue Book to Student", bg='#FFA500', fg='black', font=('Courier', 12),
              command=issueBook)
btn4.pack(side=TOP, fill=BOTH, padx=10, pady=10)

btn5 = Button(buttonsFrame, text="Return Book", bg='#FFA500', fg='black', font=('Courier', 12), command=returnBook)
btn5.pack(side=TOP, fill=BOTH, padx=10, pady=10)

root.mainloop()
