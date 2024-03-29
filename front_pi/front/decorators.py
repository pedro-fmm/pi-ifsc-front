def is_authenticated(func):
    import requests
    from front_pi.settings import API_URL
    from django.shortcuts import redirect

    def wrapper(arg, *args, **kwargs):
        if arg.session.get('Authorization', False):
            resp = requests.get(API_URL + '/api/auth/is-authenticated/', headers={'Authorization': arg.session['Authorization']})
            if resp.status_code == 200:
                return func(arg, *args, **kwargs)
            return redirect('front:login')
        return redirect('front:login')
    return wrapper