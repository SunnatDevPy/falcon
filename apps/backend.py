from typing import Optional

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class CustomModelBackend(ModelBackend):

    def authenticate(
            self,
            phone: Optional[str] = None,
            password: Optional[str] = None,
            **kwargs
    ) -> Optional[User]:
        if phone is None:
            phone = kwargs.get(User.USERNAME_FIELD)

        if phone is None or password is None:
            return None

        try:
            user = User.objects.get_by_natural_key(phone)
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(
                    user
            ):
                return user
            return None


class PhoneBackend(ModelBackend):
    def authenticate(
            self, request, phone=None, password=None, **kwargs
    ):
        if phone is None or password is None:
            return None

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None
