from django.db import models


class Chapter(models.Model):
    chapter = models.CharField(max_length=100, verbose_name='Наименование раздела')

    class Meta:
        verbose_name = 'Разделы'
        verbose_name_plural = 'Раздел'

    def __str__(self):
        return self.chapter


class Status_Account(models.Model):
    status = models.CharField(max_length=20, verbose_name='статус подписки')

    class Meta:
        verbose_name = 'Статус подписки'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.status


class Job_Chapter(models.Model):
    chapter_foreignkey = models.ForeignKey(Chapter, verbose_name='какому разделу относитя', on_delete=models.CASCADE)
    job = models.CharField(max_length=255, verbose_name='Вид работы')

    class Meta:
        verbose_name = 'Виды работ'
        verbose_name_plural = 'Работа'

    def __str__(self):
        return self.job


class CompanyOrganization(models.Model):
    name = models.CharField('Тип регистрации', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания или Подрядчик'
        verbose_name_plural = 'Компания или Подрядчик'


class Cities(models.Model):
    name = models.CharField('Город', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Город'


class Raiting(models.Model):
    raiting_choice = models.CharField(max_length=3, verbose_name='Рейтинг', default='0')

    def __str__(self):
        return self.attr_name

    class Meta:
        verbose_name = 'Рейтинги'
        verbose_name_plural = 'Рейтинг'


class Organization(models.Model):
    TOO_IP = models.ForeignKey(CompanyOrganization, verbose_name='Тип', on_delete=models.CASCADE, null=True, blank=True)
    Organization = models.CharField(max_length=50, verbose_name='Наименование Организации')
    Iin = models.CharField(max_length=50, verbose_name='БИН или ИИН компании', null=True, blank=True, default=None)
    Director = models.CharField(max_length=255, verbose_name='ФИО директора полностью')
    Number1 = models.CharField(max_length=11, verbose_name='Контактные данные')
    Job1 = models.ForeignKey(Job_Chapter, verbose_name='Виды работ', on_delete=models.CASCADE)
    Finished_project = models.TextField(verbose_name='Ваши завершенные проекты и описание компании')
    file = models.FileField(upload_to='media/', verbose_name='Ваши Комерческое предложение', null=True, blank=True)
    raiting = models.ForeignKey(Raiting, verbose_name='Рейтинг', on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(Cities, verbose_name='Ваш город', on_delete=models.CASCADE)
    status_account = models.ForeignKey(Status_Account, verbose_name='Статус подписки', on_delete=models.CASCADE)
    consideration = models.CharField(max_length=10, verbose_name='Рассмартирваете работать в разных городах?')

    class Meta:
        app_label = 'product'
        verbose_name = 'Подрядные организации'
        verbose_name_plural = 'Данные подрядных организации'

    def __str__(self):
        return self.Organization
