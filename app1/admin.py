from django.contrib import admin

# Register your models here.
from .models import Coin
from .models import Customer

admin.site.register(Customer)
