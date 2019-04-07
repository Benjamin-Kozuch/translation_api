from app import app

import requests
import urllib.parse
from iso639 import languages


def key():
    return app.config['YANDEX_KEY']


def language_code_from_phrase(phrase):
    DETECT_LANGUAGE_URL = f'https://translate.yandex.net/api/v1.5/tr.json/detect?key={key()}'
    phrase = urllib.parse.quote(phrase)
    DETECT_LANGUAGE_URL += f"&text={phrase}"
    response = requests.get(url=DETECT_LANGUAGE_URL)
    language_code = ''
    if response.status_code == 200:
        language_code = response.json()['lang']
    return language_code


def translate(phrase, from_language, to_language='en'):
    TRANSLATE_PHRASE_URL = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={key()}'
    TRANSLATE_PHRASE_URL += f"&text={phrase}"
    TRANSLATE_PHRASE_URL += f"&lang={from_language}-{to_language}"
    response = requests.get(url=TRANSLATE_PHRASE_URL)
    english_translation = 'No Translation Available'
    if response.status_code == 200:
        english_translation = response.json()['text'][0]
    return english_translation


def language_name_from_code(code):
    return languages.get(alpha2=code).name
