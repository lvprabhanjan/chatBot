import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def input():
   return render_template('input.html')

#@app.route('/', methods = ['GET'])
#def string():
 #   string = request.form['string']
  #  print("Question '" + string + "'")
   # return redirect('/')
	
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
