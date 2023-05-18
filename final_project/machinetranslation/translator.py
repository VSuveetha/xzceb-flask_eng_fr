```py
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
```

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def englishToFrench(englishText):
    '''
    Translate English to French
    '''
    translation = language_translator.translate(
    text=english,
    model_id='en-fr').get_result()
    french_translation = translation['translations'][0]['translation']
    return french_translation

def frenchToEnglish(frenchText):
    '''
    Translates French to English
    '''
    translation = language_translator.translate(
    text=french,
    model_id='fr-en').get_result()
    english_translation = translation['translations'][0]['translation']
    return english_translation