  
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.fields import NullBooleanField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
import uuid


class CustomUserManager(BaseUserManager):
    """custom user email where email is unique.
    We can also pass Full name , email and password here"""

    def create_user(self, email, password, **extra_fields):
        """Create and save a User given email and password"""
        if not email:
            raise ValueError(_("The Email is must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save Super user with given email address"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Supperuser must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Supperuser must have is_superuser=True"))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(null=True,max_length=200,verbose_name='Username',unique=True,blank=True)
    email = models.EmailField(_('email_address'), unique=True)

    password = models.CharField(max_length=10000)
    confirm_password = models.CharField(max_length=10000)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Teacher(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, related_name='teachers')
    image = models.ImageField(null=True, blank=True, upload_to='teacher/')
    name = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(verbose_name='Phone Number',null=True,blank=True)
    
    def __str__(self):   
        return self.name

    class Meta:
        verbose_name_plural = 'Teacher'

class Student(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, related_name='students')
    name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='student/')
    phone = models.IntegerField(null=True,blank=True,verbose_name='Phone Number')
    
    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name_plural = 'Student'