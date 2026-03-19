class Employee:
    def __init__(self,employee_name,employee_id,employee_role):
        self.name=employee_name
        self.id=employee_id
        self.role=employee_role


class Student:
    count=0
    def __init__(self,name=None,age=None,course=None,hometown=None):
        self.name=name
        self.age=age
        self.__course=course
        self.__id=None
        self.hometown=hometown
        if name and age and course and hometown:
            self.register()

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_course(self):
        return self.__course
    
    def get_hometown(self):
        return self.hometown
    
    def register(self):
        Student.count+=1
        self.__id=Student.count
        return self.__id
    
    def update_name(self,name):
        self.name=name

    def _update_age(self,age):
        self.age=age

    
class Libraryitem:
    def __init__ (self,book_author,book_id):
        self.author=book_author
        self.id=book_id

    def display_info(self):
        print(f"\nAuthor:{self.author}")
        print(f"ID:{self.id}")


class Book(Libraryitem):
    def __init__(self,book_title,book_author,book_category,book_id):
        super().__init__(book_author,book_id)
        self.__title=book_title
        self.__category=book_category

    def print_book_details(self):
        print(self.__title)
        print(self.__author)
        print(self.__category)
        print(self.__id)

    def get_title(self):
        return self.__title


class Ebook(Book):
    def __init__(self,book_title,book_author,book_category,book_id,file_format):
        super().__init__(book_title,book_author,book_category,book_id)
        self.file_format=file_format
    
    def display_info(self):
        super().display_info()
        print(f"file format:{self.file_format}")


class BookManagement:
    def checkout_book(self,student,book):
        print(f"\nStudent {student.name} is taking book {book.get_title()}")
        return True
    
    def return_book(self,student,book):
        print(f"Student {student.name} is returning book {book.get_title()}")
        return True


def main():
    new_student=Student()
    new_student.name=input("Enter a name:")
    new_student.age=int(input("Enter a age:"))
    new_student.hometown=input("Enter a address:")

    print(f"\nStudent name is {new_student.get_name()}")
    print(f"Student age is {new_student.get_age()}")

    second_student=None
    if second_student is not None:
        second_student.Name="Sita"

    second_student=Student("Sita",18,"Science","Mangalore")
    print(f"Student name is {second_student.get_name()}")
    print(f"Student age is {second_student.get_age()}")

    operations=BookManagement()
    book1=Book("PCS","Unknown","Coding","1")

    book1.display_info()

    ebook1=Ebook("PCS","Unknown","Coding","1","pdf")
    ebook1.display_info()

    operations.checkout_book(second_student,book1)
    operations.checkout_book(new_student,book1)

    operations.return_book(new_student,book1)

if __name__ =="__main__":
    main()


