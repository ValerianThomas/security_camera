import os

class FileUploadService:
    def  __init__(self, requests):
        self.requests=requests


    def upload(self,file_path, signed_url_data):
        file = {
            "file": open(file_path, 'rb')
        }
        upload_url = signed_url_data.get("url")
        fields = signed_url_data.get("fields")
        data = {
            "key":fields.get("key"),
            "X-Amz-Algorithm": fields.get("X-Amz-Algorithm"),
            "X-Amz-Credential": fields.get("X-Amz-Credential"),
            "X-Amz-Date": fields.get("X-Amz-Date"),
            "Policy": fields.get("Policy"),
            "X-Amz-Signature": fields.get("X-Amz-Signature"),
        }
        response = self.requests.post(upload_url, files=file, data=data)

        if response.status_code != 204:
            raise Exception("Camera couldn't upload file")