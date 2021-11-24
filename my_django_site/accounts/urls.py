from django.urls import path, re_path
from.import views

app_name='accounts'

urlpatterns = [
    path('signup/', views.signup_view,name="signup"),
    path('login/', views.login_view,name="login"),
    #re_path(r'^(?P<slug>[\w-]+)/$',views.article_detail,name="detail"),
]