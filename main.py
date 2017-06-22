# coding=utf8
__author__ = 'zhaoyuntao'

import tornado.ioloop
import tornado.web
import handler


if __name__ == "__main__":
    app = handler.make_app()
    import socket
    app.listen(8080,"0.0.0.0")
    tornado.ioloop.IOLoop.current().start()
