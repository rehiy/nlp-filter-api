from .comm import RequestHandler


class PsegHandler(RequestHandler):

    def post(self):
        content = self.get_argument('content')
        result = self.nlp.pseg_cut(content)
        self.write({"result": result})
