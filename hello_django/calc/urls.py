from django.urls import path

from hello_django.calc import views


urlpatterns = [
    path('', views.Calc.as_view()),
    path('<int:A>/<int:B>', views.index, name='calc')
]