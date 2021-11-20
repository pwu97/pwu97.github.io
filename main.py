from flask import Flask, request, render_template, session, redirect, Response, url_for, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/problems')
def problems():
#    problems = [
#        {'lc_link': 'https://leetcode.com/problems/valid-number/',
#         'sol_link': '',
#         'name': 'Valid Number',
#         'company': 'fb',
#         'number': 65,
#         'difficulty': 'Hard',
#         'topics': 'String'},
#        {'lc_link': 'https://leetcode.com/problems/valid-palindrome/',
#         'sol_link': '',
#         'name': 'Valid Palindrome',
#         'company': 'spotify',
#         'number': 125,
#         'difficulty': 'Easy',
#         'topics': 'Two Pointers, String'},
#        {'lc_link': 'https://leetcode.com/problems/happy-number/',
#         'sol_link': '',
#         'name': 'Happy Number',
#         'company': 'twitter',
#         'number': 202,
#         'difficulty': 'Easy',
#         'topics': 'Hash Table, Math, Two Pointers'},
#        {'lc_link': 'https://leetcode.com/problems/find-median-from-data-stream/',
#         'sol_link': '',
#         'name': 'Find Median from Data Stream',
#         'company': 'microsoft',
#         'number': 295,
#         'difficulty': 'Hard',
#         'topics': 'Two Pointers, Design, Sorting, Heap, Data Stream'},
#    ]
    
    return render_template('problems.html')

@app.route('/projects')
def projects():
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