from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class BotForm(FlaskForm):
    name = StringField('Nome do bot', validators=[DataRequired()])
    submit   = SubmitField('Criar')