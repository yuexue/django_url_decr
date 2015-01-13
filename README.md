# django_url_decr

Django Url Decorator is a simple lib for decorating Django every view functions ofan included url sub patterns, e.g., you may add _login\_required_ decorator for all sub urls of _/users/*_ :

    from django_url_decr import url_decr
    from django.contrib.auth.decorators import login_required

    urlpatterns = patterns(''
        url_decr(r'^users/',
                 include('users.urls'),
                 decr=login_required))


The usage of _url\_decr_ is the same as _django.conf.urls.url_, despite you may pass a _decr_ parameter as the decorator.

Note that you can only decorate the same sub url patterns only once.
