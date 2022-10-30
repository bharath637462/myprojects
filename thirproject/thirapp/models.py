from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, is_staff=False, is_superuser=False, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    is_staff = models.BooleanField(_('Staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    active = models.BooleanField(_('Active'), default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return f'{self.first_name}[{self.email}]'

    def has_perm(self, perms):
        """
        Return True if the user has the specified permission. Query all
        available auth backends, but return immediately if any backend returns
        True. Thus, a user who has permission from a single auth backend is
        assumed to have permission in general. If an object is provided, check
        permissions for that object.
        """
        # Active superusers have all permissions.
        if self.active and self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return False

    def has_module_perms(self, app_label):
        """
        Return True if the user has any permissions in the given app label.
        Use similar logic as has_perm(), above.
        """
        # Active superusers have all permissions.
        if self.active and self.is_superuser:
            return True

        return False


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Material(models.Model):
    category = models.ForeignKey(Category, related_name='materials', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Order(models.Model):
    materials = models.ManyToManyField(Material, related_name='orders')
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    materials = models.ForeignKey(Material, related_name='reviews', on_delete=models.CASCADE)
    review = models.CharField(max_length=100, null=True, blank=True)
