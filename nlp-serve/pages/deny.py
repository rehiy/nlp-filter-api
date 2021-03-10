from .comm import RequestHandler


class DenyHandler(RequestHandler):

    def post(self):
        content = self.get_argument('content')
        result = self.nlp.pseg_cut(content, ["deny"])
        self.write({"result": result})
