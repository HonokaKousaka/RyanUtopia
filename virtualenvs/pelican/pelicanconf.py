AUTHOR = 'Ryan Watson'
SITENAME = 'Ryan Utopia'
# SITEURL = 'https://honokakousaka.github.io/RyanUtopia'

DEFAULT_DATE_FORMAT = '%Y-%m-%d %a'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh-cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Source', 'https://github.com/HonokaKousaka/RyanUtopia'),
         ('Issues', 'https://github.com/HonokaKousaka/RyanUtopia/issues'),
         ('Discussions', 'https://github.com/HonokaKousaka/RyanUtopia/discussions'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = './pelican-alchemy/alchemy'
SITESUBTITLE = '只属于我的一隅就是我的乌托邦。'
SITEIMAGE = '/images/profile.png'
ICONS = (('github', 'https://github.com/HonokaKousaka'),)
DESCRIPTION = 'Ryan Watson\'s personal Blog. You can understand more what Ryan is thinking.'
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}
RFG_FAVICONS = True
