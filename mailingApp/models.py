from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}
PERIODICITY_CHOICES = [
        ('once', 'Однократно'),
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
        ('yearly', 'ежегодно'),
    ]


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Massage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Periodicity(models.Model):
    name = models.CharField(verbose_name='Название')
    periodicity = models.CharField(max_length=10, choices=PERIODICITY_CHOICES, verbose_name='Периодичность')
    at_last_attempt = models.DateTimeField(verbose_name='Дата последней попытки', **NULLABLE)
    status_attempt = models.BooleanField(verbose_name='Статус', default=False)
    answer_mail = models.CharField(max_length=100, **NULLABLE)


class Setting(models.Model):
    name = models.CharField(max_length=150, verbose_name='Описание настройки')
    at_start = models.DateTimeField(verbose_name='Дата начала отправки', **NULLABLE)
    at_end = models.DateTimeField(verbose_name='Дата окончания отправки', **NULLABLE)
    periodicity = models.ForeignKey(Periodicity, on_delete=models.CASCADE, verbose_name='Периодичность')
    status = models.CharField(max_length=20, verbose_name='Статус', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'настройка'
        verbose_name_plural = 'настройки'


class Mailings(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание рассылки')
    setting = models.ForeignKey(Setting, verbose_name='Настройки рассылки', on_delete=models.CASCADE)
    massage = models.ForeignKey(Massage, verbose_name='Сообщение', on_delete=models.CASCADE)
    client = models.ManyToManyField(Client, verbose_name='Клиент')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
