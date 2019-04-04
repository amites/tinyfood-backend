from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

from localflavor.us.models import USPostalCodeField, USStateField


class AbstractContact(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USPostalCodeField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    faceybook = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def address_str(self):
        return '{}, {}, {}, {}'.format(self.address, self.city, self.state, self.zip_code)


class UserProfile(AbstractContact):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    extra_data = models.CharField(max_length=200, null=True, blank=True)


class ProductProfile(AbstractContact):
    product = models.OneToOneField('Product', on_delete=models.CASCADE)
    extra_data = models.CharField(max_length=200, null=True, blank=True)


class FarmRegion(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    state = USStateField(null=True, blank=True)

    def __str__(self):
        return 'Farm Region {}'.format(self.name)


class FarmStyle(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Farm Style {}'.format(self.name)


class FarmBusiness(AbstractContact):
    name = models.CharField(max_length=200, null=True, blank=True)
    farming_style = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    region = models.ForeignKey(FarmRegion, on_delete=models.CASCADE)
    farm_style = models.ForeignKey(FarmStyle, on_delete=models.CASCADE)
    sell_style = models.TextField(null=True, blank=True)
    liasons = models.ManyToManyField(User, related_name='farm_liason', blank=True)
    drivers = models.ManyToManyField(User, related_name='farm_driver', blank=True)

    def __str__(self):
        return 'Farm Business {}'.format(self.name)


class Farmer(models.Model):
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    farm = models.ForeignKey(FarmBusiness, on_delete=models.CASCADE)

    # seasonal_orders_avail: 'geoghub',

    def __str__(self):
        return 'Farmer {}'.format(self.user.username)


class ProductType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return 'Product Type {}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    sale = models.BooleanField(default=False)
    organic = models.BooleanField(default=True)
    producer = models.ForeignKey(FarmBusiness, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return 'Product {}'.format(self.name)


class ProductOrder(models.Model):
    business = models.ForeignKey(FarmBusiness, on_delete=models.CASCADE, null=True, blank=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_customer')
    date = models.DateField()
    driver = models.ForeignKey(User, related_name='order_driver', on_delete=models.CASCADE, null=True, blank=True)
    liason = models.ForeignKey(User, related_name='order_liason', on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product)

    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Product Order {}'.format(self.pk)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.business and not self.farmer:
            raise ValidationError('Must fill in either business or farmer')
        super().save(force_insert=force_insert, force_update=force_update,
                     using=using, update_fields=update_fields)
