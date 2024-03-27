from djongo import models


class EmbeddedDiscussion(models.Model):
    user = models.ObjectIdField()
    texte = models.TextField()
    date = models.DateTimeField()


class ModelDiscussion(models.Model):
    _id = models.ObjectIdField()
    id_conv = models.CharField()
    id_utilisateur = models.models.ArrayField(
        model_container=models.ObjectIdField()
    )
    messages = models.ArrayField(
        models.EmbeddedField(model_container=EmbeddedDiscussion),
        default=list,
    )

    class Meta:
        db_table = "conversation"
