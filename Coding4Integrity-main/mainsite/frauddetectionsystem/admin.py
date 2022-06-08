from django.contrib import admin

from .models import EnigmaAdmin, User, USSD, Mlmodel, Investigation
# Register your models here.
admin.site.register(EnigmaAdmin)
admin.site.register(User)
admin.site.register(Mlmodel)
admin.site.register(USSD)
admin.site.register(Investigation)