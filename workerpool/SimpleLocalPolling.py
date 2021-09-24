import os
import time
from workerpool.interface import MetaWorkerPool


class SimpleLocalPolling(MetaWorkerPool):
    def __init__(self, local_folder_path, callback_function):
        self.local_folder_path = local_folder_path
        self.callback_function = callback_function

    def start_pooling(self):
        while True:
            files = os.listdir(self.local_folder_path)
            if len(files) < 3:
                time.sleep(0.5)
            else:
                for file_path in files:
                    if file_path.endswith(".mp4"):
                        self.callback_function(self.local_folder_path + file_path)
                        time.sleep(0.5)

