
from django.contrib import admin
#from .admin import custom_admin_site
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import WelcomeView
from django.views.generic.list import ListView
from .models import Receipt
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from .views import RegisterView

class ReceiptListView(ListView):
    model = Receipt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcom/', WelcomeView.as_view(), name='welcom'),
    path('login/', LoginView.as_view(success_url=reverse_lazy('welcom')), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', RedirectView.as_view(url='/login/')), 
    path('register/',RegisterView.as_view(), name='register'),
]
