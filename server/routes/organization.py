from config import app
from server.controllers import organization

# organization
app.add_url_rule('/organization/register', view_func=organization.org_register_page, endpoint="organization:register")
app.add_url_rule('/organization/login_page', view_func=organization.org_login_page, endpoint="organization:login_page")
app.add_url_rule('/organization/create', view_func=organization.org_create, endpoint="organization:create", methods=['POST'])
app.add_url_rule('/organization/login', view_func=organization.org_login, endpoint="organization:login", methods=['POST'])
app.add_url_rule('/organization/logout', view_func=organization.org_logout, endpoint="organization:logout")


#position
app.add_url_rule('/organization/post/position', view_func=organization.org_add_position, endpoint="organization:add_position", methods=['POST'])