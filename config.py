import sqlite3

TOKEN = '5023426840:AAGoQqPYmsHuDhlR7PxCncAOKtUDUgwxkj8'

STARTMSG = "Добрый день это переводчик языков коренных народов РФ, для смены языка наберите /choose"
KEYMSG = "Choose input or output - Выберите языки перевода"
OUTMSG = "Choose output language"
INMSG = "Choose input language"
mydb = sqlite3.connect("base.sqlite")
