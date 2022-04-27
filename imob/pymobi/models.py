from pickle import FALSE
from imob import db

class Categoria(db.Model):
    
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.Column(db.String(30), nullable=False,unique=False )
    Imovel = db.relationship('Imovel', backref = 'categoria',lazy=True)

    def __init__(self, name):
            self.name = name


    def __repr__(self):
        return '<Categoria %r>' % self.name

class Imovel(db.Model):
    

    id = db.Column(db.Integer, primary_key=True)
    immobile_title = db.Column(db.String(80), nullable=False)
    street_address =db.Column(db.String(120), nullable=False)
    neighborhood=db.Column(db.String(100), nullable=False)
    city= db.Column(db.String(20), nullable=False)
    state= db.Column(db.String(20), nullable=False)
    cep= db.Column(db.String(10), nullable=False)
    price= db.Column(db.Numeric(10,2), nullable=False)
    description= db.Column(db.Text, nullable=False)
    # relacionamento many to one
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"),nullable=False)
    # one to many
    proprietario = db.relationship('Proprietario', backref = 'imovel',lazy=True)

    aluguel = db.relationship('Aluguel', backref = 'imovel',lazy=True)

    def __init__ (self,immobile_title ,street_address, neighborhood, city, state,price, cep,description,categoria_id):
        self.immobile_title = immobile_title
        self.street_address= street_address
        self.neighborhood= neighborhood
        self.city=city
        self.state=state
        self.price=price
        self.cep=cep
        self.description = description
        self.categoria_id= categoria_id
    def __repr__(self):
        return f' <Imovel: {self.immobile_title}>'


class Inquilino(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    username = db.Column(db.String(40), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(11),unique=False, nullable=False)
    email = db.Column(db.String(180),unique=True, nullable=False)

    aluguel = db.relationship('Aluguel', backref = 'inquilino',lazy=True)
    
 
    def __init__(self, name, username, cpf, telefone, email):
        self.name = name
        self.username = username
        self.cpf= cpf
        self.telefone= telefone
        self.email= email
        

    def __repr__(self):
        return '<User %r>' % self.username


class Corretor(db.Model):
    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    username = db.Column(db.String(40), unique=True, nullable=False)
    creci = db.Column(db.String(6), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(11),unique=False, nullable=False)
    email = db.Column(db.String(180),unique=True, nullable=False)

    aluguel = db.relationship('Aluguel', backref = 'corretor',lazy=True)
  
 
    def __init__(self, name, username, cpf,creci , telefone, email):
        self.name = name
        self.username = username
        self.cpf= cpf
        self.creci = creci
        self.telefone= telefone
        self.email= email
        

    def __repr__(self):
        return '<User %r>' % self.username




class Proprietario(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    username = db.Column(db.String(40), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(11),unique=False, nullable=False)
    email = db.Column(db.String(180),unique=True, nullable=False)
    # many to one
    imovel_id = db.Column(db.Integer, db.ForeignKey("imovel.id"),unique=True,nullable=False)

    aluguel = db.relationship('Aluguel', backref = 'proprietario',lazy=True)
 
    def __init__(self, name, username, cpf, telefone, email, imovel_id):
        self.name = name
        self.username = username
        self.cpf= cpf
        self.telefone= telefone
        self.email= email
        self.imovel_id = imovel_id
    

    def __repr__(self):
        return '<User %r>' % self.username
    #id estrageira pra imovel relacionado
    
  


class Aluguel(db.Model):
    

    id = db.Column(db.Integer, primary_key=True)
    terms = db.Column(db.Text, nullable=False)
    price= db.Column(db.Numeric(10,2), nullable=False)
    imovel_id = db.Column(db.Integer, db.ForeignKey("imovel.id"),unique=True,nullable=False)
    proprietario_id = db.Column(db.Integer, db.ForeignKey("proprietario.id"),unique=True,nullable=False)
    inquilino_id = db.Column(db.Integer, db.ForeignKey("inquilino.id"),unique=True,nullable=False)
    corretor_id = db.Column(db.Integer, db.ForeignKey("corretor.id"),unique=True,nullable=False)

    contrato = db.relationship('Contrato', backref = 'aluguel',lazy=True)
    

    def __init__(self, terms, price,imovel_id, proprietario_id,inquilino_id,corretor_id,):
        self.terms = terms
        self.price = price
        self.imovel_id = imovel_id
        self.proprietario_id = proprietario_id
        self.inquilino_id = inquilino_id
        self.corretor_id = corretor_id

    
    
        
    def __repr__(self):
       return f' <Preço aluguel: {self.price}>'


class Contrato(db.Model):
    

    id = db.Column(db.Integer, primary_key=True)
   
    contract_months = db.Column(db.String(11),unique=False, nullable=False)
    contract_start_date = db.Column(db.String(11),unique=False, nullable=False)
    contract_terminated_date =db.Column(db.String(11),unique=False, nullable=False)
    aluguel_id = db.Column(db.Integer, db.ForeignKey("aluguel.id"),unique=True,nullable=False)
  
    

    def __init__(self,  contract_months,contract_start_date, contract_terminated_date,aluguel_id):
        
        self.contract_months = contract_months
        self.contract_start_date= contract_start_date
        self.contract_terminated_date = contract_terminated_date
        self.aluguel_id = aluguel_id

    
    
        
    def __repr__(self):
       return f' <Preço aluguel: {self.price}>'


db.create_all()