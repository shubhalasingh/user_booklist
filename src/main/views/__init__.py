from .user import *
from main import app

userview = UserView()

app.add_route('/list', userview)