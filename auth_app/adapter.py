# auth_app/adapter.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Вызывается ПЕРЕД входом через соц. сеть.
        Проверяем есть ли пользователь с таким email.
        """
        # Если пользователь уже залогинен, ничего не делаем
        if sociallogin.is_existing:
            return

        # Получаем email из данных соц. сети
        try:
            email = sociallogin.account.extra_data.get('email', '').lower()
        except:
            return

        if not email:
            return

        # Ищем существующего пользователя с таким email
        try:
            user = User.objects.get(email=email)

            # Связываем соц. аккаунт с существующим пользователем
            sociallogin.connect(request, user)

        except User.DoesNotExist:
            # Пользователя нет - будет создан новый (стандартное поведение)
            pass