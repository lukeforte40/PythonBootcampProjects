library = []
class book:
    def __init__(self, isbn, title, pages, edition, publisher, author, pubDate):
        self.isbn = isbn
        self.title = title
        self.pages = pages
        self.edition = edition
        self.publisher = publisher
        self.author = author
        self.pubDate = pubDate
        self.booklist = [isbn, title, pages, edition, publisher, author, pubDate]
    def addBook(self):
        library.append(self.booklist)
        print('Added book', self.booklist)
    def deleteBoookByTitle(self, title):
        for x in library:
            if title in x:
                library.remove(x)
        print('Deleted book', x)       
    def deleteBoookByIsbn(self, isbn):
        for x in library:
            if isbn in x:
                library.remove(x)
        print('Deleted book', x)       
    def editInfo(self, title, oldInfo, newInfo):
        for x in library:
            if title in x:
                x.remove(oldInfo)
                x.append(newInfo)
        print('Changed book', x)
    def findBook(self, isbn):
        for x in library:
            if isbn in x:
                print(x)
test = book(1,'test',20,1,'summit works','luke',2019)
test.addBook()
test = book(2,'tes2',25,2,'summit works','luke',2019)
test.addBook()
print(library)
test.deleteBoookByTitle('test')
print(library)
test = book(3,'tes3',29,3,'summit works','luke',2019)
test.addBook()
print(library)
test.deleteBoookByIsbn(3)
print(library)
test = book(4,'tes4',40,4,'summit works','luke',2019)
test.addBook()
print(library)
test.editInfo('tes4', 40, 50)
print(library)
test.findBook(4)
