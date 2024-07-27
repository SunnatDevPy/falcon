from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from apps.models import User, Order, Category, Product
from apps.proxy import Admin, Operator, CustomManager, Driver, UserClient, NewOrder, ArchiveOrder, DeliveringOrder, \
    DeliveredOrder, BrokenOrder, ReturnedOrder, CancelledOrder, ReadyToDeliveryOrder


# Register your models here.
@admin.register(User)
class UserModel(UserAdmin):
    ordering = '-id',

    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone", "password1", "password2"),
            },
        ),
    )

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/jquery.inputmask/5.0.6/jquery.inputmask.min.js',
            'apps/admin/main.js',
        )

    # def get_queryset(self, request):
    #     return super().get_queryset(request).filter(type=self._type)


@admin.register(Admin)
class AdminModelModelAdmin(ModelAdmin):
    pass


@admin.register(Operator)
class OperatorModelModelAdmin(ModelAdmin):
    pass


@admin.register(CustomManager)
class CustomManagerModelModelAdmin(ModelAdmin):
    pass


@admin.register(Driver)
class DriverModelModelAdmin(ModelAdmin):
    pass


@admin.register(UserClient)
class UserClientModelModelAdmin(ModelAdmin):
    pass


@admin.register(NewOrder)
class NewOrderModelModelAdmin(ModelAdmin):
    pass


@admin.register(ArchiveOrder)
class ArchiveOrderModelModelAdmin(ModelAdmin):
    pass


@admin.register(DeliveringOrder)
class DeliveringOrderModelModelAdmin(ModelAdmin):
    pass


@admin.register(DeliveredOrder)
class DeliveredOrderModelModelAdmin(ModelAdmin):
    pass


@admin.register(BrokenOrder)
class BrokenOrderModelModelAdmin(ModelAdmin):
    pass


@admin.register(CancelledOrder)
class CancelledOrderModelModelAdmin(ModelAdmin):
    pass


@admin.register(ReadyToDeliveryOrder)
class ReadyToDeliveryOrderModelAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelModelAdmin(ModelAdmin):
    list_display = 'id', 'name'


@admin.register(Product)
class ProductModelModelAdmin(ModelAdmin):
    list_display = 'id', 'name', 'category', 'image', 'price'


@admin.register(Order)
class OrderModelModelAdmin(ModelAdmin):
    list_display = 'id', 'product', 'user', 'count'

#
# def get_app_list(self, request):
#     custom_order = [
#         _('New Orders'),
#         _('Visit Orders'),
#         _('Ready Orders'),
#         _('Delivery Orders'),
#         _('Delivered Orders'),
#         _('Cancelled Orders'),
#         _('Missed Call Orders'),
#         _('Archived Orders'),
#         _('Courier Users'),
#         _('Operator Users'),
#         _('Manager Users'),
#         _('Admin Users'),
#         _('Users'),
#         # _('Regular Users'),
#         # _('Balance Reports'),
#         _('Orders'),
#         _('Products'),
#         # _('Payments'),
#         # _('Product Images'),
#         # _('Categories'),
#         # _('Competitions'),
#         # _('Regions'),
#         # _('Districts'),
#         # _('Tags'),
#         # _('Site Settings')
#     ]
#
#     app_dict = self._build_app_dict(request)
#     app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
#     for app in app_list:
#         if app['app_label'] == 'apps':
#             app['models'].sort(key=lambda x: custom_order.index(x['name']))
#     return app_list
#
#
# admin.AdminSite.get_app_list = get_app_list
