import json
import datetime
file_name = 'library2_data.json'
def load_file():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        FileNotFoundError
        return []
def save_record(data, file_name = 'library2_data.json'):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent= 5)
class Library:
    def __init__(self) -> None:
        self.library_data = load_file()
        #self.library_data.get("books", [])
        
    def borrow_books(self, name, book_name, email, now,  returned = 'no'):
        data = load_file()
        data.append({
            "name": name,
            "bookname": book_name,
            "email": email,
            "date-time" : str(now),
            "returned" : returned,
        })
        save_record(data)
        print(f"The Book: {book_name} Has Been borrowed succesfully by the student: {name}")
    def view_all_entries(self):
        datas = load_file()
        for data in datas:
            print(f"name: {data['name']}, book_name: {data['bookname']}, email: {data['email']}, date: {data['date-time']}, returned: {data['returned']}") 
    def total_books(self):
        datas = load_file()
        total_books = 0
        for data in datas:
            if data['returned'] == 'no':
                total_books += 1
        print(f"total books borrowed: {total_books}")
    def book_borrow_student(self):
        books = 0
        student_borrow = {}
        datas = load_file()
        student_name = input("enter the name of the student you want to check: ")
        for data in datas:
            if student_name == data['name']:
                if data['name'] in student_borrow:
                    student_borrow[data['name']] += 1

                else:
                    student_borrow[data['name']] = 1
        for student, count in student_borrow.items():
            print(f"{student} has borrowed {count} books")
    def return_book(self):
        book_return = input("enter the book name to be returned: ")
        datas = load_file()
        for data in datas:
            if data['bookname'] == book_return:
                if data['returned'] == 'no':
                    print("book was borrowed")
                    data.update({"returned": "yes"})
                    save_record(datas)
                    print("book has been returned")
                    break
                else:
                    print("book has already returned.")
                    break
            else:
                print("book is not borrowed")
                break
                
while True:
    print("""WELCOME TO LIBRARY MANAGEMENT SYSTEM.
        1.Add entry of borrow book.
        2.View all entries.
        3.Add entry of return book.
        4.Total books borrowed.
        5.Number of books borrowed by a student.
        6.Exit""")
    library = Library()
    choice = int(input("enter your choice via 1/2/3/4/5: "))
    if choice == 1:
        name = input("enter the name of the student: ")
        book_name = input("enter the name of book: ")
        now = datetime.datetime.now()
        email = input("enter the email of the student: ")
        library.borrow_books(name, book_name, email, now )
    if choice == 2:
        library.view_all_entries()
    elif choice == 3:
        library.return_book()
    elif choice == 4:
        library.total_books()
    elif choice == 5:
        library.book_borrow_student()
    elif choice == 6:
        print("THANK YOU")
        break
        