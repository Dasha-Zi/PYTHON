from book import Book

library = [
    Book("Гордость и предубеждение", "Джейн Остин"),
    Book("Мастер и Маргарита", "Михаил Булгаков"),
    Book("Преступление и наказание",  "Фёдор Достоевский")
]
for book in library:
    print(f"{book.title} - {book.author}")