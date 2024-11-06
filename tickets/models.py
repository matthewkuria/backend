from django.db import models
from django.conf import settings
import qrcode
from django.db import models
from django.core.files.base import ContentFile
from io import BytesIO
from matches.models import Match

STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('reserved', 'Reserved'),
]


class Ticket(models.Model):
    match = models.ForeignKey(Match,  on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    qr_code_data = models.CharField(max_length=255, unique=True)
    qr_code_image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)  # Optional

    def generate_qr_code(self):
        qr = qrcode.make(self.qr_code_data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        self.qr_code_image.save(f"{self.id}_qr.png", ContentFile(buffer.getvalue()), save=False)
        buffer.close()

    def save(self, *args, **kwargs):
        if not self.qr_code_image:
            self.generate_qr_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket for {self.match} - for {self.owner} -{self.status}"