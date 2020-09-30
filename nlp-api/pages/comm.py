import tornado.web


class RequestHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.nlp = self.application.nlp

    def get(self):
        self.post()
