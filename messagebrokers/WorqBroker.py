from typing import Dict
from messagebrokers.interface import MetaBroker
from worq import get_queue

class WorqBroker(MetaBroker):
    def __init__(self, url):
        self.q = get_queue(url)

    def add_task(self, data:Dict ):
        import pdb; pdb.set_trace()
        self.q.tasks.process(data["path"])
        