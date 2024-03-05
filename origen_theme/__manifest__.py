{
    'name': 'Origen Theme',
    'version': '0.1',
    'sequence': 1,
    'description': 
    """Origen module to improve interface""",
    'category': 'Theme',
    'author': 'Origen',
    'images': [],
    'depends': ['crm', 'website'],
    'data': [
        'views/assets.xml',
        'views/backend_assets.xml',
        'views/templates/common.xml',
        # 'views/footer.xml',
        'views/nav.xml',
        'views/header.xml',
        'views/layout.xml',
        'views/templates/snippets.xml',
        'views/pages/homepage.xml',
        # 'views/pages/partners.xml',
        'views/pages/about.xml',
        'views/pages/homepage.xml',
        'views/pages/contact.xml',
        'views/pages/services/fiber.xml',
        'views/pages/services/voip.xml',
        'views/pages/services/service_page_template.xml',
    ],
    'images':[
        'static/splash.png'
    ],
    'assets': {
        # 'web.layout': [
        #     ('replace', 'web/static/img/favicon.ico', 'origen_theme/static/src/img/favicon.ico'),
        # ],
        # 'website.layout': [
        #     ('replace', 'website/data/website_data.xml', 'origen_theme/views/layout.xml'),
        # ],
        'web.assets_backend': [
            # ('origen_theme/static/src/less/styles_backend.less'),
            # ('origen_theme/static/src/js/inherited_web_client.js'),
        ],
        # 'web.assets_frontend': [
        #     ('origen_theme/static/src/css/wrapwrap_replacement.css'),
        #     ('origen_theme/static/src/css/slick.css'),
        #     ('origen_theme/static/src/scss/styles.scss'),
        #     ('origen_theme/static/src/js/slick.min.js'),
        #     ('origen_theme/static/src/js/jquery.validate.min.js'),
        #     ('origen_theme/static/src/js/svginject.min.js'),
        #     ('origen_theme/static/src/js/sticky.min.js'),
        #     ('origen_theme/static/src/js/script.js'),
        # ], 
    },
        
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

