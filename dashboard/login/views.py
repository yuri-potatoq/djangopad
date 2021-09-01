from django.shortcuts import render
from django.views.generic import View

import logging


LOG = logging.getLogger(__file__)


class LoginForm(View):
    def get(self, request, *args, **kwargs):
        LOG.info("form validate")
        return render(request, 'login.html')