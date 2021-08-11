from urllib.parse import urlparse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from restapi.models import MailConf
from restapi.serializers import MailConfSerializer
from restapi.mailer import send_mail

class SendMailView(APIView, UpdateModelMixin, DestroyModelMixin):
    authentication_classes = []
    permission_classes = []

    def post(self, request, id=None):
        if id:            
            try:
                mail_conf = MailConf.objects.get(id=id)
            except MailConf.DoesNotExist:
                return Response({'errors': 'This mailconf item does not exist.'}, status=400)

            url = urlparse(request.META['HTTP_REFERER'])
            allow = False
            for allowed_host in mail_conf.allowed_hosts.all():
                if allowed_host.value == url.netloc:
                    allow = True

            if allow:            
                send_mail(
                    mail_conf.sender,
                    mail_conf.receivers_list(),
                    mail_conf.copies_list(),
                    mail_conf.password,
                    mail_conf.subject,
                    mail_conf.body, 
                    mail_conf.login,
                    mail_conf.host,
                    mail_conf.port,
                    request.data
                )
                return Response({'message': 'success'}, status=200)
            else:
                return Response({'errors': 'A origem não é permitida'}, status=403)        


        return Response({'errors': 'No mailconf id informed.'}, status=400)