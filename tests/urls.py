# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.urls import include, path


urlpatterns = [
    path("", include("plans_paypal.urls")),
    path("plans", include("plans.urls")),
]
