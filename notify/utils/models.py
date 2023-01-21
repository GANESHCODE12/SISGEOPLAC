# ContenType
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.forms import model_to_dict

#Timezone
from django.utils import timezone

# load model
from swapper import load_model

# Signals
from notify.signals import notificar

# Models
from users.models import User

#Django
from django.db import models

#Apps
from Produccion.models import Produccion



class NotificationQueryset(models.QuerySet):

	def leido(self):
		return self.filter(read=True)

	def no_leido(self):
		return self.filter(read=False)

	def marcar_todo_as_leido(self, destiny=None):
		qs = self.read(False)
		if destiny:
			qs = qs.filter(destiny=destiny)

		return qs.update(read=True)

	def marcar_todo_as_no_leido(self, destiny=None):
		qs = self.read(True)
		if destiny:
			qs = qs.filter(destiny=destiny)

		return qs.update(read=False)



class AbstractNotificationManager(models.Manager):
	def get_queryset(self):
		return self.NotificationQueryset(self.Model, using=self._db)

class AbstractNotificacion(models.Model):

	class Levels(models.TextChoices):
		success = 'Success', 'success',
		info = 'Info', 'info',
		wrong = 'Wrong', 'wrong'

	level = models.CharField(choices=Levels.choices, max_length=20, default=Levels.info)

	destiny = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones', blank=True, null=True)

	actor_content_type = models.ForeignKey(ContentType, related_name='notificar_actor', on_delete=models.CASCADE)
	object_id_actor = models.PositiveIntegerField()
	actor = GenericForeignKey('actor_content_type', 'object_id_actor')

	verbo = models.ForeignKey(Produccion, on_delete=models.CASCADE, related_name='Produccion', blank=True, null=True)

	read = models.BooleanField(default=False)
	publico = models.BooleanField(default=True)
	eliminado = models.BooleanField(default=False)

	timestamp = models.DateTimeField(default=timezone.now, db_index=True)

	objects = NotificationQueryset.as_manager()

	class Meta:
		abstract = True

	def __str__(self):
		return "Actor: {} --- Destiny: {} --- O.P: {} ".format(self.actor.username, self.destiny.username, self.verbo)

	def toJSON(self):
		item = model_to_dict(self)
		return item


def notify_signals(**kwargs):

	destiny = kwargs.pop('destiny')
	actor = kwargs.pop('sender')

	publico = bool(kwargs.pop('publico', True))
	timestamp = kwargs.pop('timestamp', timezone.now())
	verb = kwargs.pop('verb')

	Notify = load_model('notify', 'Notification')
	levels = kwargs.pop('level', Notify.Levels.info)

	destinies = destiny.user_set.all()


	for destiny in destinies:
		if actor.pk != destiny.id:
			notification = Notify(
				destiny=destiny,
				actor_content_type = ContentType.objects.get_for_model(actor),
				object_id_actor = actor.pk,
				verbo_id = verb,
				publico=publico,
				timestamp=timestamp,
				level=levels
			)

			notification.save()


notificar.connect(notify_signals, dispatch_uid='notify.models.Notification')