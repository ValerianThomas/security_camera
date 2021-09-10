from workerpool.RabbitMqPool import RabbitMqPool
from services.PoolService import PoolService
from configs import configs

worker_pool = RabbitMqPool(configs.get("worker_host"), configs.get("worker_name"))
pool_service = PoolService(worker_pool)
pool_service.start_pooling()