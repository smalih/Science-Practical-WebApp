from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from flaskPracticalWebapp import db
from flaskPracticalWebapp.models import Practical
from flaskPracticalWebapp.practicals.forms import PracticalForm
from flaskPracticalWebapp.practicals.utils import getDegStudyTitle, getSubjectTitle

practicals = Blueprint("practicals", __name__)
# Need to determine the logic for routing the practicals

@practicals.route('/<degStudy>/<subject>')
def degStudy_subject(degStudy, subject):
    practicals = Practical.query.filter_by(degStudy=degStudy,subject=subject).filter(((Practical.user_id==current_user.id) | (Practical.default==True)) if current_user.is_authenticated else (Practical.default==True)).all()
    title= f"{getDegStudyTitle(degStudy)} {getSubjectTitle(subject)}"
    return render_template("degStudy_subject.html", title=title, practicals=practicals)

@practicals.route('/<degStudy>/<subject>/new-practical', methods=["GET", "POST"])
@login_required
def new_practical(degStudy, subject):
    form = PracticalForm()
    if form.validate_on_submit():
        practical = Practical(title=form.title.data,
                              degStudy=form.degStudy.data.lower(),
                              subject=form.subject.data.lower(),
                              equipment=form.equipment.data,
                              method=form.method.data,
                              user_id=current_user.id)
        db.session.add(practical)
        db.session.commit()
        flash("Your new practical has been saved!", "success")
        return redirect(url_for("main.home"))
    return render_template("create_practical.html", title="New Practical", form=form)

@practicals.route('/<degStudy>/<subject>/<practical_id>')
def practical(degStudy, subject, practical_id):
    practical = Practical.query.get_or_404(practical_id)
    if practical.author != current_user and not(practical.default):
        abort(403)
    return render_template("practical.html", title=practical.title, practical=practical)

@practicals.route('/<degStudy>/<subject>/<practical_id>/update', methods=["GET", "POST"])
@login_required
def update_practical(degStudy, subject, practical_id):
    practical = Practical.query.get_or_404(practical_id)
    if practical.author != current_user and not(practical.default):
        abort(403)
    title = practical.title
    form = PracticalForm()
     # Need to find a better way of determining that changes were actually made unlike the logic used for the profile page
     # Initial practical variable be called practical1, new practical called 'practical2'; if practical1 == practical2, flash 'no changes'
     # The question is whether db objects/instances can be compared in this manner
    if form.validate_on_submit():
        # If a default practical is returned, an instance of that practical will be created specific to the user trying to update the practical
        if practical.default == True:
            practical = Practical(title=form.title.data,
                                  degStudy=form.degStudy.data.lower(),
                                  subject=form.subject.data.lower(),
                                  equipment=form.equipment.data,
                                  method=form.method.data,
                                  default=False,
                                  user_id=current_user.id)
            db.session.add(practical)
        else:
            practical.title=form.title.data
            practical.degStudy=form.degStudy.data.lower()
            practical.subject=form.subject.data.lower()
            practical.equipment=form.equipment.data
            practical.method=form.method.data
        db.session.commit()
        flash("Your practical has been updated!", "success")
        return redirect(url_for("practicals.practical", degStudy=practical.degStudy, subject=practical.subject, practical_id=practical.id))
    elif request.method == "GET":
        form.title.data = practical.title
        form.degStudy.data = getDegStudyTitle(practical.degStudy)
        form.subject.data = getSubjectTitle(practical.subject)
        form.equipment.data = practical.equipment
        form.method.data = practical.method
    return render_template("create_practical.html", title="Update Practical", form=form)

@practicals.route('/<degStudy>/<subject>/<practical_id>/delete', methods=["POST"])
@login_required
def delete_practical(degStudy, subject, practical_id):
    practical = Practical.query.get_or_404(practical_id)
    message = "Your practical has been deleted!"
    category = "success"
    db.session.delete(practical)
    db.session.commit()
    flash(message, category)
    return redirect(url_for("main.home"))
