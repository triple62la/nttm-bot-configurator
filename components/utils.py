import datetime
import json
import os

import jwt


def get_config():
    if not os.path.exists(os.getcwd() + "\config.json"):
        return {}
    else:
        with open("config.json", "r") as f:
            data = json.loads(f.read())
            return data


def validate_config(data):
    if not data["auth_by_login"] and not data["nttm_token"]:
        return {"is_valid": False,
                "message": "Вы выбрали авторизацию в NTTM по токену, однако поле 'токен из NTTM' пустое!"}
    if not data["bot_token"]:
        return {"is_valid": False, "message": " Не заполнен токен тлг бота!"}
    if not data["nttm_url"]:
        return {"is_valid": False, "message": " Не заполнен url адрес nttm!"}
    if data["auth_by_login"] and (not data["login"] or not data["password"]):
        return {"is_valid": False, "message": "Поле логин/пароль не заполнено!"}
    return {"is_valid": True, "message": ""}


def validate_token(token):
    jwt_options = {
        'verify_signature': False,
        'verify_exp': True,
        'verify_nbf': False,
        'verify_iat': False,
        'verify_aud': False
    }
    try:
        decoded = jwt.decode(token, algorithms=["HS512"], options=jwt_options)
        exp_timedelta = datetime.datetime.fromtimestamp(decoded["exp"]) - datetime.datetime.utcnow()
        return {"is_valid": True, "message": f"NTTM токен истекает через {exp_timedelta}",
                "exp_timedelta": exp_timedelta}
    except jwt.exceptions.ExpiredSignatureError:
        return {"is_valid": False, "message": "Срок действия введенного вами токена истек", "exp_timedelta": None}
    except Exception as e:
        return {"is_valid": False, "message": f"Произошла ошибка при проверке токена: {e}", "exp_timedelta": None}


def format_token(token: str):
    if token.startswith("Bearer "):
        token = token[6:]
    return token.strip()


SAVED_CONFIG = get_config()
