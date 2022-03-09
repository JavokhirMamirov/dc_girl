from django.contrib import admin

# Register your models here.
from home.models import Question, User

admin.site.register(Question)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'javoblar']

    def javoblar(self, obj):
        return "\n".join([f"{a.query.query} : {a.answer}" for a in obj.answer.all()])
