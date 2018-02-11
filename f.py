from flask import Flask,jsonify,request



app = Flask(__name__)

@app.before_first_request
def activate_job():



@app.route('/', methods = ['POST'])
def hello_world():
    print(request.json)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
