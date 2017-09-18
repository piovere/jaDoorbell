from flask import Flask, current_app, request, session
from flask.ext.login import LoginManager, login_user, logout_user, \
     login_required, current_user
from flask.ext.wtf import Form, TextField, PasswordField, Required, Email
from flask.principal import Principal, Identity, AnonymousIdentity, \
     identity_changed
from functools import wraps


app = Flask(__name__)


@app.route('/')
@requires_roles('user')
def homepage():
	return "Ringing the doorbell"


def requires_roles(*roles):
	def wrapper(f):
		@wraps(f)
		def wrapped(*args, **kwargs):
			if get_current_user_role() not in roles:
				return error_response()
			return f(*args, **kwargs)
		return wrapped
	return wrapper


if __name__ == "__main__":
	app.run()
