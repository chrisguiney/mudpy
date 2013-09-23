from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, StaticFileHandler
from tornado.websocket import WebSocketHandler

class CharacterHandler(RequestHandler):

    def get(self, *args, **kwargs):
        # @TODO get character
        pass

    def post(self, *args, **kwargs):
        # @TODO update character
        pass

    def put(self, *args, **kwargs):
        # @TODO create character
        pass

    def delete(self, *args, **kwargs):
        # @TODO delete character
        pass

class RaceHandler(RequestHandler):
    pass

class GameHandler(WebSocketHandler):

    def on_open(self):
        pass

    def on_message(self, message):
        self.write_message(message)


def main():
    app = Application([
        (r'/character/', CharacterHandler),
        (r'/game/', GameHandler)
    ], static_path="/Users/chris/src/mudpy/static/", debug=True)

    app.listen(8000)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()