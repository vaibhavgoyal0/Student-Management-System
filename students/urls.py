from django.urls import path
from .views import SecondYearStudentListCreateView, ThirdFourthYearStudentListCreateView

urlpatterns = [
    path('second-year-students/', SecondYearStudentListCreateView.as_view(), name='second-year-students'),
    path('third-fourth-year-students/', ThirdFourthYearStudentListCreateView.as_view(), name='third-fourth-year-students'),
]