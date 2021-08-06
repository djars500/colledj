from django.db import models
from django.core.paginator import PageNotAnInteger
from django.utils.safestring import mark_safe

class EduProgram(models.Model):
    name = models.CharField('Образовательная программа', max_length=255)

    class Meta:
        verbose_name = "Образовательную программу"
        verbose_name_plural = "Образовательные программы"

    def __str__(self):
        return self.name

class App(models.Model):

    lang = (
        ('Русский', 'Русский'),
        ('Казахский', 'Казахский'),
    )

    surname = models.CharField('Фамилия', max_length=255)
    name = models.CharField('Имя', max_length=255)
    otch = models.CharField('Отчество', max_length=255, null=True, blank=True, default="")
    phone = models.CharField('Номер телефона', max_length=11)
    edu_program = models.ForeignKey(EduProgram, on_delete=models.CASCADE, verbose_name='Образовательная программа')
    language = models.CharField('Язык обучения', choices=lang, max_length=255)
    id_card_front = models.FileField('Уд.лич лицевая', upload_to='id_card/', null=True, blank=True)
    id_card_back = models.FileField('Уд.лич обратная', upload_to='id_card/', null=True, blank=True)
    diplom = models.FileField('Диплом', upload_to='diplom/')
    zayavka = models.FileField('Заявка для приема на учебу', upload_to='zayavka/')
    fluro = models.FileField("075-y(флюрография)", upload_to="fluro/")
    zdorovie = models.FileField("063-y(Паспорт о здоровье)", upload_to="zdorovie/")
    photo = models.FileField("3x4 фото", upload_to="photo/")

    def file_link(self):
        try:
            return mark_safe("<a href='%s'>download</a>" % (self.id_card_front.url))
        except PageNotAnInteger:
            return mark_safe("<a href=127.0.0.1:8000/main>download</a>")

    file_link.allow_tags = True
    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = "Заявку"
        verbose_name_plural = "Заявки"

# # окуга кабылдау туралы отиниш
# # билим туралы кужат
# # 075-у нысаны бойынша медициналык аныктама(флюрография)
# # 063-у нысаны бойынша медициналык (денсаулык паспорты)
# # туу туралы куалигин немесе жеке куалигинин коширмеси
# 3х4 фото