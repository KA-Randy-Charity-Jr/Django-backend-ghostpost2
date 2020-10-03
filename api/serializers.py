from rest_framework import serializers
from ghostpost_app.models import Ghostpost


class GhostpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ghostpost
        fields = [
        'id',    
        'text',
        'isboast',
        'post_date',
        'upvotes',
        'downvotes',

        ]


