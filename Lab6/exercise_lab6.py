#create class
class Book:
    def __init__(self,bookname,price,auther,publisher):
        # object attributes
        self.bookname = bookname
        self.price = price
        self.auther = auther
        self.publisher = publisher
    def book_detail(self):
        print(f'Book name: {self.bookname} Price: {self.price} THB'
              f'Auther:  ')


        from book import  mybook

        book_stors = []
        num = int(input('คุณมีหนังสือทั้งหมดกี่เล่ม? :'))

        for x in range(num):
            bookname = input('ชื่อหนังสือ:')
            price = float(input('ราคา: '))
            auther = input('ชื่อผู้แต่ง: ')
            publisher = input('สำนักพิมพ์:')
            # 1
            b = Book(bookname,price,auther,publisher)
            book_stors.append(b)
            # 2
            #book_store.append(Book(bookname,price,auther,publisher))
        def display_book(book):
            for x in book:
                x.book_detail()

        display_book(book_stors)
