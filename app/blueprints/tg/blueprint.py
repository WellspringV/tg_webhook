import datetime

from flask import Blueprint
from flask import render_template, request, jsonify
from app.models import db, Message


tg_bp = Blueprint("tg", __name__, template_folder="templates")


@tg_bp.route("/")
def messages_list():
    msgs = db.session.execute(db.select(Message).order_by(Message.username)).scalars()
    return render_template("tg/list.html", msgs=msgs)


@tg_bp.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        r = request.get_json()

        msg = Message(
            username=r["message"]["from"]["username"],
            user_id=r["message"]["chat"]["id"],
            text=r["message"]["text"],
            date=datetime.datetime.fromtimestamp(r["message"]["date"])
        )
        db.session.add(msg)
        db.session.commit()

        return jsonify(r)


@tg_bp.route("/<int:id>")
def msg_detail(id):
    msg = db.get_or_404(Message, id)
    return render_template("tg/detail.html", msg=msg)
