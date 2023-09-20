from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2


import pytest

class BooksCollector:
    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    def get_book_genre(self, name):
        return self.books_genre.get(name)

    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    def get_books_genre(self):
        return self.books_genre

    def get_books_for_children(self):
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    def add_book_in_favorites(self, name):
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self):
        return self.favorites

class TestBooksCollector:

    @pytest.fixture
    def books_collector(self):
        return BooksCollector()

    def test_add_new_book(self, books_collector):
        books_collector.add_new_book("Book1")
        assert "Book1" in books_collector.get_books_genre()

    def test_set_book_genre(self, books_collector):
        books_collector.add_new_book("Book2")
        books_collector.set_book_genre("Book2", "Фантастика")
        assert books_collector.get_book_genre("Book2") == "Фантастика"

    def test_get_book_genre(self, books_collector):
        books_collector.add_new_book("Book3")
        books_collector.set_book_genre("Book3", "Ужасы")
        assert books_collector.get_book_genre("Book3") == "Ужасы"

    def test_get_books_with_specific_genre(self, books_collector):
        books_collector.add_new_book("Book4")
        books_collector.set_book_genre("Book4", "Фантастика")
        books_collector.add_new_book("Book5")
        books_collector.set_book_genre("Book5", "Фантастика")
        assert books_collector.get_books_with_specific_genre("Фантастика") == ["Book4", "Book5"]

    def test_get_books_genre(self, books_collector):
        books_collector.add_new_book("Book6")
        books_collector.set_book_genre("Book6", "Комедии")
        assert books_collector.get_books_genre() == {"Book6": "Комедии"}

    def test_get_books_for_children(self, books_collector):
        books_collector.add_new_book("Book7")
        books_collector.set_book_genre("Book7", "Мультфильмы")
        assert books_collector.get_books_for_children() == ["Book7"]

    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book("Book8")
        books_collector.add_book_in_favorites("Book8")
        assert "Book8" in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book("Book9")
        books_collector.add_book_in_favorites("Book9")
        books_collector.delete_book_from_favorites("Book9")
        assert "Book9" not in books_collector.get_list_of_favorites_books()


if __name__ == "__main__":
    pytest.main()
