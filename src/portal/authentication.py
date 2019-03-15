from flask import session
from functools import wraps
from flask import redirect, url_for


def auth_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        usr_session = AuthSession()
        if not usr_session.is_authorized():
            return redirect(url_for('account.index'))

        return f(*args, **kwargs)

    return decorated_function


class AuthSession:

    session_key = 'curr_auth'

    def destruct(self):
        session[self.session_key] = None

    def construct(self, id_ref: int):
        session[self.session_key] = AuthSessionEntry(id_ref)

    def is_authorized(self) -> bool:
        return session.get(self.session_key, None) is not None


class AuthSessionEntry:

    def __init__(self, id_user: int):
        self.id_user = id_user
        self.id_route = -1
