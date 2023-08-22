from utils import *
from flask import Flask, Response, request
from config import ServerPort

app = Flask(__name__)


# 回应NasTool的验证
@app.route('/<int:qq>/cgi-bin/gettoken')
async def gettoken(qq):
    return {"errcode": 0, "access_token": " ", "expires_in": 7200}


# 接收NasTool推过来的消息
@app.route('/<int:qq>/cgi-bin/message/send', methods=['POST'])
async def send(qq):
    data = request.json
    print(data)
    data['qq'] = qq
    await send_ws_msg(await convent_msg(data))
    return Response(status=200)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=ServerPort)
