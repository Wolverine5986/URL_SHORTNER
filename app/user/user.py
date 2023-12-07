from flask import Blueprint,render_template,request,redirect,url_for
import pyshorteners

user = Blueprint('user',__name__,url_prefix='/')


#set route method
@user.route('/', methods= ['GET','POST'])
def index():
    return render_template('index.html')

@user.route('/url_shortner', methods=['GET','POST'])
def url_shortner():
    if request.method == 'POST':
        input_url = request.form['input_url']
        short_url = pyshorteners.Shortener().tinyurl.short(input_url)
        print(short_url)
        return render_template('index.html',url=short_url)
    else:
        return render_template('index.html')
