# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english):
    '''
    Translate English to French
    '''
    if english is None:
        return None
    response = language_translator.translate(text=english,model_id="en-fr").get_result()
    translation = response['translations'][0]['translation']
    return translation

def french_to_english(french):
    '''
    Translates French to English
    '''
    if french is None:
        return None
    response = language_translator.translate(text=french,model_id="fr-en").get_result()
    translation = response['translations'][0]['translation']
    return translation