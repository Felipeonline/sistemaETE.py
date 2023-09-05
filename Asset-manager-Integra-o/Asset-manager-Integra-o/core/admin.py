from django.contrib import admin

# Register your models here.
from .models import ARMAZENAMENTO_1, ARMAZENAMENTO_2, GRADEAMENTO_1,GRADEAMENTO_2
admin.site.register(ARMAZENAMENTO_1)
admin.site.register(ARMAZENAMENTO_2)
admin.site.register(GRADEAMENTO_1)
admin.site.register(GRADEAMENTO_2)