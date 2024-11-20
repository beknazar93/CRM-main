from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} || должность {self.position} || {self.email} || {self.phone}'

    def delete(self, *args, **kwargs):
        # Дополнительные действия до удаления (если нужны)
        super(Employee, self).delete(*args, **kwargs)


class Client(models.Model):
    SPORT_CATEGORIES = [
        ('Бокс', 'Бокс'),
        ('ММА','ММА'),
        ('Sambo','Sambo'),
        ('Boryba', 'Boryba'),
        ('taekwondo','taekwondo'),
        ('Judo','Judo'),
        ('kickboxing','kickboxing'),
        ('krossfit', 'krossfit'),
        ('греко римская борьба','греко римская борьба')
    ]
    TRAINER_NAME = [
        ('Машрапов Тилек','Машрапов Тилек'),
        ('Мойдунов Мирлан','Мойдунов Мирлан'),
        ('Асанбоев Эрлан', 'Асанбоев Эрлан'),
        ('Сатаров Канат','Сатаров Канат'),
        ('Онарбоев Акжол','Онарбоев Акжол'),
        ('Абдуманаб уулу Илим','Абдуманаб уулу Илим'),
        ('Калмамат уулу Акай','Калмамат уулу Акай'),
        ('Маматжанов Марлен','Маматжанов Марлен'),
        ('Азизбек уулу Баяман','Азизбек уулу Баяман'),
        ('Тургунов Ислам', 'Тургунов Ислам'),
        ('Медербек уулу Саформурад','Медербек уулу Саформурад'),
        ('Лукас Крабб','Лукас Крабб'),
        ('Минбаев Сулайман','Минбаев Сулайман')
    ]
    MONTH_NAME = [
        ('Январь', 'Январь'),
        ('Февраль', 'Февраль'),
        ('Март', 'Март'),
        ('Апрель', 'Апрель'),
        ('Май', 'Май'),
        ('Июнь', 'Июнь'),
        ('Июль', 'Июль'),
        ('Август', 'Август'),
        ('Сентябрь', 'Сентябрь'),
        ('Октябрь', 'Октябрь'),
        ('Ноябрь', 'Ноябрь'),
        ('Декабрь', 'Декабрь')
    ]
    PRICE_NAME = [
        ('оплачено', 'оплачено'),
        ('неоплачено', 'неоплачено')
    ]
    DAY_NAME = [(str(i), str(i)) for i in range(1, 32)]
    YEAR_NAME = [(str(i), str(i)) for i in range(2020, 2029)]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default="primer@gmail.com")
    phone = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    stage = models.CharField(max_length=100)
    payment = models.CharField(max_length=100, choices=PRICE_NAME, null=True)
    price = models.CharField(max_length=20, default="2200")
    sport_category = models.CharField(max_length=100, choices=SPORT_CATEGORIES, null=True)
    trainer = models.CharField(max_length=100, choices=TRAINER_NAME, null=True)
    year = models.CharField(max_length=100, choices=YEAR_NAME, null=True)
    month = models.CharField(max_length=100, choices=MONTH_NAME, null=True)
    day = models.CharField(max_length=100, choices=DAY_NAME, null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} || {self.email} || {self.phone}'

    def delete(self, *args, **kwargs):
        # Дополнительные действия до удаления (если нужны)
        super(Client, self).delete(*args, **kwargs)


class SalesPipelineStage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    clients = models.ManyToManyField(Client, related_name='pipeline_stages', blank=True)

    def __str__(self):
        return f'{self.name}  {self.description}'

    def delete(self, *args, **kwargs):
        # Дополнительные действия до удаления (если нужны)
        super(SalesPipelineStage, self).delete(*args, **kwargs)
