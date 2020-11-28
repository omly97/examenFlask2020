from flask import render_template
from flask_login import login_required

from . import home


@home.route('/home')
@login_required
def welcome():
    return render_template('home/welcome.html', title="Welcome")