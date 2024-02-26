from django.urls import path,re_path

from .views import *

app_name = 'mainApp'

urlpatterns = [
    #English
    path('', HomePageEnView.as_view(), name='homeEn'),
    path('Contact/', ContactPageEnView.as_view(), name='contactEn'),
    re_path('emailSend/', emailSend, name='emailSend'),
    re_path('verifyCode/', verifyCode, name='verifyCode'),
    path('Injections/', InjectionsPageEnView.as_view(), name='injectionsEn'),
    path('Tablets/', TabletsPageEnView.as_view(), name='tabletsEn'),

    ################

    #Turkish
    path('Anasayfa/', HomePageTrView.as_view(), name='homeTr'),
    re_path('emailSendTr/', emailSendTr, name='emailSendTr'),
    re_path('verifyCodeTr/', verifyCodeTr, name='verifyCodeTr'),


    re_path('insertCodes/', insertCodes, name='insertCodes'),

    ################


]