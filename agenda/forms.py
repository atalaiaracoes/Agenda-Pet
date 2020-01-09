from django import forms


class CadastroTutor(forms.Form):
    
    tutor = forms.CharField(label="Nome do Tutor", max_length="200")
    tel_principal = forms.CharField(label="Telefone Principal", max_length="20")
    tel_alternativo = forms.CharField(label="Telefone Alternativo", max_length="20")
    email = forms.CharField(label="E-mail", max_length="80")
    cont_alternativo = forms.CharField(label="Contato Alternativo", max_length="200", required=False)
    tel_contato = forms.CharField(label="Telefone do Contato", max_length="20", required=False)
    observacao = forms.CharField(label="Observação", widget=forms.Textarea, required=False)


class CadastroPet(forms.Form):

    pet = forms.CharField(label="Nome do Pet", max_length="200")
    tipo = forms.CharField(label="Tipo do Pet", max_length="20")
    raca = forms.CharField(label="Raça do Pet", max_length="20")
    tamanho = forms.CharField(label="Tamanho do Pet", max_length="20")
    cor = forms.CharField(label="Cor do Pet", max_length="20")
    dt_nascimento = forms.DateField(label="Data de Nascimento", required=False)
    id_tutor = forms.CharField(label="Nome do Tutor", max_length="200")
    pet_alergico = forms.BooleanField(required=False)
    pet_cardiaco = forms.BooleanField(required=False)
    observacao = forms.CharField(label="Observação", widget=forms.Textarea, required=False)


class CadastroRaca(forms.Form):

    raca = forms.CharField(label="Nome da Raça", max_length="100")
    porte = forms.CharField(label="Porte da Raça", max_length="20")