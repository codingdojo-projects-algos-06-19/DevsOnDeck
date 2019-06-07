from config import app
from server.controllers import dashboard

# Dashboard
app.add_url_rule('/', view_func=dashboard.root, endpoint="home")
app.add_url_rule('/dashboard', view_func=dashboard.dashboard, endpoint="dashboard")
app.add_url_rule('/logout', view_func=dashboard.logout, endpoint="logout")

app.add_url_rule('/developer/dashboard', view_func=dashboard.dev_dashboard, endpoint="developer:dashboard")

app.add_url_rule('/organization/dashboard', view_func=dashboard.org_dashboard, endpoint="organization:dashboard")