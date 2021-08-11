from django.conf import settings
from cryptography.fernet import Fernet

fernet = Fernet(settings.MAIL_CONF_SECRET)

def encrypt_string(string):
    return fernet.encrypt(password.encode())

def decrypt_string(string):
    return fernet.decrypt(string).decode()