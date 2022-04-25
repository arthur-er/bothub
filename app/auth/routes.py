from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app import db
from app.models import User
from app.auth import bp
from app.auth.forms import LoginForm, RegisterForm, RequestPasswordResetForm, PasswordResetForm

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuario ou senha invalidos!')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.rememberme.data)
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Login', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Parabens, agora voce e um usuario registrado')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Registro', form=form)

@bp.route('/recover', methods=['GET', 'POST'])
def recover():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RequestPasswordResetForm()
    if form.validate_on_submit():
        # TODO
        # Adicionar sistema
        # de envio de email
        # para recuperacao de
        # senha e/ou usuario
        pass
    return render_template('login.html', title='Recuperar senha', form=form)

@bp.route('/reset/<token>', methods=['GET', 'POST'])
def reset(token):
    if not token:
        flash('Token invalido!')
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        # TODO
        # Adicionar sistema
        # de troca de senha
        pass
    return render_template('reset.html', title='Redefinir senha', form=form)