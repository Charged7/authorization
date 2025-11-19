# auth_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

def validate_avatar(file: UploadedFile):
    """Валидация загружаемого аватара"""
    # Проверка размера (макс 5MB)
    if file.size > 5 * 1024 * 1024:
        raise ValidationError('Размер файла не должен превышать 5MB')

    # Проверка типа файла
    allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
    if file.content_type not in allowed_types:
        raise ValidationError('Разрешены только изображения (JPEG, PNG, GIF, WebP)')

    # Проверка расширения
    import os
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
        raise ValidationError('Недопустимое расширение файла')


@login_required
def profile(request):
    """Страница профиля пользователя"""
    if request.method == 'POST':
        # Логика обновления профиля
        user = request.user

        # Обновление текстовых полей
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.phone = request.POST.get('phone', '')
        user.bio = request.POST.get('bio', '')

        # Обработка даты рождения
        date_of_birth = request.POST.get('date_of_birth', '')
        if date_of_birth:
            user.date_of_birth = date_of_birth

        # Обработка аватара с валидацией
        if request.FILES.get('avatar'):
            try:
                avatar_file = request.FILES['avatar']
                validate_avatar(avatar_file)
                user.avatar = avatar_file
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('auth_app:profile')

        user.save()
        messages.success(request, 'Профиль успешно обновлен!')
        return redirect('auth_app:profile')

    return render(request, 'auth_app/profile.html', {
        'user': request.user
    })

@login_required
def delete_account(request):
    """Удаление аккаунта пользователя"""
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Ваш аккаунт был успешно удален.')
        return redirect('home')
    return redirect('auth_app:profile')