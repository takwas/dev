# Flask practice application


############################################################################################################
# Do imports

from flask import Flask, request, make_response, redirect


# enable command-line interaction (cmd arg parsing) using extension
from flask.ext.script import Manager

############################################################################################################
# app instance
app = Flask(__name__)

# run prog with this instead to enable cmd arg parsing
app_mang = Manager(app)

############################################################################################################
# general attribs...

# generate an HTML page using the template
# and passing in the given string
def gen_html(content=";) :) ;-D"):

	# basic HTML template
	base_html = "<html> <!--\
		--><head> <!--\
		--><title>Ac3 Flask App</title><!--\
		--><!--\
		--></head><!--\
		--><body><!--\
		--><div id='content'><!--BEGIN--> <!--END--></div><!--\
		--></body><!--\
		--><!--\
		--></html>"

	# partition base html for insertion
	part = base_html.rpartition("<!--BEGIN--> <!--END-->")
	
	# return newly formed string of html doc
	return "".join((part[0], content, part[2]))


############################################################################################################
# View functions...

# to default page
@app.route('/')
def index():
	# |go to home page;		|response-status-code:200 is not necessary; it is the default
	return make_response(gen_html("<h1>Hello Flaskr!</h1> <br/> <h4>This is the Home Page.</h4>"), 200)


# a custom user-page
@app.route('/user/<name>')
def profile(name='Anonymous'):
	response = make_response(gen_html('<h2>Hello,</h2> <br/></h3>Welcome back {0}!</h3>'.format(str(name).title())))
	return response


# a redirect view function
@app.route('/page_2')
def page_2():
	# A redirect takes a redirect URL and response-status-code:302
	return redirect('redir', 302)


# a redirect-page
@app.route('/redir')
def redir():
	response = make_response(gen_html('<h2>oOh-0oh!!!</h2> <br/></h3>You have been redirected.</h3>'), 200)
	return response


# an abort view function
@app.route('/user/<username>')
def error(username):
	user = load_user(username)		### need to confirm where to get load_user function
	if not user:
		# abort takes error-code:404
		abort(404)
	# else
	return profile(user)



# run the program
if __name__=='__main__':
	app_mang.run()