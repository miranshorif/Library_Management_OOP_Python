class User:
    # all_users = []
    def __init__(self,name,roll,password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = []
        self.returned_books = []


class Library:
    def __init__(self,book_list) -> None:
        self.book_list = book_list

    def borrow_book(self,bookName,user):
        for book in self.book_list:
            if book == bookName:
                if bookName in user.borrow_books:
                    print('Age ferot dao')
                    return
                if self.book_list[book] == 0:
                    print('book sesh hoea gece')
                    return
                self.book_list[book] -= 1
                user.borrow_books.append(bookName)
                print('You have borrowed this book')
                return
        print('book not available')

    def return_book(self,bookName,user):
        for book in self.book_list:
            if book == bookName:
                if book in user.borrow_books:
                    self.book_list[book] += 1
                    user.borrow_books.remove(bookName)
                    user.returned_books.append(bookName)
                    print('book returned successfully')
                    return
                else:
                    print('Onner book nebona')
        print('kar book ferot dite asco')

    def donate(self,bookName,amount):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += amount
                print('Thanks for donating')
                return
        self.book_list[bookName] = amount
        print('Thanks for donating')

    def available(self):
        for book in self.book_list:
            if self.book_list[book] > 0:
                print(book,self.book_list[book])
                

library = Library({'English':3,'Bangla':4,'Math':6})

all_users = []
current_users = None

while True:
    if current_users == None:
        print('Not logged in\nPlease Login or cread account (L/C)')
        option = input('Enter C/L: ')
        if option == 'L':
            roll = int(input('Roll: '))
            password = input('Password: ')
            match = False
            for user in all_users:
                if user.roll == roll and user.password == password:
                    current_users = user
                    match = True
            if match == False:
                print('No user found')
        else:
            name = input('Name: ')
            roll = int(input('Roll: '))
            password = input('Password: ')
            found = False
            for user in all_users:
                if roll.user == roll:
                    found = True
            if found:
                print('Bhi koto bar account khulben?')
                continue
            user = User(name,roll,password)
            current_users = user
            all_users.append(user)
    else:
        print('\n\n________OPTION__________\n')
        print('1.Borrow a book')
        print('2.Returne a book')
        print('3.Borrowe books list')
        print('4.Return books list')
        print('5.Check Available')
        print('6.Donate book')
        print('7.Logout')
        x = int(input('Give option: '))
        if x == 1:
            bookName = input('Book name: ')
            library.borrow_book(bookName,current_users)
        elif x == 2:
            bookName = input('Book name: ')
            library.return_book(bookName,current_users)
        elif x == 3:
            print(current_users.borrow_books)
        elif x == 4:
            print(current_users.returned_books)
        elif x == 5:
            library.available()
        elif x == 6:
            bookName = input('Book name: ')
            amount =  int(input('Amount: '))
            library.donate(bookName,amount)
        elif x == 7:
            current_users = None
