from .comm import RequestHandler


class TagsHandler(RequestHandler):

    def post(self):
        content = self.get_argument('content')
        result = self.nlp.text_rank(content)
        self.write({"result": result})
