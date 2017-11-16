from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# 博文列表
class Articles(models.Model):
    id = models.AutoField('ID', primary_key=True)
    title = models.CharField('标题', max_length=100)
    picture = models.ImageField('图片', upload_to='uploadImages', null=True, blank=True)
    date = models.DateTimeField('时间', auto_now=True)
    describe = models.TextField('描述')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章列表'


# 正文内容
class Content(models.Model):
    id = models.OneToOneField(Articles, primary_key=True)
    content = RichTextUploadingField('正文')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '正文'
        verbose_name_plural = '正文'


# 联系
class Contact(models.Model):
    id = models.AutoField('ID', primary_key=True)
    name = models.CharField('姓名', max_length=100)
    email = models.CharField('邮箱', max_length=100)
    message = models.TextField('内容')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '反馈'
        verbose_name_plural = '反馈列表'
