import os
from services.SigninService import SignInService
from services.RequestSignedUrlService import RequestSignUrlService
from services.FileUploadService import FileUploadService
from services.FileDeleteService import FileDeleteService


class FileUploadController:
    file_delete_service: FileDeleteService
    file_upload_service: FileUploadService
    request_signed_url_service:RequestSignUrlService
    signin_service:SignInService

    def __init__(self,file_delete_service: FileDeleteService,file_upload_service: FileUploadService,request_signed_url_service:RequestSignUrlService,signin_service:SignInService):
        self.file_delete_service=file_delete_service
        self.file_upload_service=file_upload_service
        self.request_signed_url_service=request_signed_url_service
        self.signin_service=signin_service

    def handle_file_upload(self, file_path):
        try:
            user_token = self.signin_service.retrieveUserToken()
            signed_url_data = self.request_signed_url_service.retrieve_signed_url(bearer_token=f"Bearer {user_token}",  fileName= os.path.basename(file_path))
            self.file_upload_service.upload(file_path=file_path, signed_url_data=signed_url_data)
            self.file_delete_service.deleteFile(file_path=file_path)
        except Exception as exp:
            print(f"an error occurred {exp}")