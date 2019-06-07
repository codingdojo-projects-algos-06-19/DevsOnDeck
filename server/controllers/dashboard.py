from flask import render_template, request, redirect, session, url_for, flash
from server.models.developer import Developer
from server.models.organization import Organization

# Dashboard
def root():
    if 'developer_id' not in session:
        return render_template("home.html")
    return redirect(url_for('dashboard'))

def dashboard():
    return render_template(
        'dashboard.html',
    )

def logout():
    session.clear()
    return redirect(url_for('home'))

def dev_dashboard():
    return render_template("dev_dashboard.html")

def org_dashboard():
    return render_template("org_dashboard.html")