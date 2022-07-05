from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.db import models

# Create your models here.

#custom model사용위해
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('username이 필요합니다.')
        user = self.model(
            username = username,
            is_seller=0,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    #python manage.py createsuperuser 사용시 이 함수사용함.
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("아이디", max_length=50, unique=True)#아이디로 사용하려면 unique해야함
    password = models.CharField("비밀번호", max_length=255) #해쉬화해서 저장알지?
    fullname = models.CharField("이름", max_length=10)
    phone = models.CharField("전화번호", max_length=20)
    email = models.EmailField("이메일")
    is_active = models.BooleanField("활성화 여부",default=0) #장고유저모델의 필수필드
    is_admin = models.BooleanField("관리자 여부", default=0) #장고유저모델의 필수필드
    is_seller = models.BooleanField("판매자 여부")
    created_at = models.DateTimeField(auto_now_add= True)

    #id로 사용할 필드
    USERNAME_FIELD = 'username'

    object = UserManager()

    def __str__(self):
        return self.fullname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    #admin권한 설정
    @property
    def is_staff(self):
        return self.is_admin




