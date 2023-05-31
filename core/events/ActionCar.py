from core.base import Event, IncomingMessage
from core import Pythogram


cars = [
    dict(car="skoda", href="https://kolesa-uploads.ru/-/389e92c8-1607-44fb-94ba-fc427db8ce7b/skoda-octavia-front2-mini.jpg"),
    dict(car="lada", href="https://mn365.ru/wp-content/uploads/2021/05/1610525534_6d0723730c6f820e5ab9570b6c6f4749.jpg"),
    dict(car="volvo", href="https://n-russia.ru/wp-content/uploads/1/2/8/1286f51c56b71215d14d34a1836b7c85.jpeg"),
    dict(car="porche", href="https://sportishka.com/uploads/posts/2022-04/1651067808_30-sportishka-com-p-porshe-mashini-krasivo-foto-32.jpg"),
    dict(car="renault", href="https://static.tildacdn.com/tild3531-3463-4461-a464-613431356539/_2.jpg"),
    dict(car="mitsubishi", href="https://627400.ru/wp-content/uploads/f/7/7/f7780de395d504806a405851ad0b06ea.jpeg"),
    dict(car="opel", href="https://mobimg.b-cdn.net/v3/fetch/df/df0c41df4be36d68e7c6ea9915b0f071.jpeg"),
]


class ActionCar(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ["skoda", "volvo", "lada", "porche", "renault", "mitsubishi", "opel"]

    def action(self, message: IncomingMessage, *args, **kwargs):
        text = message.text
        for car in cars:
            if text == car.get("car"):
                self.__sender.photo.send(
                    file=car.get("href"),
                    chat=message.chat
                )


