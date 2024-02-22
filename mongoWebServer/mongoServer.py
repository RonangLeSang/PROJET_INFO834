import tornado
from tornado.websocket import WebSocketHandler


class ChangesHandler(tornado.websocket.WebSocketHandler):

    connected_clients = set()

    def open(self):
        ChangesHandler.connected_clients.add(self)

    def on_close(self):
        ChangesHandler.connected_clients.remove(self)

    @classmethod
    def send_updates(cls, message):
        for connected_client in cls.connected_clients:
            connected_client.write_message(message)

    @classmethod
    def on_change(cls, change):
        message = f"{change['operationType']}: {change['fullDocument']['name']}"
        ChangesHandler.send_updates(message)

