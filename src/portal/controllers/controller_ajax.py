from flask import Blueprint, request
from flask_login import login_user

from portal.ajax.ajax_response import AjaxResponse
from portal.ajax.ajax_response_code import AjaxResponseCode
from system.database import Database
from system.models.user import User
from system.util.util_input import input_format, input_match_hash, input_match, input_hash

ajax_controller = Blueprint('ajax', __name__)
db = Database.get_instance()


@ajax_controller.route('/')
def ajax_default():
    return AjaxResponse(AjaxResponseCode.invalid,
                        message='Invalid AJAX call').send()


@ajax_controller.route('/account-login/', methods=['POST'])
def ajax_login():
    form = request.form
    session = db.get_session()
    email = input_format(form.get('email'))
    password = input_format(form.get('password'))

    user = session.query(User).filter_by(email=email).first()
    response = AjaxResponseCode.failure
    message = 'Unknown username/password combination'

    if user is not None and input_match_hash(password, user.password):
        if user.is_authenticated:
            login_user(user)
            response = AjaxResponseCode.success
            message = ''
        else:
            message = 'Account has not been activated yet.'

    return AjaxResponse(response, message=message).send()


@ajax_controller.route('/account-register/', methods=['POST'])
def ajax_register():
    form = request.form
    session = db.get_session()
    email = input_format(form.get('email'))
    password = input_format(form.get('password'))
    password_confirmed = input_format(form.get('password_confirmed'))
    response = AjaxResponseCode.failure

    if not input_match(password, password_confirmed):
        message = 'Password entries do not match!'

    elif session.query(User.id).filter_by(email=email).first() is not None:
        message = 'Email already exists!'

    else:
        message = 'Account successfully created!'
        response = AjaxResponseCode.success

        user = User()
        user.email = email
        user.password = input_hash(password)

        db.commit(user)

    return AjaxResponse(response, message=message).send()
