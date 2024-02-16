#Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings


def send_email(
	from_email, 
		to_email, 
		subject, 
		template_name, 
		context, 
		attachment=None, 
		attachment_name='export.xlsx',
		attachment_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
	):

		plaintext = get_template('emails/{}.txt'.format(template_name))
		html = get_template('emails/{}.html'.format(template_name))

		text_content = plaintext.render(context)
		html_content = html.render(context)
		if settings.DEBUG:
			to_email = to_email
		else:
			to_email = to_email

		final_toemail = [to_email] if type(to_email) == str else to_email
		msg = EmailMultiAlternatives(subject, text_content, from_email, final_toemail)
		msg.attach_alternative(html_content, "text/html")
		if attachment:
			msg.attach(attachment_name, attachment, attachment_type)
		msg.send()