from .forms import LoginForm, RegistrationForm
from . import auth
from flask import redirect, render_template, url_for


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('auth/login.html', form=form)
