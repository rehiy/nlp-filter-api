import tornado.web


class Application(tornado.web.Application):

    def __init__(self, nlp):
        self.nlp = nlp
        super(Application, self).__init__([
            (r"/", HomeHandler),
            (r"/tags", TagsHandler),
            (r"/pseg", PsegHandler),
            (r"/deny", DenyHandler)
        ])


class RequestHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.nlp = self.application.nlp

    def get(self):
        self.post()


class HomeHandler(RequestHandler):

    def get(self):
        self.write("nlp api server")


class TagsHandler(RequestHandler):

    def post(self):
        content = self.get_argument('content')
        result = self.nlp.text_rank(content)
        self.write({"result": result})


class PsegHandler(RequestHandler):

    def post(self):
        content = self.get_argument('content')
        result = self.nlp.pseg_cut(content)
        self.write({"result": result})


class DenyHandler(RequestHandler):

    def post(self):
        content = self.get_argument('content')
        result = self.nlp.pseg_cut(content, ["deny"])
        self.write({"result": result})
