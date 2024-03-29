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
STATUS_MAILING = {
    ('create', 'Создана'),
    ('launched', 'Запущена'),
    ('completed', 'Завершена'),
}


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


class Mailing(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание рассылки')
    periodicity = models.CharField(max_length=10, choices=PERIODICITY_CHOICES, verbose_name='Периодичность')
    at_start = models.DateTimeField(verbose_name='Дата начала отправки')
    at_end = models.DateTimeField(verbose_name='Дата окончания отправки')
    status = models.CharField(max_length=20, choices=STATUS_MAILING, verbose_name='Статус', default='create')
    massage = models.ForeignKey(Massage, verbose_name='Сообщение', on_delete=models.CASCADE)
    client = models.ManyToManyField(Client, verbose_name='Клиент')
    next_run = models.DateTimeField(verbose_name='Дата и время отправки')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Attempt(models.Model):
    at_last_attempt = models.DateTimeField(verbose_name='Дата последней попытки', auto_now_add=True)
    status_attempt = models.BooleanField(verbose_name='Статус', default=False)
    answer_mail = models.TextField(max_length=100, **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка', **NULLABLE)

    def __str__(self):
        return 'попытка отправки'

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'
