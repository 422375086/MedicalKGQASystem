
from QA_main import QuestionAnswerSystem

from flask import Flask,request,make_response,jsonify
from flask_cors import * # 解决ajax 跨域问题请求

app = Flask(__name__)
# r'/*' 是通配符，让本服务器所有的URL 都允许跨域请求
CORS(app, resources=r'/*')

@app.route("/",methods=('GET', 'POST'))
def index():
    global handler

    if request.method == 'POST':
        print("get post request")
        question = request.form['question']
        answer = handler.question_answer_main(question)
        if answer == "非常抱歉，这个问题超出小医的能力范围！":
            valid_answer = "false"
        else:
            valid_answer = "true"

        result_text = {"statusCode": 200, "answer": answer,"valid_answer":valid_answer}

        response = make_response(jsonify(result_text)) # jsonify 返回json格式数据
        response.headers['Access-Control-Allow-Origin'] = '*'
        # response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'

        return response

    else:
        question = request.args.get('question')
        answer =  handler.question_answer_main(question)
    return answer

if __name__ == '__main__':

    handler = QuestionAnswerSystem()
    app.run(debug=True,port=5000)

