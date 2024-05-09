from django.db import models


class EmployeeRole(models.Model):
    name = models.CharField(verbose_name='Имя роли', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Роль сотрудника"
        verbose_name_plural = "Роли сотрудников"



class Employee(models.Model):
    employee_role = models.ForeignKey(EmployeeRole, verbose_name='Роль сотрудника', on_delete=models.CASCADE)
    surname = models.CharField(verbose_name='Фамилия', max_length=50)
    name = models.CharField(verbose_name='Имя', max_length=50)
    patronymic = models.CharField(verbose_name='Отчество', max_length=50, null=True, default='-')
    login = models.CharField(verbose_name='Логин', max_length=50, default='-')
    password = models.CharField(verbose_name='Пароль', max_length=50, default='-')

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic} - {self.employee_role.name}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

#Карта
class Map(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    image = models.ImageField(verbose_name='Изображение карты', upload_to='static/img')

    def __str__(self):
        return f"Карта {self.name}"

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"


#Общее оборудование
class Equipment(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    description = models.CharField(verbose_name='Краткое описание', max_length=50, blank=True, default='')
    x_position = models.DecimalField(verbose_name='Позиция по X для карты', max_digits=6, decimal_places=2)
    y_position = models.DecimalField(verbose_name='Позиция по Y для карты', max_digits=6, decimal_places=2)
    is_in_stock = models.BooleanField(verbose_name='На складе?', default=False)
    map = models.ForeignKey(Map, verbose_name='На какой карте оборудование находится', on_delete=models.PROTECT, null=True)
    last_update = models.DateTimeField(verbose_name='Последняя проверка', auto_now_add=True)

    def __str__(self):
        return f"Оборудование '{self.name}'. Последняя проверка: {self.last_update}"

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"


#МФУ


class MFPType(models.Model):
    name = models.CharField(verbose_name='Имя типа', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип МФУ"
        verbose_name_plural = "Типы МФУ"

class MFP(models.Model):
    equipment = models.OneToOneField(Equipment, verbose_name='Какое оборудование является МФУ?',  on_delete=models.CASCADE, primary_key=True)
    is_wb = models.BooleanField(verbose_name='Черно-белый?', default=False)
    format = models.CharField(verbose_name='Формат печати', max_length=50)
    colour_copy_amount = models.IntegerField(verbose_name='Количество напечатанных цветных страниц', default=0)
    black_copy_amount = models.IntegerField(verbose_name='Количество напечатанных ЧБ страниц', default=0)
    mfp_type = models.ForeignKey(MFPType, verbose_name='Тип МФУ', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.equipment.name} - {self.mfp_type.name} МФУ, {'Черно-белый' if self.is_wb else 'Цветной'}. Формат печати: {self.format}"

    class Meta:
        verbose_name = "МФУ"
        verbose_name_plural = "МФУ"


class MFPColour(models.Model):
    name = models.CharField(verbose_name='Имя цвета картриджа', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет картриджа"
        verbose_name_plural = "Цвета картриджей"


class MFPCartridge(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    mfp = models.ForeignKey(MFP, verbose_name='К какому МФУ картридж?',  on_delete=models.CASCADE)
    mfp_colour = models.ForeignKey(MFPColour, verbose_name='Цвет картриджа',  on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена', default=0)
    storage_amount = models.IntegerField(verbose_name='Количество на складе', default=0)
    page_resource = models.IntegerField(verbose_name='Ресурс страниц', default=0)
    commentary = models.TextField(verbose_name='Комментарий к картриджу', blank=True, default='')
    url = models.TextField(verbose_name='Ссылка на картридж для покупки', blank=True, default='')
    last_change_date = models.DateTimeField(verbose_name='Последнее обновление', auto_now_add=True)

    def __str__(self):
        return f"Картридж для {self.mfp.equipment.name} - {self.mfp_colour.name}. Ссылка для покупки: {self.url}. Последнее обновление: {self.last_change_date}"

    class Meta:
        verbose_name = "Картридж для МФУ"
        verbose_name_plural = "Картриджи для МФУ"


#Компьютер

class PC(models.Model):
    equipment = models.OneToOneField(Equipment, verbose_name='Какое оборудование является ПК?',  on_delete=models.CASCADE, primary_key=True)
    characteristics = models.TextField(verbose_name='Характеристики')

    def __str__(self):
        return f"ПК {self.equipment.name}"

    class Meta:
        verbose_name = "ПК"
        verbose_name_plural = "ПК"


#Заявки

class RequestStatus(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя статуса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус заявки"
        verbose_name_plural = "Статусы заявок"


class Requests(models.Model):
    employee = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.CASCADE)
    status = models.ForeignKey(RequestStatus, verbose_name='Статус заявки',  on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, verbose_name='Оборудование',  on_delete=models.CASCADE)
    commentary = models.TextField(verbose_name='Комментарий')
    date_of_request = models.DateTimeField(verbose_name='Дата заявки', auto_now_add=True)
    date_of_last_update = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)

    def __str__(self):
        return f"Заявка на {self.equipment.name}. Дата от: {self.date_of_request}. Последнее изменение - {self.date_of_last_update}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
