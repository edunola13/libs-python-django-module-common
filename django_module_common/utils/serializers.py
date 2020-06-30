# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.utils.translation import gettext as _
from rest_framework import serializers


class JSONField(serializers.Field):
    default_error_messages = {
        'invalid': _('Value must be valid JSON.')
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        try:
            return json.dumps(data)
        except (TypeError, ValueError):
            self.fail('invalid')

    def to_representation(self, value):
        if value is None:
            return None
        try:
            return json.loads(value)
        except (TypeError, ValueError):
            return "error"
