# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
# Import date class from datetime module
from datetime import date, datetime
# from flask_restful import Resource, Api

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def my_backend_world():
    return 'Welcome to my API testing for 2 get request params that produces a json result'


@app.route('/api')
# ‘/’ URL is bound with hello_world() function.
def two_params():
    # Returns the current local date
    today = date.today()
    utc_time = datetime.now()
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    result = {
            "slack_name": slack_name,
            "current_day": today.strftime("%A, %dth of %B %Y"),
            # "utc_time": "2023-08-21T15:04:05Z",
            # "utc_time": utc_time,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": "https://github.com/mikeolams/hngx-stage1/blob/main/app.py",
            "github_repo_url": "https://github.com/mikeolams/hngx-stage1",
            "status_code": 200
            }
    return  result

    # return 	{ "current_day": today   }

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)

