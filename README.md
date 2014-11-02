# django_url_decr

Django Url Decorator is a simple lib let you decorating Django view functions based on url patterns, e.g., you may add _login\_required_ decorator for all sub urls of _/users/*_ :

    from django_url_decr import url_decr
    from django.contrib.auth.decorators import login_required

    urlpatterns = patterns(''
        url_decr(r'^users/',
                 include('users.urls'),
                 decr=login_required))


Note that you can only decorate the same sub url patterns only once. 
