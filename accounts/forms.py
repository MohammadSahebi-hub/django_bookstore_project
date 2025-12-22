from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Signup
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'email',)

# Admin
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'email',)