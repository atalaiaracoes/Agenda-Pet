from django import forms


class CadastroServico(forms.Form):

	codigo = forms.IntegerField(label="Código do Serviço", required=False)
	servico = forms.CharField(label="Descrição do Serviço", max_length="200")
	tipo = forms.CharField(label="Tipo do Pet", max_length="10")
	tamanho = forms.CharField(label="Tamanho do Pet", max_length="10")
	valor = forms.DecimalField(label="Valor do Serviço", max_digits=10, decimal_places=2)
	ativo = forms.BooleanField(label="ativo", required=False)
	observacao = forms.CharField(label="Observação", widget=forms.Textarea, required=False)
