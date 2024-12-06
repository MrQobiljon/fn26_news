from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = 'Kategoriyalar'


class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name="Maqola nomi")
    content = models.TextField(blank=True, null=True, verbose_name="Maqola matni")
    photo = models.ImageField(upload_to="post/photos/", blank=True, null=True, verbose_name="Rasmi")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarish",
                                    help_text="Agar galochka qo'ysangiz sayta chiqaradi!!!")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'
        ordering = ['-created', '-pk']
