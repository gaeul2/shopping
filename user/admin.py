from django.contrib import admin
from user.models import User as UserModel
from user.models import Review as ReviewModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(ReviewModel)