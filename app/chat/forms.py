from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class ChatForm(FlaskForm):
    content = StringField('Mensagem', validators=[DataRequired()])
    submit   = SubmitField('Enviar')