
Quick Start::

    pipenv install
    pipenv shell
    python app.py

    pipenv shell
    python client.py


操作步骤

1. 启动 app.py: `python app.py`
2. 访问 http://127.0.0.1:5000 ，输入用户名
3. 访问 http://127.0.0.1:5000/client ，获取 client_id 和 client_secret
4. 新建 .env 并设置 CLIENT_ID 和 CLIENT_SECRET 变量
5. 启动 client.py: `python client.py`
6. 访问 http://127.0.0.1:8000 ，选择yes
7. 自动跳转页面后获取到 oauth_token
8. 访问 http://127.0.0.1:8000 即可获取资源服务器的帐号名
