import falcon
app = falcon.API()
from .views import *
from .settings import *