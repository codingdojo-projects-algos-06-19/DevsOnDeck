from config import app
from server.controllers import developer

# organization
app.add_url_rule('/developer/register', view_func=developer.dev_register_page, endpoint="developer:register")
app.add_url_rule('/developer/login_page', view_func=developer.dev_login_page, endpoint="developer:login_page")
app.add_url_rule('/developer/create', view_func=developer.dev_create, endpoint="developer:create", methods=['POST'])
app.add_url_rule('/developer/login', view_func=developer.dev_login, endpoint="developer:login", methods=['POST'])
app.add_url_rule('/developer/logout', view_func=developer.dev_logout, endpoint="developer:logout")