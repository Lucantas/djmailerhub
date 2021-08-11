from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from restapi.models import MailConf
from restapi.serializers import MailConfSerializer

class MailConfView(APIView, UpdateModelMixin, DestroyModelMixin):
    def get(self, request, id=None):
        if id:            
            try:
                queryset = MailConf.objects.get(id=id)
            except MailConf.DoesNotExist:
                return Response({'errors': 'This mailconf item does not exist.'}, status=400)

            read_serializer = MailConfSerializer(queryset)

        else:
            queryset = MailConf.objects.all()

            read_serializer = MailConfSerializer(queryset, many=True)

            return Response(read_serializer.data)


    def post(self, request):
        create_serializer = MailConfSerializer(data=request.data)

        if create_serializer.is_valid():
            mailconf_item_object = create_serializer.save()

            read_serializer = MailConfSerializer(mailconf_item_object)

            return Response(read_serializer.data, status=201)

        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
            mailconf_item = MailConf.objects.get(id=id)
        except MailConf.DoesNotExist:
            return Response({'errors': 'This mailconf item does not exist.'}, status=400)

        update_serializer = MailConfSerializer(mailconf_item, data=request.data)

        if update_serializer.is_valid():
            mailconf_item_object = update_serializer.save()

            read_serializer = MailConfSerializer(mailconf_item_object)

            return Response(read_serializer.data, status=200)

        return Response(update_serializer.errors, status=400)


    def delete(self, request, id=None):
        try:
            mailconf_item = MailConf.objects.get(id=id)
        except MailConf.DoesNotExist:
            return Response({'errors': 'This mailconf item does not exist.'}, status=400)

        mailconf_item.delete()

        return Response(status=204)
