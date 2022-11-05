from rest_framework.test import APITestCase
from rest_framework import status

class TestToken(APITestCase):
    
    def test_create_token(self):
        sample_body={
            'username':'test',
            'password':'test',
        }
        #verificando se rota está protegida
        response = self.client.post('/auth-token/', sample_body,'json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)