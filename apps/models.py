from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField, IntegerField, SlugField, ImageField, ForeignKey, CASCADE, TextChoices, \
    DateTimeField, TimeField
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField
from django.utils.translation import gettext as _

from apps.manager import CustomUserManager


class User(AbstractUser):
    class Type(TextChoices):
        OPERATOR = 'operator', 'Operator'
        MANAGER = 'manager', 'Manager'
        ADMIN = 'admin', 'Admin'
        DRIVER = 'courier', 'Kuryer'
        USER = 'user', 'Foydalanuvchi'

    username = None
    type = CharField(max_length=50, choices=Type.choices, default=Type.USER, verbose_name='Type')
    image = ResizedImageField(size=[200, 100], upload_to='users', default='default/user.png', verbose_name=_('Rasm'))
    phone = CharField(max_length=255, unique=True, verbose_name=_('Telefon raqam'))
    telegram_id = CharField(max_length=100, verbose_name='Telegram id')
    coins = IntegerField(default=0, db_default=0)
    address = CharField(max_length=255, verbose_name=_('Yashash manzil'))
    description = CKEditor5Field('Text', blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []


class LoveProduct(Model):
    user = ForeignKey('apps.User', CASCADE, related_name='love_product')
    product = ForeignKey('apps.Product', CASCADE, related_name='products')


class FromTimeToTime(Model):
    user = ForeignKey('apps.User', CASCADE, related_name='work_time')
    from_work_time = TimeField(auto_now=True)
    to_work_time = TimeField(auto_now=True)


class Category(Model):
    image = ImageField(upload_to='category', default='default/category.png', verbose_name=_('Rasm'))
    name = CharField(max_length=255, verbose_name=_('Nom'))
    slug = SlugField(unique=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Product(Model):
    category = ForeignKey('apps.Category', CASCADE, related_name='products', verbose_name=_('Id kategoriya'))
    name = CharField('Nom bering', max_length=255)
    price = IntegerField()
    image = ImageField('Rasm', upload_to='product', default='default/img.png')

    description = CKEditor5Field('Text', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(Model):
    class Type(TextChoices):
        NEW = 'new', 'New'
        ARCHIVE = 'archive', 'Archive'
        DELIVERING = 'yetkazilmoqda', 'Yetkazilmoqda'
        DELIVERED = 'yetkazildi', 'Yetkazildi'
        BROKEN = 'nosoz_mahsulot', 'Nosoz mahsulot'
        RETURNED = 'qaytib_keldi', 'Qaytib keldi'
        CANCELLED = 'bekor_qilindi', 'Bekor qilindi'
        READY_TO_DELIVERY = 'dastavkaga_tayyor', "Dastavkaga tayyor"

    type = CharField(max_length=50, choices=Type.choices, default=Type.NEW, verbose_name=_('Buyurtma holati'))
    user = ForeignKey('apps.User', CASCADE, verbose_name='Userni id si', related_name='orders')
    phone = CharField(max_length=255, verbose_name='Userni telefon raqami')
    product = ForeignKey('apps.Product', CASCADE, verbose_name='Productni id si', related_name='orders')
    count = IntegerField(db_default=1, default=1, verbose_name=_('Mahsulot soni'))

    @property
    def total(self):
        return self.count * self.product.price


class Region(Model):
    name = CharField(max_length=255)


class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('apps.Region', CASCADE)
    # user = ForeignKey('apps.User', CASCADE)
