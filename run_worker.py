from workerpool.SimpleLocalPolling import SimpleLocalPolling
import requests
from workerpool.RabbitMqPool import RabbitMqPool
from services.PoolService import PoolService
from configs import configs
from services.SigninService import SignInService
from services.RequestSignedUrlService import RequestSignUrlService
from services.FileUploadService import FileUploadService
from services.FileDeleteService import FileDeleteService
from controllers.FileUploadController import FileUploadController
from configs import configs


file_delete_service = FileDeleteService()
file_upload_service = FileUploadService(requests)
request_signed_url_service = RequestSignUrlService(requests=requests, sign_api_url=configs["signin_api_url"])
signin_service = SignInService(email=configs["email"], password=configs["password"], requests=requests, login_url=configs["login_api_url"])
file_upload_controller = FileUploadController(file_delete_service=file_delete_service, file_upload_service=file_upload_service, request_signed_url_service=request_signed_url_service,signin_service=signin_service)


worker_pool = SimpleLocalPolling(configs.get["records_path"], file_upload_controller.handle_file_upload)
pool_service = PoolService(worker_pool)
pool_service.start_pooling()