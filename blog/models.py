from django.db import models
from xadmin.plugins.auth import User
from DjangoUeditor.models import UEditorField


class BlogType(models.Model):
    type_name = models.CharField(max_length=20, verbose_name='标签名')

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'blog_type'
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name


class Blog(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name='标签')
    content = UEditorField(verbose_name='内容', width=600, height=300, toolbars='full', imagePath='static/media/', filePath='static/media/', blank=True, default="")
    create_time = models.DateTimeField(auto_now_add=True ,verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')


    def __str__(self):
        return self.title


    class Meta:
        db_table = 'blog_name'
        verbose_name = '博客'
        verbose_name_plural = verbose_name

class ArticleAdmin(object):

    # TODO 注意这里是content字段是你要换成ueditor的字段，我这里就被坑了，好长时间不知道BUG出现在哪
    style_fields = {'content': 'ueditor'}