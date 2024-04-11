from requests import Request
from dotenv import load_dotenv
from datetime import datetime, timedelta
import jwt
import os

load_dotenv(f"/app/core/credenciales.env")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def verify_token(request: Request):
    secret = SECRET_KEY
    try:
        token = request.headers.get("Authorization")
        token = token[7:]
        payload = jwt.decode(token, secret, algorithms=[ALGORITHM])
        username = payload.get("sub")
        exp = payload.get("exp")

        if datetime.utcnow().timestamp() > exp:
            raise jwt.ExpiredSignatureError
        
        return {'status': 'ok'}
    
    except jwt.ExpiredSignatureError:
        return {'status': 'expired'}
    except jwt.DecodeError:
        return {'status': 'decode_err'}
    except jwt.PyJWTError:
        return {'status': 'pywterror'}
    except:
        return {'status': 'err'}
    