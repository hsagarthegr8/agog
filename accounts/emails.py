from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail, EmailMessage


class ActivationEmail():
    subject = 'Activate Your Account'
    from_email = 'accounts@agog.com'
    template = get_template('accounts/emails/email_verify.html')

    def __init__(self, to, url):
        self.to = to
        self.context = {
            'activation_url':url
        }
        self.message = self.template.render(self.context)

    def send(self):
        msg = EmailMessage(subject=self.subject,body=self.message,from_email=self.from_email,to=self.to)
        msg.content_subtype = 'html'
        msg.send(fail_silently=False)


