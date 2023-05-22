from django.db import models
from ckeditor.fields import RichTextField

""" HOME PAGE MODEL """


class HomePageContent(models.Model):
    """ Home page content model """

    name = models.CharField("Название страницы",
                            max_length=255)
    title = models.CharField("Главный заголовок h1",
                             max_length=255, default=None)
    text = models.TextField("Контент")

    def __str__(self):
        return f'id: {self.id} {self.name}'

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"


class Client(models.Model):
    """ A client queries registry form """

    name = models.CharField("Имя", max_length=255)
    phone = models.CharField("Номер телефона", max_length=255)
    gmt = models.CharField("Часовой пояс", max_length=128)
    query = models.TextField("Запрос")

    def __str__(self):
        return f'id: {self.id} {self.name} {self.phone}'

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


""" ABOUT PAGE MODEL """


class AboutPageContent(models.Model):
    """ About page content model """

    name = models.CharField("Название страницы",
                            max_length=128)
    title = models.CharField("Главный заголовок h1",
                             max_length=255, default=None)
    text = RichTextField("Контент")

    def __str__(self):
        return f'id: {self.id} {self.name}'

    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"


""" PRICES PAGE MODEL """


class PricesPageContent(models.Model):
    """ Prices page content model """

    name = models.CharField("Название страницы",
                            max_length=128)
    title = models.CharField("Главный заголовок h1",
                             max_length=255,
                             default=None)
    text_1 = models.TextField("Контент 1",
                              default=None)
    text_2 = models.TextField("Контент 2",
                              default=None)
    text_3 = models.TextField("Контент 3",
                              default=None)

    def __str__(self):
        return f'id: {self.id} {self.name}'

    class Meta:
        verbose_name = "Страница Цены"
        verbose_name_plural = "Страница Цены"


class Service(models.Model):
    """ The table for Prices page """

    service = models.CharField("Услуга", max_length=128, blank=False, help_text="Введите наименование услуги")
    duration = models.CharField("Продолжительность", max_length=64, blank=False,
                                help_text="Сколько по времени длится сессия")
    price = models.IntegerField("Цена", blank=False, help_text="Введите цену. Числом, без букв. Не может быть пустым!")

    def __str__(self):
        return f'id: {self.id} {self.service}'

    class Meta:
        verbose_name = "Таблица цен"
        verbose_name_plural = "Таблица цен"


class SocialNetworksLinks(models.Model):
    """ Model for containing social networks account names """
    name = models.CharField("Название соцсети", max_length=64, default="none")
    account = models.CharField("Аккаунт", max_length=128,
                               default="none")

    def __str__(self):
        return f'id: {self.id}: {self.name}: {self.account}'

    class Meta:
        verbose_name = "Ссылка на Соцсети"
        verbose_name_plural = "Ссылки на Соцсети"
