

# Simple Web app, written in Flask
# 
# It prints "Hello World" to the client's web page

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
	return "<html> <!--\
	--><head> <!--\
	--><title>Ac3 Flask App</title><!--\
	--><!--\
	--></head><!--\
	--><body><!--\
	--><h1>Hello Flaskr!</h1><!--\
	--></body><!--\
	--><!--\
	--></html>"


if __name__ == '__main__':
	app.run(debug=True)
