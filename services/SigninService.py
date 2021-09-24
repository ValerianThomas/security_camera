class SignInService:
    def  __init__(self, email, password, requests, login_url):
        self.email = email
        self.password=password
        self.requests=requests
        self.login_url=login_url


    def retrieveUserToken(self):
        response = self.requests.post(self.login_url, json={"email":self.email, "password":self.password })
        if response.status_code == 200:
            return response.json().get("token")
        else:
            raise Exception("Camera couldn't not Identified itself")

