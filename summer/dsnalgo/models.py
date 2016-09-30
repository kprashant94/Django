from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class SubArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class PythonCode(models.Model):
    sub_article = models.ForeignKey(SubArticle, on_delete=models.CASCADE)
    code = models.TextField(max_length=5000)

    def __str__(self):
        return self.sub_article.title

class JavaCode(models.Model):
    sub_article = models.ForeignKey(SubArticle, on_delete=models.CASCADE)
    code = models.TextField(max_length=5000)

    def __str__(self):
        return self.sub_article.title

class CCode(models.Model):
    sub_article = models.ForeignKey(SubArticle, on_delete=models.CASCADE)
    code = models.TextField(max_length=5000)

    def __str__(self):
        return self.sub_article.title

