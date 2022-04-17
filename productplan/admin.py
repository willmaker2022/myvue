from django.contrib import admin
from .models import Productplan, ProcessAssemble,ProcessElPrepare,ProcessMePrepare,\
    ProcessScPrepare,ProcessTesting,ProductHistory

# Register your models here.
admin.site.register(Productplan)
admin.site.register(ProcessAssemble)
admin.site.register(ProcessElPrepare)
admin.site.register(ProcessMePrepare)
admin.site.register(ProcessScPrepare)
admin.site.register(ProcessTesting)
admin.site.register(ProductHistory)