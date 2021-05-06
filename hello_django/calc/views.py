from django.shortcuts import render
from django.http import HttpResponse
from hello_django.views import HomePage


def index(request, **kwargs):
    A = kwargs['A']
    B = kwargs['B']
    result = A + B
    # return HttpResponse(f"{A}+{B}={result}")
    return render(request, 'calc.html', context={'a': A, 'b': B, 'result': result})


class Calc(HomePage):

    template_name = "calc.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse('calc')
