import re


def password_validator(password):
    return re.compile(
        "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"
    ).match(password)


def tire_format_validator(tire_info):
    return re.compile("\d+/\d+R\d+").match(tire_info)
