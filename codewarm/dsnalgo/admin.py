from django.contrib import admin
from . models import Article, SubArticle, PythonCode, JavaCode, CCode

admin.site.register(Article)
admin.site.register(SubArticle)
admin.site.register(PythonCode)
admin.site.register(JavaCode)
admin.site.register(CCode)
