from django.apps import AppConfig


class ManagerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manager_app'

from django.apps import AppConfig
import threading

class FileuploadConfig(AppConfig):
    name = 'manager_app'

    def ready(self):
        from .echo_bot import main as start_bot
        bot_thread = threading.Thread(target=start_bot)
        bot_thread.setDaemon(True)
        bot_thread.start()