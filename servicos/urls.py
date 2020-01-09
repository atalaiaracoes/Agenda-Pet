from django.urls import path
from .views import lista_servico, cadastro_servico, submit_servico

app_name = 'servicos'

urlpatterns = [
	path('listservico', lista_servico, name='lista_servico'),
	path('cadservico/', cadastro_servico, name='cadastro_servico'),
	path('cadservico/submit', submit_servico, name='submit_servico'),
]