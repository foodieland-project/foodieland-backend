from .managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.html import format_html


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(max_length=125, unique=True)
    is_author = models.BooleanField(
        default=False, help_text='Determines whether this user is allowed to write an article')
    special_user = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(
        default="default-pic.jpg", upload_to="media/users-pics/", null=True, blank=True)

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # backend = 'accounts.authentication.EmailBackend'

    def thumbnail(self):
        if self.avatar:
            return format_html("<img width=40 height=40 style='border-radius: 20px;' src='{}'>".format(self.avatar.url))
        return "nothing"
    thumbnail.short_description = "thumbnail"

    def __str__(self):
        if self.email == None:
            return "Email cant be none"
        return self.email
