from flask import Blueprint

practicals = Blueprint("practicals", __name__)

@practicals.route('/gcse/biology')
def gcse_biology():
    title = "GCSE Biology"
    return render_template("/biology/biology-gcse.html", title=title)


@practicals.route('/alevel/biology')
def alevel_biology():
    title = "A Level Biology"
    return render_template("/biology/biology-alevel.html", title=title)


@practicals.route('/gcse/chemistry')
def gcse_chemistry():
    title = "GCSE Chemistry"
    return render_template("/chemistry/chemistry-gcse.html", title=title)


@practicals.route('/alevel/chemistry')
def alevel_chemistry():
    title = "A Level Chemistry"
    return render_template("/chemistry/chemistry-alevel.html", title=title)


@practicals.route('/gcse/physics')
def gcse_physics():
    title = "GCSE Physics"
    return render_template("/physics/physics-gcse.html", title=title)


@practicals.route('/alevel/physics')
def alevel_physics():
    title = "A Level Physics"
    return render_template("/physics/physics-alevel.html", title=title)

@practicals.route('/practical/new', methods=["GET", "POST"])
@login_required
def new_practical():
    form = PracticalForm()
    if form.validate_on_submit():
        practical = Practical(title=form.title.data,
                              degStudy=form.degStudy.data,
                              equipment=form.equipment.data,
                              method=form.method.data,
                              user_id = current_user.id)
        db.session.add(practical)
        db.session.commit()
        flash("Your new practical has been saved!", "success")
        return redirect(url_for("home"))
    return render_template("create_practical.html", title="New Practical", form=form)


@practicals.route('/practical/<practical_title>')
def practical(practical_title):

    practical = Practical.query.filter_by(title=practical_title).first()
    return render_template("practical.html", title=practical.title, practical=practical)

@practicals.route('/practical/<practical_title>/update', methods=["GET", "POST"])
@login_required
def update_practical(practical_title):
    # Should be using get_or_404 or first_or_404 function
    # If there already exists a practical written by the user trying to acess it, tha practical will be returned.
    '''
    practical = Post.query.get_or_404(practical_title)
    if practical.autor != current_user:
        abort(403)
    '''
    if Practical.query.filter_by(title=practical_title, user_id=current_user.id).first():
        practical = Practical.query.filter_by(title=practical_title, user_id=current_user.id).first()
    else:
        practical = Practical.query.filter_by(title=practical_title).first()
    title = practical.title

    form = PracticalForm()
    if form.validate_on_submit():
        # If a default practical is returned, an insatnce of that practical wwill be created spefific to the user trying to update the practical
        if practical.default == True:
            practical = Practical(title=form.title.data,
                                  degStudy=form.degStudy.data,
                                  equipment=form.equipment.data,
                                  method=form.method.data,
                                  default=False,
                                  user_id=current_user.id)
            db.session.add(practical)
        else:
            practical.title = form.title.data
            practical.degStudy = form.degStudy.data
            practical.subject = form.subject.data
            practical.equipment = form.equipment.data
            practical.method = form.method.data
            practical.default = False
        db.session.commit()
        flash("Your practical has been updated!", "success")
        return redirect(url_for("practical", practical_title=practical.title))
    elif request.method == "GET":
        form.title.data = practical.title
        form.degStudy.data = practical.degStudy
        form.subject.data = practical.subject
        form.equipment.data = practical.equipment
        form.method.data = practical.method

    return render_template("create_practical.html", title="Update Practical", form=form)

@practicals.route('/practical/<practical_title>/delete', methods=["POST"])
@login_required
def delete_practical(practical_title):
    # Should be using get_or_404 or first_or_404 function
    if Practical.query.filter_by(title=practical_title, user_id=current_user.id).first():
        practical = Practical.query.filter_by(title=practical_title, user_id=current_user.id).first()
        message = "Your practical has been deleted!"
        category = "success"
        db.session.delete(practical)
        db.session.commit()
    else:
        message = "You are not the author of this practical."
        category = "danger"

    flash(message, category)
    return redirect(url_for("home"))
