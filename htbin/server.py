import tornado.httpserver
import tornado.ioloop

from jbnlp import Jbnlp
from route import Application


def start(port=80):
    app = Application(nlp=Jbnlp())
    tornado.httpserver.HTTPServer(app).listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    start()
