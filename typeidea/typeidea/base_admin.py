from django.contrib import admin
"""
用来自动补充文章，分类，侧边栏
"""
class BaseOwnerAdmin(admin.ModelAdmin):
    exclude = ('owner',)
    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request.request, obj, form, change)