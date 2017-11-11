from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# 博文列表
class Articles(models.Model):
    id = models.AutoField('ID', primary_key=True)
    title = models.CharField('标题', max_length=100)
    picture = models.ImageField('图片', upload_to='uploadImages', null=True)
    date = models.DateField('时间', max_length=30)
    describe = models.TextField('描述')

    def __str__(self):
        return self.title


# 正文内容
class Content(models.Model):
    id = models.OneToOneField(Articles, primary_key=True)
    content = RichTextUploadingField('内容')

    def __str__(self):
        return str(self.id)


# 联系
class Contact(models.Model):
    id = models.AutoField('ID', primary_key=True)
    name = models.CharField('姓名', max_length=100)
    email = models.CharField('邮箱', max_length=100)
    message = models.TextField('内容')

    def __str__(self):
        return self.name
