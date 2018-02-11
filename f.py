from flask import Flask,jsonify,request



app = Flask(__name__)
database = ["atlantic croacker", "atlantic salmon", "bigeye tuna", "hound needlefish", "pollock", "red groupe", "sailfish"]
@app.before_first_request
def activate_job():
    pass


@app.route('/', methods = ['POST'])
def hello_world():
    print(request.json)
    dicts = {}
    dicts['name'] = 'sailfish'
    dicts['s_name'] = 'sailfish'
    

    return json.dumps(dicts)


if __name__ == '__main__':
    app.run()
