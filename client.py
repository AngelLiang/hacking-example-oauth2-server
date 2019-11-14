import os
from flask import Flask, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
from flask_oauthlib.client import OAuthException

from dotenv import load_dotenv
dotenv_path = '.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)


CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


app = Flask(__name__)
app.debug = True
app.secret_key = 'secret'
oauth = OAuth(app)

remote = oauth.remote_app(
    'remote',
    consumer_key=CLIENT_ID,
    consumer_secret=CLIENT_SECRET,
    request_token_params={'scope': 'email'},
    base_url='http://127.0.0.1:5000/api/',
    request_token_url=None,
    access_token_url='http://127.0.0.1:5000/oauth/token',
    authorize_url='http://127.0.0.1:5000/oauth/authorize'
)


@app.route('/')
def index():
    if 'remote_oauth' in session:
        # 调用资源服务器的 api
        # base_url + 'me'
        resp = remote.get('me')  
        if resp.status >= 200 and resp.status <= 299:
            return jsonify(resp.data)
        return resp.data
    next_url = request.args.get('next') or request.referrer or None
    # 返回资源服务器的认证页面
    return remote.authorize(
        callback=url_for('authorized', next=next_url, _external=True)
    )


@app.route('/authorized')
def authorized():
    resp = remote.authorized_response()
    print(resp)
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    elif isinstance(resp, OAuthException):
        return 'message=%s data=%s' % resp.message, resp.data
    # 把 access_token 放进 session
    session['remote_oauth'] = (resp['access_token'], '')
    return jsonify(oauth_token=resp['access_token'])


@remote.tokengetter
def get_oauth_token():
    return session.get('remote_oauth')


if __name__ == '__main__':
    import os
    os.environ['DEBUG'] = 'true'
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
    app.run(host='localhost', port=8000)
