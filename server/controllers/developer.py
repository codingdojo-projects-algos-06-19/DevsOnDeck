from flask import render_template, request, redirect, session, url_for, flash
from server.models.developer import Developer
from server.models.skill import Skill


# Developer
def dev_register_page():
    return render_template('dev_register.html')

def dev_login_page():
    return render_template('dev_login.html')

def dev_create():
    errors = Developer.register_validation(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect(url_for('developer:register'))
    developer_id = Developer.create_developer(request.form)
    session['developer_id'] = developer_id
    return redirect(url_for("dashboard"))

def dev_login():
    valid, response = Developer.login_developer(request.form)
    if not valid:
        flash(response)
        return redirect(url_for("developer:login_page"))
    session['developer_id'] = response
    print('random')
    print(session['developer_id'])
    return redirect(url_for("dashboard"))

def dev_logout():
    session.clear()
    return redirect(url_for("home"))

#developer skills
def dev_add_skill():
    errors = Skill.skill_validation(request.form)
    if errors:
        for error in errors:
            flash(error)
    Skill.add_skill(request.form, session['developer_id'])
    return redirect(url_for("dashboard"))