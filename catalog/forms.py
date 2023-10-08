from django import forms

from catalog.models import Product, Version, Category, Contacts

stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
              'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class MixinForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('date_modified', 'owner')

    def clean_name(self):
        clean_name = self.cleaned_data.get('name')
        for word in stop_words:
            if word in clean_name.lower():
                raise forms.ValidationError('Название не может содержать запрещённые слова')
        return clean_name

    def clean_description(self):
        clean_description = self.cleaned_data.get('description')
        for word in stop_words:
            if word in clean_description.lower():
                raise forms.ValidationError('Описание не может содержать запрещённые слова')
        return clean_description


class VersionForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('product',)

    def clean_product(self):
        cleaned_data = super().clean()
        product = self.instance.product
        current_version = cleaned_data.get('current_version')
        if current_version and product.versions.filter(current_version=True).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Только одна версия может быть активной')


class ContactForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
