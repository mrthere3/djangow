from django.contrib.admin import AdminSite
"""设置site样式  将admin和superadmin分割开来"""

class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')