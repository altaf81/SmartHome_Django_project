from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Phone(models.Model):
    phoneId = models.AutoField(primary_key=True)
    phoneName = models.CharField(max_length=255)
    phonePrice = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    phoneDescription = models.TextField()
    image_url = models.CharField(max_length=2083)

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Phone.objects.filter(category = category_id)
        else:
            return Phone.objects.all()


    def __str__(self):
        return self.phoneName



class CartItem(models.Model):
    phone = models.ForeignKey(Phone,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone.phoneName} - {self.quantity}"

    def get_total_item_price(self):
        return self.quantity * self.phone.phonePrice


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    itemlist = models.ManyToManyField(CartItem)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} {self.itemlist.all()}"

    def __repr__(self) -> str:
        return f"{self.user.username} {len(self.itemlist.all())}"

    def get_total(self):
        total = 0
        for item in self.itemlist.all():
            total += item.get_total_item_price()
        return total




