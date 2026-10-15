from playwright.sync_api import Playwright

firstOrderPayload = {"orders":[{"country":"Algeria","productOrderedId":"6960eae1c941646b7a8b3ed3"}]}

class APIUtils:
    #first login to get the token
    def get_token(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": "rahulshetty33@gmail.com", "userPassword": "Password123$$"})
        assert response.ok #verify the call was done successfully
        print("this is the response after login successfully", response.json()) #will print the whole json response
        respbody = response.json()
        print(respbody["token"]) #will print only the token
        return respbody["token"] #this allows me to call in the other class, without it; the code will fail

    #use token to create first order
    def create_first_order(self, playwright: Playwright):
        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=firstOrderPayload,
                                 headers={"Authorization": token,
                                          "Content-Type": "application/json"})
        assert response.ok
        print("this is the response after creating an order",response.json())
        order_id = response.json()['orders'][0]
        print('this is the order number',order_id)
        return order_id
