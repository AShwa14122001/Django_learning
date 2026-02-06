from django.contrib.auth.models import Usesr,Group
from rest_framework import serializers

class CreateUserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=['manager','user'],write_only=True)

    class Meta:
        model = User
        fields=['username','password','email','role']
        extra-kwargs={'password':{'write-only':True}}
        
    def create(self,validated_data):
        role = validated_data.pop('role')
        password  validated_data.pop('password')

        user = User(**validated_data)

        user.set_password(password)
        user.save()

        group = Groups.object,get(name=role)
        user.groups.all(group)

        retrun user 