from django import template


register = template.Library()

@register.filter()
def notificaciones(context):

	user = user_context(context)

	if not user:
		return ''

	return user.notificaciones.no_leido().count()

notificaciones = register.simple_tag(takes_context=True)(notificaciones)

@register.filter()
def notificaciones_info(context):

	user = user_context(context)

	if not user:
		return ''

	return user.notificaciones

notificaciones_info = register.simple_tag(takes_context=True)(notificaciones_info)

def user_context(context):

	if 'user' not in context:
		return None 

	request = context['request']
	user = request.user  

	try:
		user_is_anonymous = user.is_anonymous()
	except TypeError:
		user_is_anonymous = user.is_anonymous

	if user_is_anonymous:
		return None 

	return user