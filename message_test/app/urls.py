# coding: utf-8

from django.urls import path
from .views import Three,FourPageOne,FourPageTwo,FourPageThree,FourPageFour,FivePage

urlpatterns = [
    path('two/<str:message_type>', Three.as_view(), name='tow'),
    path('FourPageOne/<str:message_type>', FourPageOne.as_view()),
    path('FourPageTwo', FourPageTwo.as_view(),name='fourpagetwo'),
    path('FourPageThree', FourPageThree.as_view()),
    path('FourPageFour', FourPageFour.as_view()),
    path('Five', FivePage.as_view(), name='Five')
]
