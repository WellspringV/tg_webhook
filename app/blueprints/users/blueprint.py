from flask import Blueprint
from flask import render_template, request, redirect, url_for
from app.models import db, User


users_bp = Blueprint("users", __name__, template_folder="templates")


@users_bp.route("/")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("users/list.html", users=users)


@users_bp.route("/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("users.user_detail", id=user.id))

    return render_template("users/create.html")


@users_bp.route("/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template("users/detail.html", user=user)


@users_bp.route("/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(User, id)

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("users.user_list"))

    return render_template("users/delete.html", user=user)
