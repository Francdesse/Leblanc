from playwright.sync_api import Playwright

firstOrderPayload = {"orders":[{"country":"Algeria","productOrderedId":"6960eae1c941646b7a8b3ed3"}]}

class APIUtils:
    #first login to get the token
    def get_token(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": "rahulshetty33@gmail.com", "userPassword": "Password123$$"})
        assert response.ok

        return response.json()["token"]

    #use token to create first order
    def create_first_order(self, playwright: Playwright):
        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=firstOrderPayload,
                                 headers={"Authorization": token,
                                          "Content-Type": "application/json"})
        print(response.json())