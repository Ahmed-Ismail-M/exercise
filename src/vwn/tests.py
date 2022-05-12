import json
from django.test import TestCase

class IndexTest(TestCase):
    def test_post(self):
            data = {"hours":1}
            json_data = json.dumps(data)
            response = self.client.post("/",data=json_data,  content_type='application/json')
    #         print(response.content)
    # def test_get(self):
    #         response = self.client.get("/")
    #         print(response.content)
