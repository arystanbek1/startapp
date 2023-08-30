from rest_framework import serializers
from product.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['TOO_IP', 'Organization', 'Iin', 'Director',
                  'Number1', 'Job1', 'Finished_project', 'city', 'consideration',
                  'status_account', 'test',
                  ]

    def to_representation(self, instance):
        representation = dict()
        representation['too_ip'] = instance.TOO_IP.name
        representation['organization'] = instance.Organization
        representation['iin'] = instance.Iin
        representation['director'] = instance.Director
        representation['number1'] = instance.Number1
        representation['job1'] = instance.Job1.job
        representation['finished_project'] = instance.Finished_project
        # representation['file'] = instance.file
        representation['city'] = instance.city.name
        representation['status_account'] = instance.status_account.status
        representation['consideration'] = instance.consideration
        return representation



