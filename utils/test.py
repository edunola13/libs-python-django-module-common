# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APITestCase, APIClient

from .factories import UserFactory


class CommonAPIClient(APIClient):
    pass


class CommonTestCase(TestCase):
    user_factory = UserFactory


class CommonAPITestCase(APITestCase):
    client_class = CommonAPIClient
    user_factory = UserFactory
