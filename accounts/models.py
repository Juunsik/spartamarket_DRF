from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, name, nickname, birth, password=None):

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            nickname=nickname,
            birth=birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, name, nickname, birth, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            name=name,
            nickname=nickname,
            birth=birth,
        )
        user.is_admin = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    GENDER_CHOICES = {
        ("N", "Undefined"),
        ("M", "Male"),
        ("F", "Female"),
    }

    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField(
        max_length=150,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    name = models.CharField(max_length=150)
    nickname = models.CharField(max_length=100)
    birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="N")
    description = models.TextField(max_length=200, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name", "nickname", "birth"]

    def __str__(self):
        return self.username
