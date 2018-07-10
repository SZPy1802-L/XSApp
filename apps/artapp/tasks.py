import time

from XSproject.celery import app

@app.task
def sendMail(to, msg):
    time.sleep(10)
    print('向 %s 发送: %s 成功!' % (to, msg))

    return 'ok'