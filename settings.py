from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0, doc="")

LANGUAGE_CODE = 'en'

SESSION_CONFIGS = [
    dict(
        name='collective_deliberation_infoTreatment', 
        num_demo_participants=3, 
        app_sequence=['collective_deliberation_infoTreatment']
        ),
    dict(
        name='No_Info_treatment',
        num_demo_participants=3,
        app_sequence=['No_info_treatment']
        ),
    ]

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1837006143083'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
