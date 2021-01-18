import requests
from .models import TgSettings


def sendTelegram(tg_name, tg_plan):
    setting = TgSettings.objects.get(pk=1)
    token = str(setting.tg_token)
    chat_id = str(setting.tg_chat_id)
    text = str(setting.tg_text)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    a = text.find('{')
    b = text.find('}')
    c = text.rfind('{')
    d = text.rfind('}')

    final_text = text[0:a] + tg_name + text[b+1:c] + tg_plan + text[d+1:-1]

    req = requests.post(method, data={'chat_id': chat_id,
                                      'text': final_text
                                      })


