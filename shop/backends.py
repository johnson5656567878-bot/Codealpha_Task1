from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Custom authentication backend that allows users to authenticate
    using either their username or their email address.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if not username or not password:
            return None

        try:
            # Match either exact username or case-insensitive email
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except User.DoesNotExist:
            # Run the default password hasher once to prevent timing attacks
            User().set_password(password)
            return None
        except User.MultipleObjectsReturned:
            # If multiple accounts have the same email, prioritize username
            user = User.objects.filter(username__iexact=username).first()
            if not user:
                user = User.objects.filter(email__iexact=username).order_by('id').first()

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
