from flask import render_template, request, redirect, session, url_for, flash
from server.models.developer import Developer
from server.models.organization import Organization
from server.models.skill import Skill
from server.models.position import Position

# Dashboard
def root():
    if 'developer_id' not in session:
        return render_template("home.html")
    elif 'organization_id' not in session:
        return render_template("home.html")
    return redirect(url_for('dashboard'))

def dashboard():

    if 'developer_id' in session or 'organization_id' in session:
        if 'developer_id' in session:
            developers = Developer.query.get(session['developer_id'])
            skills = Skill.get_all_skills()
            positions = Position.get_all_positions()
            return render_template(
                'dashboard.html',
                deverlopers = developers,
                skills = skills,
                positions = positions,
            )
        
        if 'organization_id' in session:
            organization = Organization.query.get(session['organization_id'])
            positions = Position.get_all_positions()
            skills = Skill.get_all_skills()
            return render_template(
                'dashboard.html',
                organizations = organization,
                positions = positions,
                skills = skills,
            )
    else: 
        return redirect(url_for('home'))
    

def logout():
    session.clear()
    return redirect(url_for('home'))

def dev_dashboard():
    return render_template("dev_dashboard.html")

def org_dashboard():
    return render_template("org_dashboard.html")