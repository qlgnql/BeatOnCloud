from flask import Blueprint, render_template
from flask_login import login_required, current_user


bp = Blueprint("main", __name__, url_prefix="/")

@bp.route("/")
def index():
    return render_template("main.html")

# from flask_login import login_required

# @bp.route("/register_emotion")
# @login_required
# def register_emotion():
#     return render_template("register_emotion.html", user_id=current_user.id)