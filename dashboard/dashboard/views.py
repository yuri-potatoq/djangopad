from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View

import logging


LOG = logging.getLogger(__file__)


# @login_required(login_url='login')
class EntryDash(View):
    def get(self, *args, **kwargs):
        LOG.info("form validate")
        
        return render(self.request, 'dashboard-entry.html')


class LoginForm(View):
    def get(self, request, *args, **kwargs):
        LOG.info("form validate")
        return render(request, 'login.html')


class RegisterForm(View):
    def get(self, request, *args, **kwargs):
        LOG.info("form validate")
        return render(request, 'register.html')