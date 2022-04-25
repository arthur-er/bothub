from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import db
from app.models import User, Bot, Message
from app.main import bp
from app.main.forms import BotForm

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    bots = Bot.query.filter_by(owner_id=current_user.id)
    return render_template('index.html', bots=bots, user=current_user)

@bp.route('/makebot', methods=['POST','GET'])
@login_required
def botform():
    form = BotForm()
    if form.validate_on_submit():
        bot = Bot(name=form.name.data, owner_id=current_user.id)
        bot.setHash()
        db.session.add(bot)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('makebot.html', form=form)
