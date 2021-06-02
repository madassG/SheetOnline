from django import forms
from django.forms import ModelForm
from sheetCheck.models import Sheet
from django.core.validators import FileExtensionValidator


class SheetSecondForm(forms.Form):
    choices = [
        ('02.20/2020.2-943', '02.20/2020.2-943')
    ]
    sheet_format = forms.ChoiceField(
        required=True,
        label='Формат ведомости',
        widget=forms.TextInput(attrs={'class': "main-content-form__select"}),
        choices=choices,
    )
    cols = forms.CharField(
        required=True,
        label='Столбцы',
        error_messages={'required': 'Введите номера столбцов'},
        widget=forms.TextInput(attrs={'class': "main-content-form__text"})
    )
    file = forms.FileField(
        required=True,
        label='PDF-файл ведомости',
        error_messages={'required': 'Загрузите файл ведомости'},
        widget=forms.TextInput(attrs={'class': "main-content-form__file"}),
        validators=[FileExtensionValidator(['pdf'])],
    )


class SheetForm(ModelForm):
    class Meta:
        model = Sheet
        fields = ['sheet_format', 'columns', 'file']
        widgets = {
            'sheet_format': forms.Select(attrs={
                'class': 'main-content-form__select'
            }),
            'columns': forms.TextInput(attrs={
                'class': 'main-content-form__text'
            }),
            'file': forms.FileInput(attrs={
                'class': 'main-content-form__file'
            })
        }
