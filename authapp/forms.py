from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import User
from django import forms


class UserLoginForms(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForms, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль пользователя'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите пароль пользователя'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль пользователя'
        self.fields['password2'].widget.attrs['placeholder'] = 'Введите пароль повторно '
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserProfileForm(UserChangeForm):
    avatar = forms.ImageField(widget=forms.FileInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'
