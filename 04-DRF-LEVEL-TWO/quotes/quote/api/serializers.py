from rest_framework import serializers

from django.contrib.auth.models import User

from quote.models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = "__all__"