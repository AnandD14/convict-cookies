from django.contrib import admin
from .models import Cookie, Club, ClubFundraiser

# Register your models here.
admin.site.register(Cookie)
admin.site.register(Club)
admin.site.register(ClubFundraiser)