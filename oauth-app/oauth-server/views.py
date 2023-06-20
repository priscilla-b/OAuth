import urllib.parse
import base64
import secrets
from hashlib import sha256

from flask import redirect, session, request
from flask_restx import Namespace, Resource, fields

from werkzeug.security import generate_password_hash, check_password_hash

from .models import User


oauth_namespace = Namespace(
    'oauth',
    description='a namespace for oauth server logic')

login_model = oauth_namespace.model(
        'Login', 
        {
            'email':fields.String(required=True, description='user email address'),
            'password': fields.String(required=True, description='user input of password')
        }

)



def generate_and_save_state():
    state = base64.urlsafe_b64encode(
        secrets.token_bytes(64)).replace('=', '')
    session['oauth_state'] = state
    return state

def generate_and_save_code_challenge():
    code_verifier = base64.urlsafe_b64encode(
        secrets.token_bytes(64)).replace('=', '')
    session['code_verifier'] = code_verifier
    return base64.urlsafe_b64encode(sha256(code_verifier)).replace('=', '')

def generate_and_save_nonce():
    nonce = base64.urlsafe_b64encode(
        secrets.token_bytes(64)).replace('=', '')
    session['oauth_nonce'] = nonce
    return nonce


@oauth_namespace.route("/login")
@oauth_namespace.expect(login_model)
class OAuthRedirectToLogin(Resource):
    def get(self):
        """
        Redirect to login service
        """
        client_id = '9b893c2a-4689-41f8-91e0-aecad306ecb6'
        redirect_uri = urllib.parse.quote('http://localhost:5000/login')
        scopes = urllib.parse.quote('profile offline_access openid')
        state = generate_and_save_state()
        code_challenge = generate_and_save_code_challenge()
        nonce = generate_and_save_nonce()

        return redirect(
            'http://localhost:8080/oauth/authorize?' +
            f'client_id={client_id}' +
            f'redirect_uri={redirect_uri}' +
            f'state={state}' +
            f'response_type=code' +
            f'scope={scopes}' +
            f'code_challenge={code_challenge}' +
            f'code_challenge_method=S256' +
            f'nonce={nonce}'
        )


@oauth_namespace.route("/authorize")
@oauth_namespace.expect(login_model)
class OAuthAuthorize(Resource):
    def post(self):
        """
        OAuth Login service
        """
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = User.query.filter_by(email=email).first()

        if user is None:
            response = {"message": f"User with email {email} could not be found"}
            return response, 400
        
        if not check_password_hash(user.password, password):
            response =  {"message": "Password incorrect"}
            http_status = 400
        # else:
        #     access_token = create_access_token(identity=user.id)
        #     refresh_token = create_refresh_token(identity=user.id)

        #     response = {
        #         'access_token': access_token,
        #         'refresh_token': refresh_token
        #     }
        http_status = 200

        return response, http_status




