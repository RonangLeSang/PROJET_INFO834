from djongo import models


class ModelUser(models.Model):
    _id=models.ObjectIdField()
    username = models.CharField(max_length = 255)
    password =  models.CharField(max_length =255)
    conversation = models.ArrayField(
        model_container = models.ObjectIdField(),
        default = list,
    )
    class Meta:
        db_table = "user_collection"
    
    """
class ModelConversation(models.Model):
    _id = models.ObjectIdField()
    users = models.ArrayField(
        id_user = models.ObjectIdField(),
        default = list,
    )
    id_conv = models.CharField()
    class Meta:
        db_table = "conversation_collection"
        """


class EmbeddedDiscussion(models.Model):
    user = models.ObjectIdField()
    texte = models.TextField()
    date = models.DateTimeField()

class ModelDiscussion(models.Model):
    _id = models.ObjectIdField()
    id_conv = models.CharField()
    id_utilisateur = models.models.ArrayField(
        model_container = models.ObjectIdField()
    )
    messages =models.ArrayField(
        models.EmbeddedField(model_container=EmbeddedDiscussion),
        default = list,
        )
    class Meta:
        db_table = "conversation"