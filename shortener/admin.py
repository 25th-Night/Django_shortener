from django.contrib import admin
from shortener.models import PayPlan, Users, Statistic

# Register your models here.

admin.site.register(Users)
admin.site.register(PayPlan)
admin.site.register(Statistic)