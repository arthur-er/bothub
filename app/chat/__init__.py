from flask import Blueprint

bp = Blueprint('chat', __name__, template_folder='templates')

from app.chat import routes