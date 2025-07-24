from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLES = (
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

#Conversation model.

class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField('User', related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"


#messaging model

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name='messages_sent')
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} from {self.sender}"


#user model

class User(AbstractUser):
    USER_ROLES = (
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    created_at = models.DateTimeField(auto_now_add=True)