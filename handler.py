__author__ = 'zhaoyuntao'
import tornado.ioloop
import tornado.web
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class MyIPHander(tornado.web.RequestHandler):
    def get(self):
        self.write(self.request.remote_ip);

def make_app():
    current_path = os.path.dirname(__file__)
    return tornado.web.Application([
        (r"/hello", MainHandler),
        (r"/myip", MyIPHander),
        (r'^/(.*?)$', tornado.web.StaticFileHandler,
        {"path": os.path.join(current_path, "static"), "default_filename": "index.html"}),
    ])