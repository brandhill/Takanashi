
from application import app
from handlers.account_handler import *
from handlers.document_handler import *
from handlers.settings_handler import *
from handlers.web_service_handler import *


# Home
app.add_url_rule('/', 'crash_group_home', view_func=document_view, methods=['GET'])

# Login
app.add_url_rule('/login', 'login', view_func=login_page, methods=['GET'])

# Settings
app.add_url_rule('/settings', 'settings_apps_home', view_func=redirect_to_application, methods=['GET'])
app.add_url_rule('/settings/profile', 'settings_profile', view_func=profile, methods=['GET'])
app.add_url_rule('/settings/profile', 'settings_profile_put', view_func=profile_update, methods=['PUT'])

# Applications
app.add_url_rule('/settings/applications', 'settings_apps', view_func=applications, methods=['GET'])
app.add_url_rule('/settings/applications', 'settings_apps_post', view_func=application_add, methods=['POST'])
app.add_url_rule('/settings/applications/<application_id>', 'settings_apps_put', view_func=application_update, methods=['PUT'])
app.add_url_rule('/settings/applications/<application_id>', 'settings_apps_delete', view_func=application_delete, methods=['DELETE'])
app.add_url_rule('/settings/applications/<application_id>/invite', 'settings_apps_invite', view_func=application_invite, methods=['POST'])
app.add_url_rule('/settings/applications/<application_id>/members/<member_id>', 'settings_apps_member_delete', view_func=application_member_delete, methods=['DELETE'])

# Users
app.add_url_rule('/settings/users', 'settings_users', view_func=users, methods=['GET'])
app.add_url_rule('/settings/users', 'settings_users_post', view_func=user_add, methods=['POST'])
app.add_url_rule('/settings/users/<user_id>', 'settings_users_delete', view_func=user_delete, methods=['DELETE'])

# Document
app.add_url_rule('/crash_groups/<application_id>/<group_tag>', 'crash_list', view_func=document_view, methods=['GET'])
app.add_url_rule('/crash_groups/<application_id>', 'crash_group', view_func=document_view, methods=['GET'])
app.add_url_rule('/crash_groups', 'crash_group_default', view_func=document_view, methods=['GET'])
app.add_url_rule('/exception_groups/<application_id>/<group_tag>', 'exception_list', view_func=document_view, methods=['GET'])
app.add_url_rule('/exception_groups/<application_id>', 'exception_group', view_func=document_view, methods=['GET'])
app.add_url_rule('/exception_groups', 'exception_group_default', view_func=document_view, methods=['GET'])
app.add_url_rule('/log_groups/<application_id>/<group_tag>', 'log_list', view_func=document_view, methods=['GET'])
app.add_url_rule('/log_groups/<application_id>', 'log_group', view_func=document_view, methods=['GET'])
app.add_url_rule('/log_groups', 'log_group_default', view_func=document_view, methods=['GET'])

# API
app.add_url_rule('/api/v1/exception/<key>', 'api_exception', view_func=exception_document_add, methods=['POST'])
app.add_url_rule('/api/v1/exception/<key>', 'api_exception_jsonp', view_func=exception_document_add_jsonp, methods=['GET'])
app.add_url_rule('/api/v1/log/<key>', 'api_log', view_func=log_document_add, methods=['POST'])
app.add_url_rule('/api/v1/log/<key>', 'api_log_jsonp', view_func=log_document_add_jsonp, methods=['GET'])
app.add_url_rule('/api/v1/crash/<key>', 'api_crash', view_func=crash_document_add, methods=['POST'])
