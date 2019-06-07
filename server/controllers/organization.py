from flask import render_template, request, redirect, session, url_for, flash
from server.models.organization import Organization


# Organization
def org_register_page():
    return render_template('org_register.html')

def org_login_page():
    return render_template('org_login.html')

def org_create():
    errors = Organization.register_validation(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect(url_for('organization:register'))
    organization_id = Organization.create_organization(request.form)
    session['organization_id'] = organization_id
    return redirect(url_for("dashboard"))

def org_login():
    valid, response = Organization.login_organization(request.form)
    if not valid:
        flash(response)
        return redirect(url_for("organization:login_page"))
    session['organization_id'] = response
    return redirect(url_for("dashboard"))

def org_logout():
    session.clear()
    return redirect(url_for("home"))