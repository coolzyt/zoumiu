#coding=utf8
__author__ = 'zhaoyuntao'
import tornado.ioloop
import tornado.web
import os
from utils import dates
from utils import images

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class OCRHandler(tornado.web.RequestHandler):
    def post(self):
        upload_path=os.path.join(os.path.dirname(__file__),'temp')  #文件的暂存路径
        file_metas=self.request.files['file']    #提取表单中‘name’为‘file’的文件元数据
        meta = file_metas[0];
        filepath=os.path.join(upload_path,str(dates.current_timestampms()))
        with open(filepath,'wb') as up:      #有些文件需要已二进制的形式存储，实际中可以更改
            up.write(meta['body'])
        self.write(images.ocr(filepath))

class MyIPHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(self.request.remote_ip);

class CarnumHandler(tornado.web.RequestHandler):
    def post(self):
        upload_path=os.path.join(os.path.dirname(__file__),'temp')  #文件的暂存路径
        file_metas=self.request.files['file']    #提取表单中‘name’为‘file’的文件元数据
        meta = file_metas[0];
        filepath=os.path.join(upload_path,str(dates.current_timestampms()))
        with open(filepath,'wb') as up:      #有些文件需要已二进制的形式存储，实际中可以更改
            up.write(meta['body'])
        filename = images.carnum_detect(filepath);
        self.redirect("./files/"+filename);

def make_app():
    current_path = os.path.dirname(__file__)
    return tornado.web.Application([
        (r"/myip", MyIPHandler),
        (r"/ocr", OCRHandler),
        (r"/carnum", CarnumHandler),
        (r'^/(.*?)$', tornado.web.StaticFileHandler,
        {"path": os.path.join(current_path, "static"), "default_filename": "index.html"}),
    ])