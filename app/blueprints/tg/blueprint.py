import datetime

from flask import Blueprint
from flask import render_template, request, jsonify
from app.models import db, Message


tg_bp = Blueprint("webhook", __name__, template_folder="templates")


@tg_bp.route("/", methods=["GET", "POST"])
def index():
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
