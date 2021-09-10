from workerpool.interface import MetaWorkerPool
from worq import get_broker, TaskSpace
from worq.pool.process import WorkerPool

ts = TaskSpace(__name__)



def start_init(url: str):
    broker = get_broker(url)
    broker.expose(ts)
    return broker


@ts.task
def process(path:str):
    import pdb; pdb.set_trace()
    print(f"receive url {path}")



class WorqPool(MetaWorkerPool):
    def init(self, url):
        import pdb; pdb.set_trace()
        self.broker = start_init(url)
        self.pool = WorkerPool(self.broker, start_init, workers=1)
    
    def start_pooling(self):
        self.pool.start()