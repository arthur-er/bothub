from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    rememberme = BooleanField('Manter conectado?')
    submit   = SubmitField('Entrar')

class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('password')])
    submit   = SubmitField('Entrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Este nome de usuario nao esta disponivel!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Este email ja foi utilizado!')

class RequestPasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit   = SubmitField('Solicitar mudanca de senha')

class PasswordResetForm(FlaskForm):
    password = PasswordField('Nova Senha', validators=[DataRequired()])
    password2 = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    submit   = SubmitField('Mudar senha')