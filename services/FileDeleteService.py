import  os

class FileDeleteService:


    def deleteFile(self,file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print(f"The file {file_path} does not exist")
