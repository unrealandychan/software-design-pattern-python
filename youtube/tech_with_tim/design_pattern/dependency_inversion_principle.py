# Dependency Inversion Principle
# High-level modules should not depend on low-level modules. Both should depend on abstractions.
# Abstractions should not depend on details. Details should depend on abstractions.

# Wrong Example
class EmailNotifier:
    def send_email(self, message: str):
        print(f"Email sent: {message}")


class UserService:
    def __init__(self):
        self.email_notifier = EmailNotifier()  # Tight coupling - high-level module depends on low-level module

    def register(self, username: str):
        self.email_notifier.send_email(f"Welcome {username}")


# Right Example
from abc import ABC, abstractmethod
# We don't have interface in python, but we can use ABC to create an abstract class
# ABC stands for Abstract Base Class
# ABC is a decorator that allows us to create abstract classes in Python
# An abstract class is a class that contains one or more abstract methods

class Notifier(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass


class EmailNotifierNew(Notifier):
    def send_notification(self, message: str):
        print(f"Email sent: {message}")


class SMSNotifier(Notifier):
    def send_notification(self, message: str):
        print(f"SMS sent: {message}")


class PushNotifier(Notifier):
    def send_notification(self, message: str):
        print(f"Push sent: {message}")


class UserServiceNew:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def register(self, username: str):
        self.notifier.send_notification(f"Welcome {username}")
