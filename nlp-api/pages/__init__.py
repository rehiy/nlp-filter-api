from .tags import TagsHandler
from .pseg import PsegHandler
from .deny import DenyHandler
from .home import HomeHandler

pages = [
    (r"/", HomeHandler),
    (r"/tags", TagsHandler),
    (r"/pseg", PsegHandler),
    (r"/deny", DenyHandler)
]
