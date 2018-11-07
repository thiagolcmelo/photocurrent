from functools import wraps
from flask import redirect, request, url_for, session, abort

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def author_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_author', False):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function