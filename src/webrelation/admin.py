from django.contrib import admin
from models import Friendship

# Register your models here.

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    pass
