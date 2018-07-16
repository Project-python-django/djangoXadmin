from django.contrib import admin

# Register your models here.
import xadmin
from .models import BlogType, Blog
from xadmin import views


# 后台主题功能
class AdminSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "博客后台"
    site_footer = "AlfredPad@outlook.com"

    # 菜单样式变为响应式
    menu_style = "accordion"



class BlogTypeAdmin(object):
    list_display = ('id', 'type_name')
    # list_display_links = ('type_name')  # 使可点击并进入编辑模式



class BlogAdmin(object):
    list_display = ('title', 'author', 'blog_type', 'content', 'create_time', 'modify_time')

    def query(self):
        qs = super(BlogAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)



# 注册功能
xadmin.site.register(views.BaseAdminView, AdminSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(BlogType, BlogTypeAdmin)