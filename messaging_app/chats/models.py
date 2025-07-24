from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    # `password`, `username`, `email`, etc., are inherited from AbstractUser
    def __str__(self):
        return self.username

class Conversation(models.Model):
    conversation_id = models.AutoField(primary_key=True)
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id}"

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.message_id} from {self.sender}"
