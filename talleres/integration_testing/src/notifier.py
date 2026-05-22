import random

class Notifier:
    def send(self, message):
        if random.random() < 0.1:
            raise ConnectionError("No se pudo enviar la notificación")

        print(f"Notificación enviada: {message}")
