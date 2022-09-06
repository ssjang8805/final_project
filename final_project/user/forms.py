from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import check_password

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        error_messages={"required": "이메일을 입력해주세요."}, max_length=64, label="이메일"
    )
    username = forms.CharField(
        error_messages={"required": "유저이름을 입력해주세요."},
        label="유저명",
    )
    password1 = forms.CharField(
        error_messages={"required": "비밀번호를 입력해주세요."},
        widget=forms.PasswordInput,
        label="비밀번호",
    )
    password2 = forms.CharField(
        error_messages={"required": "비밀번호를 입력해주세요."},
        widget=forms.PasswordInput,
        label="비밀번호 확인",
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

class LoginForm(forms.Form):
    # TODO: 2. login 할 때 form을 활용해주세요
    username = forms.CharField(
        error_messages={"required": "유저이름을 입력해주세요."},
        max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'from-control','placeholder':"사용자 이름"})
    )

    password = forms.CharField(
        error_messages={"required": "비밀번호를 입력해주세요."},
        max_length=30, required=True,
        widget=forms.PasswordInput(attrs={'class': 'from-control','placeholder':"패스워드"})
    )