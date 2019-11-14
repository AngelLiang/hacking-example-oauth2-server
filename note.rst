
Quick Start::

    pipenv install
    pipenv shell
    python app.py

    pipenv shell
    python client.py


操作步骤

1. 访问 http://127.0.0.1:5000 ，输入用户名
2. 访问 http://127.0.0.1:5000/client ，获取 client_id 和 client_secret
3. 新建 .env 并设置 CLIENT_ID 和 CLIENT_SECRET 变量，重启 client.py
4. 访问 http://127.0.0.1:8000 ，选择yes
5. 自动跳转页面后获取到 oauth_token
6. 访问 http://127.0.0.1:8000 即可获取帐号名
