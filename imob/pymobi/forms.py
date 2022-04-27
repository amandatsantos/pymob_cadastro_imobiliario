
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class ImovelForm(Form):
    immobile_title = StringField('Titulo para o Imovel:', [validators.Length(min=4, max=25), validators.DataRequired()])
    street_address = StringField('Logradouro:', [validators.Length(min=4, max=25), validators.DataRequired()])
    neighborhood = StringField('Bairro:', [validators.Length(min=4, max=25),validators.DataRequired()])
    city = StringField('Cidade:', [validators.Length(min=4, max=25), validators.DataRequired()])
    state = StringField('Estado:', [validators.Length(min=4, max=25),validators.DataRequired()])
    cep= StringField('CEP:', [validators.Length(min=4, max=25), validators.DataRequired()])
    price = StringField('Preço: ', [validators.Length(min=6, max=35),validators.DataRequired()])
    description = StringField('Descrição', [validators.Length(min=6, max=200), validators.DataRequired()])

class InquilinoForm(Form):
    name = StringField('Nome:', [validators.Length(min=4, max=25), validators.DataRequired()])
    username = StringField('Nome de usuario:', [validators.Length(min=4, max=25), validators.DataRequired()])
    cpf = StringField('CPF:', [validators.Length(min=14, max=14), validators.DataRequired()])
    telefone =StringField('Telefone:', [validators.Length(min=16, max=16),validators.DataRequired()])
    email = StringField('Email :', [validators.Length(min=6, max=35),validators.DataRequired()])
    
class CorretorForm(Form):
    name = StringField('Nome:', [validators.Length(min=4, max=25), validators.DataRequired()])
    username = StringField('Nome de usuario:', [validators.Length(min=4, max=25),validators.DataRequired()])
    creci  = StringField('CRECI:', [validators.Length(min=8, max=8),validators.DataRequired()])
    cpf = StringField('CPF:', [validators.Length(min=14, max=14),validators.DataRequired()])
    telefone =StringField('Telefone:', [validators.Length(min=16, max=16),validators.DataRequired()])
    email = StringField('Email :', [validators.Length(min=6, max=35),validators.DataRequired()])
    
class ProprietarioForm(Form):
    name = StringField('Nome:', [validators.Length(min=4, max=25),validators.DataRequired()])
    username = StringField('Nome de usuario:', [validators.Length(min=4, max=25),validators.DataRequired()])
    cpf = StringField('CPF:', [validators.Length(min=14, max=14),validators.DataRequired()])
    telefone =StringField('Telefone:', [validators.Length(min=16, max=16),validators.DataRequired()])
    email = StringField('Email :', [validators.Length(min=6, max=35),validators.DataRequired()])
    
class AluguelForm(Form):
    terms= StringField('Termos do aluguel:', [validators.Length(min=6, max=200),validators.DataRequired()])
    price = StringField('Valor do aluguel: ', [validators.Length(min=6, max=35),validators.DataRequired()])


class ContratoForm(Form):
    contract_months= description = StringField('Tempo de contrato:', [validators.Length(min=6, max=12),validators.DataRequired()])
    contract_start_date= description = StringField('Data de Inicio:', [validators.Length(min=6, max=200),validators.DataRequired()])
    contract_terminated_date= description = StringField('Data de encerramento:', [validators.Length(min=6, max=200),validators.DataRequired()])
    