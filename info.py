import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7641333049:AAHRXsz0G9FqIykeqp-Se9llS4MN7ur7eDQ")
API_ID = int(os.environ.get("API_ID", "23439358"))
API_HASH = os.environ.get("API_HASH", "ef7fbd454fd8a9456bbe76ee0d14ae11")
PICS = os.environ.get("PICS", "https://i.ibb.co/q7kcZCh/1-jpg.jpg").split()
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6110266480').split()]
DB_URL = os.environ.get("DB_URL", "mongodb+srv://zainab56689:<zainab56689>@cluster0.7kwls.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "zainab56689")
RemoveBG_API = os.environ.get("RemoveBG_API", "fH5qkD9xFNeHG4aRth5e1YZB")
IBB_API = os.environ.get("IBB_API", "c658b2f364a82002e6e3dda5709eef64")
FORCE_SUB = os.environ.get("FORCE_SUB", "ziddi_shop")
PORT = os.environ.get('PORT', '8080')          
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 'ziddi_shop'))
LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""
