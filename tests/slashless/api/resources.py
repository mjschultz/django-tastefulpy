from django.contrib.auth.models import User
from tastefulpy import fields
from tastefulpy.resources import ModelResource
from tastefulpy.authorization import Authorization
from basic.models import Note


class UserResource(ModelResource):
    class Meta:
        resource_name = 'users'
        queryset = User.objects.all()
        authorization = Authorization()


class NoteResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    
    class Meta:
        resource_name = 'notes'
        queryset = Note.objects.all()
        authorization = Authorization()
