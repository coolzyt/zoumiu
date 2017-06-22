# coding=utf8
__author__ = 'zhaoyuntao'

import tornado.ioloop
import tornado.web
import handler
from settings import *

if __name__ == "__main__":
    app = handler.make_app()
    app.listen(settings["bind_port"],settings["bind_ip"])
    tornado.ioloop.IOLoop.current().start()
