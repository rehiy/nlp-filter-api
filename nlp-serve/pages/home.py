from .comm import RequestHandler


class HomeHandler(RequestHandler):

    def get(self):
        self.write("nlp api server")
