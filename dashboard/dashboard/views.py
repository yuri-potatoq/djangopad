from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

import logging


LOG = logging.getLogger(__file__)


class EntryDash(View):
    def get(self, request, *args, **kwargs):
        LOG.info("form validate")
        return render(request, 'dashboard-entry.html', context={
             # 'static_domain': '54.94.51.143:80',
            'static_domain': 'localhost:80',
        })