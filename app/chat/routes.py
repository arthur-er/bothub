from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Bot, Message
from app.chat import bp
from app.chat.bot import botController
from app.chat.forms import ChatForm

@bp.route('/chat/<string:bhash>', methods=['GET', 'POST'])
@bp.route('/<string:bhash>', methods=['GET', 'POST'])
@login_required
def chat(bhash):
    bot = Bot.query.filter_by(bhash=bhash).first()
    form = ChatForm()
    dbfile = 'databases/' + bhash + '.db'
    botInstance = botController.getBot(bhash, dbfile)

    messages = Message.query.all()
    if form.validate_on_submit():
        message = Message(content=form.content.data, user_id=current_user.id, bothash=bhash)
        bot_response = botInstance.get_response(form.content.data)
        response = Message(user_id=current_user.id,content=str(bot_response), isbot=True, bothash=bhash, replyed=1)
        if response:
            message.replyed = 1
        db.session.add(message)
        db.session.add(response)
        db.session.commit()
        return redirect(url_for('chat.chat', bhash=bhash))
    return render_template('chat.html', title=bot.name, form=form, messages=messages, user=current_user, bhash=bhash)