import tornado.httpserver
import tornado.ioloop
import tornado.web

from .jieba import JiebaApi
from .pages import pages


class App(tornado.web.Application):

    def __init__(self):
        self.nlp = JiebaApi()
        super(App, self).__init__(pages)

    def start(self, port=80):
        tornado.httpserver.HTTPServer(self).listen(port)
        tornado.ioloop.IOLoop.current().start()
