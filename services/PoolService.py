from workerpool.interface import MetaWorkerPool


class PoolService:
    worker_pool: MetaWorkerPool
    def __init__(self, worker_pool: MetaWorkerPool):
        self.worker_pool=worker_pool

    def start_pooling(self):
        print("pool started")
        self.worker_pool.start_pooling()