#-----------------------
# 匯入flask套件
#-----------------------
from flask import Flask

#-----------------------
# 產生一個Flask網站物件
# 名稱為app
#-----------------------
app = Flask(__name__)

#-----------------------
# 定義app的路由
#-----------------------
@app.route('/')
def index():
    return 'Hello'
@app.route('/123')
def index2():
    return 'Hello123'

#-----------------------
# 啟動Flask網站
#-----------------------
if __name__ == '__main__':
    app.run(port=5000, debug=True)