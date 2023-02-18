class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author



class PaperBook(Book):
    """Дочерний класс - бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if isinstance(new_pages, int):
            if new_pages > 0:
                self._pages = new_pages
            else:
                raise AttributeError(f'Количество страниц не может быть отрицательным')
        else:
            raise ValueError(f"Количество страниц должно быть представлено в виде целочисленного типа данных ")


    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if isinstance(new_duration, float):
            if new_duration > 0:
                self._duration = new_duration
            else:
                raise AttributeError(f'Продолжительность не может быть отрицательной')
        else:
            raise ValueError(f"Продолжительность дожна быть представлена в виде числа с плавующей зпт")

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

if __name__ == "__main__":

    mumu = AudioBook("Муму", "Тургенев", 60.5)
    print (mumu)
    mumu.duration = 70.5
    print(mumu)
    try:
        mumu.duration = "-70.0"
    except:
        print("Duration setter works correctly")
    print(mumu)
    try:
        mumu.author = "Пушкин"
    except:
        print("Author setter works correctly")
    print(mumu)
    try:
        mumu.name = "Каританская дочка"
    except:
        print("Name setter works correctly")
    print(mumu)




