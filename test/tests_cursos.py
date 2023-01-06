from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status 


class CursosTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Cursos teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Cursos teste 2', nivel='1'
        )
        
        def test_requisition_get_para_listar_cursos(self):
            response = self.client.get(self.list_url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)