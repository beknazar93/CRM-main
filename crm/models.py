from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} || должность {self.position} || {self.email} || {self.phone}'





class Client(models.Model):
    SPORT_CATEGORIES = [
        ('Бокс', 'Бокс'),
        ('Футбол', 'Футбол'),
        ('Теннис', 'Теннис'),
        ('Плавание', 'Плавание'),
        ('Бег', 'Бег'),
        # Добавьте другие категории по необходимости
    ]
    TRAINER_NAME= [
        ('1', 'Мирлан'),
        ('2', 'Расул'),
        ('3', 'Тимур'),
        ('4', 'Айбек'),
        ('5', 'Улан'),
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
        ('Декабрь', 'Декабрь'),
    ]
    DAY_NAME = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
    ]
    YEAR_NAME = [
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default="primer@gmail.com")
    phone = models.CharField(max_length=100)
    stage = models.CharField(max_length=100)
    payment = models.CharField(max_length=20, default='оплачено')
    price = models.CharField(max_length=20, default="2200")
    sport_category = models.CharField(max_length=100, choices=SPORT_CATEGORIES, null=True)
    trainer = models.CharField(max_length=100, choices=TRAINER_NAME, null=True)
    year = models.CharField( max_length=100, choices=YEAR_NAME, null=True)
    month = models.CharField( max_length=100,  choices=MONTH_NAME, null=True)
    day = models.CharField( max_length=100,  choices=DAY_NAME, null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} || {self.email} || {self.phone}'


class SalesPipelineStage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    clients = models.ManyToManyField(Client, related_name='pipeline_stages')

    def __str__(self):
        return f'{self.name}  {self.description}'




