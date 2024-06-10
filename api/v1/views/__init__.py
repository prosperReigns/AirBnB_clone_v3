#!/usr/bin/python3
""" a script """

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.user import *
from api.v1.views.place import *
from api.v1.views.place_reviews import *
