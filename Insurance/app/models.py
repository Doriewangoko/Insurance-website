from django.db import models
from django.conf import settings

# Model to handle file uploads
class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/', help_text="Upload a PDF or image")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} uploaded at {self.uploaded_at}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

