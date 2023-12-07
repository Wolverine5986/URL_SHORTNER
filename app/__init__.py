from flask import Flask

app = Flask(__name__)


#------------------initialize user----------------------

from app.user.user import user
app.register_blueprint(user)




