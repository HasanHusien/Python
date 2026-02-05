from flask import Flask, render_template

myApp = Flask(__name__)

@myApp.route('/')
def homePage() :
  return render_template('homepage.html')

@myApp.route('/about') 
def aboutPage() :
  return render_template('about.html')


if __name__ == '__main__' :
  
  myApp.run(debug=True, port=8000)