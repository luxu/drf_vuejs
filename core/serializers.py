from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Prisoner


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        )


class PrisonerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prisoner
        fields = (
            'id',
            'name',
            'matriculation',
            'created_at',
            'updated_at',
        )
