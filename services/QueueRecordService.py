from messagebrokers.interface import MetaBroker


class QueueRecordService:
    message_broker:MetaBroker
    def __init__(self,message_broker:MetaBroker):
        self.message_broker = message_broker
    
    def  notify_record_ready_for_upload(self, path:str):
        self.message_broker.add_task({"path":path})