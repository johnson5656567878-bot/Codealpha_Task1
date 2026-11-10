import re
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Order, NewsletterSubscriber

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create password'}),
        help_text='At least 8 characters with a mix of letters and numbers.'
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("A user with this username already exists.")
        if not re.match(r'^[\w.@+-]+$', username):
            raise ValidationError("Enter a valid username. Letters, digits and @/./+/-/_ only.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("An account with this email address already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                self.add_error('confirm_password', "Passwords do not match.")
            else:
                try:
                    validate_password(password)
                except ValidationError as err:
                    self.add_error('password', err)

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username or email',
            'autocomplete': 'username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'autocomplete': 'current-password'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            self.user = authenticate(username=username, password=password)
            if not self.user:
                raise ValidationError("Invalid username/email or password. Please try again.")
            if not self.user.is_active:
                raise ValidationError("This account is currently disabled.")
        return cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('instance')
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if self.user and User.objects.filter(email__iexact=email).exclude(pk=self.user.pk).exists():
            raise ValidationError("This email is already in use by another account.")
        return email


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'full_name',
            'email',
            'phone',
            'delivery_address',
            'city',
            'state',
            'postal_code',
            'payment_method',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rahul Sharma'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'rahul@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 9876543210'}),
            'delivery_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Flat / House No., Street, Landmark'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mumbai'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maharashtra'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '400001'}),
            'payment_method': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        # Ensure phone has valid format (at least 7 digits, allowed +, spaces, hyphens)
        digits = re.sub(r'\D', '', phone)
        if len(digits) < 8 or len(digits) > 15:
            raise ValidationError("Please provide a valid contact phone number (8-15 digits).")
        return phone

    def clean_postal_code(self):
        postal_code = self.cleaned_data.get('postal_code', '').strip()
        if len(postal_code) < 3 or len(postal_code) > 12:
            raise ValidationError("Please enter a valid postal / PIN code.")
        return postal_code


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'aria-label': 'Email address'
            })
        }
