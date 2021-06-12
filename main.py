from flask import Flask, request, render_template, session, redirect, Response, url_for, send_file

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/data')
def data_page():
    return render_template('data.html')

@app.route('/problems')
def problems_page():
    return render_template('problems.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host = '127.0.0.1', debug = True)