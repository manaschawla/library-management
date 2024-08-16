import os
import csv
import smtplib
from datetime import datetime
from email.message import EmailMessage
class Library:
    def __init__(self, csv_file = "library_data.csv"):
        self.csv_file = csv_file
        self.initialize_csv()
    def initialize_csv(self):
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['Student Name', 'Book Name', 'Date and Time' , 'Email', 'Returned'])
    def send_email(self, student_name, book_name):
        sender_email = ""
        sender_password = ""
        receiver_email = input("enter the receiver's email")
        msg =  EmailMessage()
        msg.set_content(f"{student_name} has borrowed the book: {book_name}.")
        msg['subject'] = 'Book Borrowed Notification'
        msg['from'] = sender_email
        msg['to'] = receiver_email
        with smtplib.SMTP_SSL("smpt.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print(f"email send to {receiver_email} about book borrowed.")
                
    def borrow_book(self, book_name, student_name):
        student_name = input("enter the name of the student: ")
        book_name = input("enter the name of the book: ")
        now = datetime.now()
        email = input("enter your email")
        with open(self.csv_file, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([student_name, book_name, now, email])
            