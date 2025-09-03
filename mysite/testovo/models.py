from django.db import models


class Author(models.Model):
    """
    Модель автора, содержит поля:
    first_name: имя автора
    last_name: фамилия автора
    birth_date: дата рождения автора
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    """
    Модель книги, содержит следующие поля:
    title: название книги
    published_date: дата публикации
    price: цена книги
    author: модель автора
    """
    title = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title