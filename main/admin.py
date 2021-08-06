from django.contrib import admin
from .models import App, EduProgram
from django.utils.safestring import mark_safe

@admin.register(App)
class AppAdmin(admin.ModelAdmin):


    list_display = ("surname", "name", "otch", "phone",)
    list_filter = ("language", "edu_program",)
    search_fields = ("surname", "name", "otch",)
    readonly_fields = ("admin_image", "admin_image2", "admin_image3", 'file_link',)
    fields = ("surname", "name", "otch", "phone", "edu_program", "language", "admin_image", "admin_image2", "admin_image3",'zayavka','fluro','zdorovie','photo', 'file_link',)

    def admin_image(self, obj):
        return mark_safe('<img src="%s"/ width="300" height="200">' % obj.id_card_front.url)

    admin_image.short_description = "Уд.лич лицевая"
    def admin_image2(self, obj):
        return mark_safe('<img src="%s"/ width="300" height="200">' % obj.id_card_back.url)

    admin_image2.short_description = "Уд.лич обратная"
    def admin_image3(self, obj):
        return mark_safe('<img src="%s"/ width="300" height="200">' % obj.diplom.url)

    admin_image3.short_description = "Диплом"

admin.site.register(EduProgram)