from django.urls import path
from .views import cadastro_pet, cadastro_tutor, lista_pet, lista_tutor, submit_tutor, submit_pet, cadastro_raca, submit_raca, lista_raca


app_name = 'agenda'


urlpatterns = [
	path('cadpet/', cadastro_pet, name='cadastro_pet'),
	path('cadpet/submit', submit_pet, name='submit_pet'),

	path('cadraca/', cadastro_raca, name='cadastro_raca'),
	path('cadraca/submit', submit_raca, name='submit_raca'),
	
	path('cadtutor/', cadastro_tutor, name='cadastro_tutor'),
	path('cadtutor/submit', submit_tutor, name='submit_tutor'),

	path('listtutor/', lista_tutor, name='lista_tutor'),
	path('listpet/', lista_pet, name='lista_pet'),
	path('listraca/', lista_raca, name='lista_raca'),
]