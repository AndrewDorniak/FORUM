from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('<int:rubric_id>/', linc_by_rubric, name='linc_by_rubric'),
    path('<int:rubric_id>/<int:question_id>/', linc_by_question, name='linc_by_question')

]