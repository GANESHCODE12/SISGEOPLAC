# Django
from notify.utils.models import AbstractNotificacion


class Notification(AbstractNotificacion):

	class Meta(AbstractNotificacion.Meta):
		abstract = False
