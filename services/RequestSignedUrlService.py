class RequestSignUrlService:
    def  __init__(self, requests, sign_api_url):
        self.requests=requests
        self.sign_api_url=sign_api_url


    def retrieve_signed_url(self, bearer_token, fileName):
        headers = {
            "Authorization":bearer_token
        }
        response = self.requests.post(self.sign_api_url, json={"fileName":fileName}, headers=headers)
        if response.status_code == 200:
            return response.json().get("data")
        else:
            raise Exception("Camera couldn't not get signed url")

        

