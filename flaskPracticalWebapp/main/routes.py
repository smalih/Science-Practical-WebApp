from flask import Blueprint, render_template, request
from flaskPracticalWebapp.models import Practical
from flask_login import current_user
from sqlalchemy import or_

main = Blueprint("main", __name__)

@main.route('/')
def home():
    title = "Dashboard"
    # Returns an immutable dict
    # Get method the dict item with the value of "page", or defaults to page 1
    page = request.args.get("page", 1, type=int)
    # ISSUE 6
    # Learn how to mutate the 'practicals' db query datatype
    # All practicals that are the user's or default should appear, user's being displayed first.
    # Moreover, there should be an option for the user to choose whether default practicals should appear or not.
    if current_user.is_authenticated:
        practicals = Practical.query.filter_by(user_id=current_user.id).paginate(page=page, per_page=5)

    else:
        practicals = Practical.query.filter_by(default=True).paginate(page=page, per_page=5)
    return render_template("index.html", title=title, practicals=practicals)
