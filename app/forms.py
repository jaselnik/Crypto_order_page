from wtforms import Form, StringField, validators, PasswordField


class ClientForm(Form):
    apiKey = StringField('apiKey', [validators.Length(min=4, max=100)])
    secret = StringField('secret', [validators.Length(min=6, max=100)])


class UserLoginForm(Form):
    username = StringField('username', [validators.data_required(), validators.Length(min=4, max=25)])
    password = PasswordField('password', [validators.data_required(), validators.Length(min=6, max=200)])
