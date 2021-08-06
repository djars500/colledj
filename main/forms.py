from django import forms
from .models import App, EduProgram

lang = (
        ('Русский', 'Русский'),
        ('Казахский', 'Казахский'),
    )
class AppForm(forms.ModelForm):
    edu_program = forms.ModelChoiceField(queryset=EduProgram.objects.all(), to_field_name="name",widget=forms.Select(attrs={'class': 'custom-select'}) )
    language = forms.ChoiceField(choices=lang, widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = App
        fields = '__all__'
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Ваше фамилия"}),
            'name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Ваше имя"}),
            'otch': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Ваше отчество"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', "placeholder": " +7"}),
            'id_card_front': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Уд лич. лицевая"}),
            'id_card_back': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Уд.лич обратная"}),
            'diplom': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Диплом"}),
            'zayavka': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Заявление на обучение"}),
            'fluro': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Флюрография"}),
            'zdorovie': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Справка о здоровье"}),
            'photo': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "3х4 фото"}),
        }
        # phone
        # edu_program
        # language
        # id_card_front
        # id_card_back
        # diplom
        # zayavka
        # fluro
        # zdorovie
        # photo