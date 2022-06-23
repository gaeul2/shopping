from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.db import models

# Create your models here.

#custom model사용위해
'''Todo create_user와 create_superuser 함수 완성'''
class UserManager(BaseUserManager):
    def create_user(self):
        pass

    def create_supersuer(self):
        pass


class User(AbstractBaseUser):
    username = models.CharField("아이디", max_length=50)
    password = models.CharField("비밀번호", max_length=255) #해쉬화해서 저장알지?
    fullname = models.CharField("이름", max_length=10)
    phone = models.CharField("전화번호", max_length=20)
    email = models.EmailField("이메일")
    is_active = models.BooleanField("활성화 여부",default=0) #장고유저모델의 필수필드
    is_admin = models.BooleanField("관리자 여부", default=0) #장고유저모델의 필수필드
    ROLE = [
        ("판매자", 'Seller'),
        ("일반사용자", "Common_user"),
    ]
    role = models.CharField(
        max_length=50,
        choices=ROLE,
        default="일반사용자",
    )

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

