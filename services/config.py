import os
import flask


IMG_ALLOWED = {'png', 'jpg', 'jpeg', 'JPG'}#'JPG', 'gif'}

TEMPLATE = "/home/ksys/Documents/app/app1/template"
STATIC = "/home/ksys/Documents/app/app1/static"
DATA = "/home/ksys/Documents/app/app1/static/data"

app = flask.Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
app.config['UPLOAD'] = os.path.join(STATIC, 'upload')
