from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import ShopUser
from mainapp.models import Category, Product


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')


class ShopUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs.update({'class': 'form-control'})
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды!')
        return data

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2',
                  'email', 'age', 'avatar')


class ShopUserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды!')
        return data

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

class ShopUserDeleteForm(forms.ModelForm):
    class Meta:
        model = ShopUser
        fields = ()


class ShopCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopCategoryDeleteForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ()


class ShopProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'image', 'short_desc', 'description', 'price', 'quantity')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'image', 'short_desc', 'description', 'price', 'quantity')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ()
