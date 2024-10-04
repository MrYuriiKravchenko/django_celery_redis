import os
from celery import Celery

# Установка переменной окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')
# Создание экземпляра Celery
app = Celery('publish', broker_connection_retry=False,
             broker_connection_retry_on_startup=True, )
# Загрузка настроек из конфигурационного файла Django
app.config_from_object('django.conf:settings')
# Отключение повторного подключения к брокеру задач
broker_connection_retry = False

# Автоматическое обнаружение задач
app.autodiscover_tasks()

