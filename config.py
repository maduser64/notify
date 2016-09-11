# config.py

from authomatic.providers import oauth2, oauth1

CONFIG = {
    
    'tw': { #  internal provider name
           
        # Provider class
        'class_': oauth1.Twitter,
        
        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': '########################',
        'consumer_secret': '########################',
    }
}
