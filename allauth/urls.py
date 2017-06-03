from importlib import import_module

from django.conf.urls import include, url

from allauth.account import views as account_views
from allauth.socialaccount import providers

from . import app_settings


urlpatterns = [
    url(r"^signup/$", account_views.signup, name="account_signup"),
    url(r"^login/$", account_views.login, name="account_login"),
    url(r"^logout/$", account_views.logout, name="account_logout"),
]

if app_settings.ACCOUNT_ENABLED:
    urlpatterns += [url(r'^', include('allauth.account.urls'))]

if app_settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [url(r'^social/', include('allauth.socialaccount.urls'))]

for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + '.urls')
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, 'urlpatterns', None)
    if prov_urlpatterns:
        urlpatterns += prov_urlpatterns
