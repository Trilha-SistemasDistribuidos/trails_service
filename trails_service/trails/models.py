from django.db import models

class Trail(models.Model):
    user_id = models.IntegerField()  # ID do usuário (vindo do users_service)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=50, choices=[
        ('easy', 'Fácil'),
        ('medium', 'Médio'),
        ('hard', 'Difícil'),
    ])
    length_km = models.FloatField()
    category_id = models.IntegerField()  # ID da categoria (comunicação com categories_service)
    date_time = models.DateTimeField()
    # Novo campo para imagem
    image = models.ImageField(
        upload_to='trail_images/',
        null=True,
        blank=True,
        help_text='Imagem representativa da trilha'
    )

    def __str__(self):
        return self.name