from django.http.response import HttpResponse
from django.views.generic import View, FormView

from typing import Optional

import logging

logger = logging.getLogger('main')
logger.setLevel(logging.INFO)


class TestView(View):
    def get(self, *args, **kwargs):
        
        logger.info(self.request)
        return HttpResponse(f'{args}\n{kwargs}')

class TestForm(FormView):
    def echo_form(self, *args, **kwargs):
        return HttpResponse("cap is amazing")