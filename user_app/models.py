# from django.db import models
# # from .managers import CustomUserManager
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager
# from django.contrib.auth.hashers import make_password


# class CustomUserManager(BaseUserManager):

#     def _create_user(self, email, password, **extra_fields):
#         email = self.normalize_email(email)
#         user = CustomUser(email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("user_type", 1)
#         extra_fields.setdefault("last_name", "System")
#         extra_fields.setdefault("first_name", "Administrator")

#         assert extra_fields['is_staff']
#         assert extra_fields['is_superuser']
#         return self._create_user(email, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = None  # removed , using email instead
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=120)
#     last_name = models.CharField(max_length=120)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()

#     def __str__(self):
#         return self.last_name + " " + self.first_name
