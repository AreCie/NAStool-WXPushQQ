import json
import websockets
from config import WsClientHost, WsClientPort


# 转换消息格式
async def convent_msg(msg):
    """
    转换消息格式
    :param msg: NasTool推过来的消息
    :return: 推向QQBot的消息
    """
    print('开始转换...')
    ret_msg = {'pic': '', 'msg': '', 'qq': msg['qq']}
    if msg['msgtype'] == 'text':
        ret_msg['msg'] = msg['text']['content']
    elif msg['msgtype'] == 'news':
        article = msg['news']['articles'][0]
        ret_msg['pic'], ret_msg['msg'] = article['picurl'], f"{article['title']}\n----------\n{article['description']}"
    else:
        ret_msg['msg'] = msg
    print(ret_msg)
    return json.dumps(ret_msg)


# 连接WS推送消息
async def send_ws_msg(msg):
    """
    连接WS推送消息
    :param msg: 推向QQBot的消息
    """
    print('开始连接ws...')
    async with websockets.connect(f"ws://{WsClientHost}:{WsClientPort}") as websocket:
        print('连接成功，开始推送...')
        await websocket.send(msg)
        print(await websocket.recv())
