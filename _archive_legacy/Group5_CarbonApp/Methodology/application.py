from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
  return render_template('home.html', title='Home')

@application.route('/methodology')
def methodology():
  return render_template('methodology.html', title='Methodology')

@application.route('/carbon_app')
def carbon_app():
  return render_template('carbon_app.html', title='Carbon App')

@application.route('/register')
def register():
  return render_template('register.html', title='Register')

if __name__=='__main__':
  application.run(debug=True)  