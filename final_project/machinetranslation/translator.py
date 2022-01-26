'''Required Modules'''
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

languages = language_translator.list_languages().get_result()

def english_to_french(english_text):
    ''' Translates English to French'''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()

    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    ''' Translates French to English'''

    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()

    english_text = translation['translations'][0]['translation']

    return english_text
