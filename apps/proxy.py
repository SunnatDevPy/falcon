from django.db.models import Manager

from apps.models import User, Order


class TypeManager(Manager):
    def get_type(self, type):
        return super().get_queryset().filter(type=type)


class AdminManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Type.ADMIN)


class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'


class OperatorManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Type.OPERATOR)


class Operator(User):
    objects = OperatorManager()

    class Meta:
        proxy = True
        verbose_name = 'Operator'
        verbose_name_plural = 'Operators'


class Manager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Type.MANAGER)


class CustomManager(User):
    objects = Manager()

    class Meta:
        proxy = True
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'


class DriverManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Type.DRIVER)


class Driver(User):
    objects = DriverManager()

    class Meta:
        proxy = True
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'


class UserManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Type.USER)


class UserClient(User):
    objects = UserManager()

    class Meta:
        proxy = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class NewOrderManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Order.Type.NEW)


class NewOrder(Order):
    objects = NewOrderManager()

    class Meta:
        proxy = True
        verbose_name = 'NewOrder'
        verbose_name_plural = 'New Orders'


class ArchiveOrderManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Order.Type.ARCHIVE)


class ArchiveOrder(Order):
    objects = ArchiveOrderManager()

    class Meta:
        proxy = True
        verbose_name = 'ArchiveOrder'
        verbose_name_plural = 'Archive Orders'


class DeliveringOrderManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Order.Type.DELIVERING)


class DeliveringOrder(Order):
    objects = DeliveringOrderManager()

    class Meta:
        proxy = True
        verbose_name = 'DeliveringOrder'
        verbose_name_plural = 'Delivering Orders'


class DeliveredOrderManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Order.Type.DELIVERED)


class DeliveredOrder(Order):
    objects = DeliveredOrderManager()

    class Meta:
        proxy = True
        verbose_name = 'DeliveredOrder'
        verbose_name_plural = 'Delivered Orders'


class BrokenOrderManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Order.Type.BROKEN)


class BrokenOrder(Order):
    objects = BrokenOrderManager()

    class Meta:
        proxy = True
        verbose_name = 'BrokenOrder'
        verbose_name_plural = 'Broken Orders'


class ReturnedOrderManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Order.Type.RETURNED)


class ReturnedOrder(Order):
    objects = ReturnedOrderManager()

    class Meta:
        proxy = True
        verbose_name = 'ReturnedOrder'
        verbose_name_plural = 'Returned Orders'


class CancelledOrderManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Order.Type.CANCELLED)


class CancelledOrder(Order):
    objects = CancelledOrderManager()

    class Meta:
        proxy = True
        verbose_name = 'CancelledOrder'
        verbose_name_plural = 'Cancelled Orders'


class ReadyToDeliveryOrderManager(TypeManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Order.Type.READY_TO_DELIVERY)


class ReadyToDeliveryOrder(Order):
    objects = ReadyToDeliveryOrderManager()
    class Meta:
        proxy = True
        verbose_name = 'ReadyToDeliveryOrder'
        verbose_name_plural = 'Ready To Delivery Orders'



# class BAseModel(ModelAdmin):
#     def get_queryset(self):
#         return super().get_queryset().filter(type=Order.Type.READY_TO_DELIVERY)
#
#     _status = User.Type.USER