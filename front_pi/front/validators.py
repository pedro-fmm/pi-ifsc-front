import re

def validaEmail(email):
    regra_email = re.compile(r'^[\w-]+@[\w-]+\.[\w-]')
    if regra_email.match(email):
        return True
    return False



