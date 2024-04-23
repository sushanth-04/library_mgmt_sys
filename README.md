# library_mgmt_sys

# Library Management System in Python
The library management system in python which we are going to build will look something like this

## Home ##
![Home](https://github.com/sushanth-04/library_mgmt_sys/assets/134486908/6a6a00b1-5e3e-4f2f-bc4c-3c03b7463446)

## Operations ##
![Addbook](https://github.com/sushanth-04/library_mgmt_sys/assets/134486908/212f25db-7147-41ba-8abc-c3bf003be31e)
![DeleteBook](https://github.com/sushanth-04/library_mgmt_sys/assets/134486908/c3f77e33-f70c-4018-8d84-799d24e77630)
![ViewBook](https://github.com/sushanth-04/library_mgmt_sys/assets/134486908/86fefba0-d426-4826-acb5-0eeb9a1389d5)
![IssueBook](https://github.com/sushanth-04/library_mgmt_sys/assets/134486908/8d6092e5-985e-496e-9804-21442141fe6b)
![ReturnBook](https://github.com/sushanth-04/library_mgmt_sys/assets/134486908/3efcac6d-966a-4eb1-9ae1-60084e72194c)

Project Prerequisites
tkinter – Please run below command to install tkinter
```
pip install tkinter
```

pillow – Please run below command to install tkinter
```
pip install pillow
```

pymysql – Please run below command to install tkinter

```
pip install pymysql
```

##Description of Project Files
Below are the project files you will get once you download and extract the Library project:

main.py – which does function call to all other python files
AddBook.py – To add the book
ViewBooks.py – To View the list of books in the library
DeleteBook.py – To Delete a book from library
IssueBook.py – To Issue a book from library
ReturnBook.py – To Return a book to the library

##Description of Tables
#Create Tables
```sql
create database LMS;
create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
create table books_issued(bid varchar(20) primary key, issuedto varchar(30));
```


