from django import forms

from catalog.models import Product

stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
              'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('date_modified', 'vers')

    def clean_name(self):
        clean_name = self.cleaned_data.get('name')
        for word in stop_words:
            if word in clean_name.lower():
                raise forms.ValidationError(
                    'Название не может содержать запрещённые слова')
        return clean_name

    def clean_description(self):
        clean_description = self.cleaned_data.get('description')
        for word in stop_words:
            if word in clean_description.lower():
                raise forms.ValidationError(
                    'Описание не может содержать запрещённые слова')
        return clean_description
