from .email_notifier import EmailNotifier
from .manager import NotificationsManager

notifications_manager = NotificationsManager()
notifications_manager.register(EmailNotifier())
