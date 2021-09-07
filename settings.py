from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0, doc="")

LANGUAGE_CODE = 'en'

SESSION_CONFIGS = [
    dict(
        name='Public_Info_Treatment', 
        num_demo_participants=3, 
        app_sequence=['collective_deliberation_infoTreatment']
        ),
    dict(
        name='No_Public_Info_Treatment', 
        num_demo_participants=3, 
        app_sequence=['No_info_treatment']
        ),    
    ]

ROOMS = [
    dict(
        name='GMULAB',
        display_name='GMU ECON LAB',
        participant_label_file='_rooms/GMU_lab.txt',
        use_secure_urls=False
    ),
]


# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ''
USE_POINTS = False

DEBUG_INFO = False
OTREE_PRODUCTION = True


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1837006143083'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
