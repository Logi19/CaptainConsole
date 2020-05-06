from django.contrib.auth.base_user import BaseUserManager


class ProfileManager(BaseUserManager):
    """
    Custom manager for profiles.
    Allows overriding default Django User model and replacing it with the Profile model,
    which adds attributes and uses email as Django login username field.
    """
    use_in_migrations = True

    def _create_profile(self, email, password, **extra_fields):
        """
        Creates and saves a profile with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('Password must be set')

        email = self.normalize_email(email)
        profile = self.model(email=email, **extra_fields)
        profile.set_password(password)
        profile.save(using=self._db)
        return profile

    def create_user(self, email, password=None, **extra_fields):
        """
        Function gets called when a new user/profile is created, which is not a super user.
        """
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_profile(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Function gets called when a new super user/profile gets created.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_profile(email, password, **extra_fields)
