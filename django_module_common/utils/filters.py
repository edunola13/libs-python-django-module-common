# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers


class MongoFilter(serializers.Serializer):
    # define fields

    ordering = serializers.ChoiceField(default="-created_at", choices=[
        'created_at', '-created_at'
    ])

    def validate(self, data):
        # Override that you need
        return data

    def filter(self, queryset, additionals={}):
        order = self.validated_data.pop('ordering')

        query = self.validated_data
        query.update(additionals)

        queryset = queryset.find(query)
        queryset = queryset.sort(
            order.strip("-"),
            1 if order[0] != '-' else -1
        )

        return queryset
