import os
import flask


IMG_ALLOWED = {'png', 'jpg', 'jpeg', 'JPG'}#'JPG', 'gif'}

TEMPLATE = "" # path for template folder (ex. "/home/Username/Documents/app/app1/template")
STATIC = "" # path for static folder (ex. "/home/Username/Documents/app/app1/static")
DATA = "" # path for data folder (ex. "/home/Username/Documents/app/app1/static/data")

app = flask.Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
app.config['UPLOAD'] = os.path.join(STATIC, 'upload')
