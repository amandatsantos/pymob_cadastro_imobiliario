from os import abort

from sqlalchemy.exc import IntegrityError
from flask import render_template,session, request,url_for, flash, redirect, session
from .forms import  *
from imob import app, db
from .models import *



@app.route('/')
def home():
    return render_template('admin/index.html', title = 'CONSULTA PYMOB')

#abrir na adm


# CATEGORIA ROTAS

@app.route('/categorias')
def categorias():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('login'))
    categorias = Categoria.query.order_by(Categoria.id.desc()).all()
    return render_template ('pymob/categoria/categoria.html', title = 'CATEGORIAS', categorias = categorias)


@app.route('/addcategoria', methods=["GET", "POST"])
def addcategoria():
    if 'email' not in session:
       flash(f'FAvor fazer login ' , 'danger')
       return redirect(url_for('/login'))
    
    if  request.method == "POST":
        getcategoria = request.form.get('categoria')
        categoria = Categoria(name=getcategoria)
        db.session.add(categoria)
        flash(f'a categoria {getcategoria} foi cadastrada com sucesso', 'success')
        db.session.commit()

        return redirect(url_for('categorias'))
   
    
    return render_template('/pymob/categoria/addcategoria.html', title='ADICIONAR CATEGORIAS' ,categorias='categorias')


@app.route('/updatecategoria/<int:id>', methods=["GET", "POST"])
def updatecategoria(id):
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('/login'))
    updatecategoria = Categoria.query.get_or_404(id)
    categoria = request.form.get('categoria')
    if request.method == "POST":
        updatecategoria.name = categoria
        flash(f'a categoria  foi atualizada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('categorias'))  
    return render_template('/pymob/categoria/updatecategoria.html', title='ATUALIZAR CATEGORIAS' ,updatecategoria='updatecategoria')    


@app.route('/remover-categoria/<int:id>', methods=[ "POST", "GET"])
def deletecategoria(id):

    categoria = Categoria.query.filter_by(id=id).first()
    print(id)
    if request.method == "POST":
            if categoria:
                db.session.delete(categoria)
                db.session.commit()
                return redirect('/categorias')
               
    return render_template('/pymob/categoria/deletecategoria.html')
            
    


# IMOVEL ROTAS

@app.route('/imoveis', methods=["GET", "POST"])
def imoveis():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('login'))
    imoveis = Imovel.query.all()
    return render_template ('pymob/imovel/imovel.html', title = 'IMOVEIS', imoveis = imoveis)


@app.route('/addimovel', methods=["GET", "POST"])
def addimovel():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('/login'))

    
    
    categorias = Categoria.query.all()
    form = ImovelForm(request.form)
    if request.method=="POST":
        immobile_title = form.immobile_title.data
        street_address = form.street_address.data
        neighborhood = form.neighborhood.data
        city =form.city.data
        state = form.state.data
        cep = form.cep.data
        price= form.price.data
        description = form.description.data
        categoria = request.form.get( 'categoria')
        
    
        addimov = Imovel( immobile_title=immobile_title,street_address=street_address, neighborhood=neighborhood, city=city, state=state,price=price ,cep=cep,  description =description,categoria_id=categoria)
        db.session.add(addimov)
        db.session.commit()
        flash(f' Produto {immobile_title} foi cadastrada com sucesso')
        return redirect(url_for('imoveis'))
    return render_template('pymob/imovel/addimovel.html',title='REGISTRAR IMOVEL' ,form=form, categorias=categorias)


@app.route('/updateimovel/<int:id>', methods=["GET", "POST"])
def updateimovel(id):
    categorias = Categoria.query.all()
    imovel = Imovel.query.get_or_404(id)
    categoria = request.form.get('categoria') 
    form = ImovelForm(request.form)
    if request.method=="POST":
        
        imovel.immobile_title = form.immobile_title.data 
        imovel.street_address = form.street_address.data 
        imovel.neighborhood =  form.neighborhood.data 
        imovel.city    = form.city.data 
        imovel.state           = form.state.data 
        imovel.cep             =  form.cep.data 
        imovel.price           = form.price.data
        imovel.description     = form.description.data
        imovel.categoria_id = categoria

        db.session.commit()
        flash(f' Imovel  foi Atualizado com sucesso')
        return redirect(url_for('addimovel'))
    form.immobile_title.data = imovel.immobile_title
    form.street_address.data = imovel.street_address
    form.neighborhood.data = imovel.neighborhood
    form.city.data = imovel.city
    form.state.data = imovel.state
    form.cep.data = imovel.cep
    form.price.data= imovel.price
    form.description.data =imovel.description
       
        
    return render_template('/pymob/imovel/updateimovel.html', title='ATUALIZAR IMOVEIS' ,form=form, categorias= categorias, imovel =imovel)    

@app.route('/remover-imovel/<int:id>', methods=[ "POST", "GET"])
def deleteimovel(id):

    imovel = Imovel.query.filter_by(id=id).first()
    print(id)
    if request.method == "POST":
            if imovel:
                db.session.delete(imovel)
                db.session.commit()
            return redirect('imoveis')
            
    return render_template('/pymob/imovel/deleteimovel.html')
            

# INQUILINO ROTAS

@app.route('/inquilinos')
def inquilinos():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('login'))
    inquilinos =Inquilino.query.order_by(Inquilino.id.desc()).all()
    return render_template ('pymob/inquilino/inquilino.html', title = 'INQUILINOS', inquilinos= inquilinos)


@app.route('/updateinquilino/<int:id>', methods=["GET", "POST"])
def updateinquilino(id):
    
    inquilino = Inquilino.query.get_or_404(id)
    form = InquilinoForm(request.form)
    if request.method=="POST":
        
        inquilino.name = form.name.data 
        inquilino.username = form.username.data 
        inquilino.cpf = form.cpf.data 
        inquilino.telefone = form.telefone.data 
        inquilino.email = form.email.data 
        
        
        db.session.commit()
        flash(f' Inquilino foi Atualizado com sucesso')
        return redirect(url_for('inquilinos'))
    form.name.data = inquilino.name
    form.username.data  = inquilino.username
    form.cpf.data = inquilino.cpf
    form.telefone.data  = inquilino.telefone
    form.email.data  = inquilino.email
    
       
        
    return render_template('/pymob/inquilino/updateinquilino.html', title='ATUALIZAR INQUILINO' ,form=form,  inquilino= inquilino)    


@app.route('/addinquilino', methods=["GET", "POST"])
def addinquilino():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('/login'))

    
    form = InquilinoForm(request.form)
    if request.method=="POST":
        name = form.name.data
        username = form.username.data
        cpf = form.cpf.data
        telefone =form.telefone.data
        email = form.email.data
        


    
        addinq = Inquilino( name =name , username = username, cpf =cpf, telefone=telefone,email=email )
        db.session.add(addinq)
        db.session.commit()
        flash(f' Produto {name} foi cadastrada com sucesso')
    return render_template('pymob/inquilino/addinquilino.html',title='REGISTRAR INQUILINO' ,form=form)


@app.route('/remover-inquilino/<int:id>', methods=[ "POST", "GET"])
def deleteinquilino(id):

    inquilino = Inquilino.query.filter_by(id=id).first()
    print(id)
    if request.method == "POST":
            if inquilino:
                db.session.delete(inquilino)
                db.session.commit()
                return redirect('/inquilinos')
            abort(404)
    return render_template('/pymob/inquilino/deleteinquilino.html')
            
# CORRETOR ROTAS

@app.route('/corretores')
def corretores():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('login'))
    corretores =Corretor.query.order_by(Corretor.id.desc()).all()
    return render_template ('pymob/corretor/corretor.html', title = 'CORRETORES', corretores=corretores)


@app.route('/addcorretor', methods=["GET", "POST"])
def addcorretor():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('/login'))

    
    
    form = CorretorForm(request.form)
    if request.method=="POST":
        name = form.name.data
        username = form.username.data
        creci = form.creci.data
        cpf = form.cpf.data
        telefone =form.telefone.data
        email = form.email.data
    
    
        addcorr = Corretor( name =name , username = username, creci=creci,cpf =cpf, telefone=telefone,email=email )
        db.session.add(addcorr)
        db.session.commit()
        flash(f' Produto {name} foi cadastrada com sucesso')
    return render_template('pymob/corretor/addcorretor.html',title='REGISTRAR CORRETOR' ,form=form)


@app.route('/updatecorretor/<int:id>', methods=["GET", "POST"])
def updatecorretor(id):
    
    corretor = Corretor.query.get_or_404(id)
    form = CorretorForm(request.form)
    if request.method=="POST":
        
        corretor.name = form.name.data 
        corretor.username = form.username.data 
        corretor.creci = form.creci.data 
        corretor.cpf = form.cpf.data 
        corretor.telefone = form.telefone.data 
        corretor.email = form.email.data 
        
        
        db.session.commit()
        flash(f' corretor foi Atualizado com sucesso')
        return redirect(url_for('corretores'))
    form.name.data = corretor.name
    form.username.data  = corretor.username
    form.creci.data = corretor.creci
    form.cpf.data = corretor.cpf
    form.telefone.data  = corretor.telefone
    form.email.data  = corretor.email
    return render_template('/pymob/inquilino/updateinquilino.html', title='ATUALIZAR CORRETOR' ,form=form,  corretor=corretor)   


@app.route('/remover-corretor/<int:id>', methods=[ "POST", "GET"])
def deletecorretor(id):

    corretor = Corretor.query.filter_by(id=id).first()
    print(id)
    if request.method == "POST":
            if corretor:
                db.session.delete(corretor)
                db.session.commit()
                return redirect('/corretores')
            abort(404)
    return render_template('/pymob/corretor/deletecorretor.html')
            

# PROPRIETARIO ROTAS

@app.route('/proprietarios')
def proprietarios():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('login'))
    proprietarios =Proprietario.query.order_by(Proprietario.id.desc()).all()
    return render_template ('pymob/proprietario/proprietario.html', title = 'PROPRIETARIOS', proprietarios=proprietarios)
    

@app.route('/addproprietario', methods=["GET", "POST"])
def addproprietario():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('/login'))

    
    imoveis = Imovel.query.all()
    form = ProprietarioForm(request.form)
    if request.method=="POST":
        name = form.name.data
        username = form.username.data
        cpf = form.cpf.data
        telefone =form.telefone.data
        email = form.email.data
        imovel= request.form.get('imovel')
        

       
    
        addprop = Proprietario( name =name , username = username, cpf =cpf, telefone=telefone,email=email,imovel_id=imovel )
        db.session.add(addprop)
        db.session.commit()
        flash(f' Proprietario {name} foi cadastrada com sucesso, {imovel}')
    return render_template('pymob/proprietario/addproprietario.html',title='REGISTRAR PROPRIETARIO' ,form=form, imoveis=imoveis)


@app.route('/updateproprietario/<int:id>', methods=["GET", "POST"])
def updateproprietario(id):
    imoveis= Imovel.query.all()
    proprietario = Proprietario.query.get_or_404(id)
    imovel = request.form.get('imovel') 
    form = ProprietarioForm(request.form)
    if request.method=="POST":
        
        proprietario.name = form.name.data 
        proprietario.username = form.username.data 
        proprietario.cpf = form.cpf.data 
        proprietario.telefone = form.telefone.data 
        proprietario.email = form.email.data 
        proprietario.imovel_id =  imovel
        
        db.session.commit()
        flash(f' Proprietario foi Atualizado com sucesso')
        return redirect(url_for('proprietarios'))
    form.name.data = proprietario.name
    form.username.data  = proprietario.username
    form.cpf.data = proprietario.cpf
    form.telefone.data  = proprietario.telefone
    form.email.data  = proprietario.email
    
       
        
    return render_template('/pymob/proprietario/updateproprietario.html', title='ATUALIZAR PROPRIETARIO' ,form=form, imoveis =imoveis, proprietario= proprietario)    

@app.route('/remover-proprietario/<int:id>', methods=[ "POST", "GET"])
def deleteproprietario(id):

    proprietario = Proprietario.query.filter_by(id=id).first()
    print(id)
    if request.method == "POST":
            if proprietario:
                db.session.delete(proprietario)
                db.session.commit()
                return redirect('/proprietarios')
            abort(404)
    return render_template('/pymob/proprietario/deleteproprietario.html')
            

# ALUGUEL ROTAS

@app.route('/addaluguel', methods=["GET", "POST"])
def addaluguel():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('/login'))

    
    imoveis = Imovel.query.all()
    proprietarios = Proprietario.query.all()
    inquilinos = Inquilino.query.all()
    corretores = Corretor.query.all()
    form = AluguelForm(request.form)
    if request.method=="POST":
        terms = form.terms.data
        price = form.price.data
        imovel= request.form.get('imovel')
        proprietario= request.form.get('proprietario')
        inquilino= request.form.get('inquilino')
        corretor= request.form.get('corretor')
        
    
        addalu = Aluguel( terms=terms,price=price, imovel_id=imovel, proprietario_id=proprietario, inquilino_id=inquilino, corretor_id=corretor, )
        db.session.add(addalu)
        db.session.commit()
        flash(f' Aluguel de {id} foi cadastrada com sucesso')
    return render_template('pymob/aluguel/addaluguel.html',title='REGISTRAR ALUGUEL' ,form=form, imoveis=imoveis, proprietarios=proprietarios, inquilinos=inquilinos, corretores=corretores)


@app.route('/alugueis')
def alugueis():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('login'))
    alugueis = Aluguel.query.order_by(Aluguel.id.desc()).all()
    return render_template ('pymob/aluguel/aluguel.html', title = 'ALUGUEIS', alugueis=alugueis)


@app.route('/updatealuguel/<int:id>', methods=["GET", "POST"])
def updatealuguel(id):
    imoveis= Imovel.query.all()
    proprietarios= Proprietario.query.all()
    inquilinos=Inquilino.query.all()
    corretores= Corretor.query.all()
    aluguel = Aluguel.query.get_or_404(id)
    imovel = request.form.get('imovel') 
    proprietario = request.form.get('proprietario') 
    inquilino = request.form.get('inquilino') 
    corretor = request.form.get('corretor') 
    form = AluguelForm(request.form)
    if request.method=="POST":
        
        aluguel.terms = form.terms.data 
        aluguel.price = form.price.data 
        aluguel.imovel_id =  imovel
        aluguel.proprietario_id = proprietario
        aluguel.inquilino_id =  inquilino
        aluguel.corretor_id =  corretor
        db.session.commit()
        flash(f' Aluguel foi Atualizado com sucesso')
        return redirect(url_for('alugueis'))
    form.terms.data = aluguel.terms
    form.price.data  = aluguel.price
    
    return render_template('pymob/aluguel/updatealuguel.html',title='ATUALIZAR ALUGUEL' ,form=form,aluguel=aluguel ,imoveis=imoveis, proprietarios=proprietarios, inquilinos=inquilinos, corretores=corretores)


@app.route('/remover-aluguel/<int:id>', methods=[ "POST", "GET"])
def deletealuguel(id):

    aluguel = Aluguel.query.filter_by(id=id).first()
    print(id)
    if request.method == "POST":
            if aluguel:
                db.session.delete(aluguel)
                db.session.commit()
                return redirect('alugueis')
            abort(404)
    return render_template('/pymob/aluguel/deletealuguel.html')
            

# CONTRATO ROTAS

@app.route('/addcontrato', methods=["GET", "POST"])
def addcontrato():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('/login'))

    
    alugueis= Aluguel.query.all()
    
    form = ContratoForm(request.form)
    if request.method=="POST":
        contract_months = form.contract_months.data
        contract_start_date = form.contract_start_date.data
        contract_terminated_date = form.contract_terminated_date.data
        aluguel= request.form.get('aluguel')
        
        
    
        addcontrt = Contrato( contract_months=contract_months,contract_start_date=contract_start_date, contract_terminated_date=contract_terminated_date, aluguel_id=aluguel )
        db.session.add(addcontrt)
        db.session.commit()
        flash(f' Contrato de {id} foi cadastrada com sucesso')
    return render_template('pymob/contrato/addcontrato.html',title='REGISTRAR CONTRATO' ,form=form, alugueis=alugueis)


@app.route('/contratos')
def contratos():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('login'))
    contratos = Contrato.query.order_by(Contrato.id.desc()).all()
    return render_template ('pymob/contrato/contrato.html', title = 'CONTRATOS', contratos = contratos)


@app.route('/updatecontrato/<int:id>', methods=["GET", "POST"])
def updatecontrato(id):


    alugueis= Aluguel.query.all()
    contrato = Contrato.query.get_or_404(id)
    aluguel = request.form.get('aluguel') 
    form = ContratoForm(request.form)
    if request.method=="POST":
        
        contrato.contract_months = form.contract_months.data 
        contrato.contract_start_date = form.contract_start_date.data 
        contrato.contract_terminated_date =  form.contract_terminated_date.data 
        contrato.aluguel_id = aluguel
        
        db.session.commit()
        flash(f' Contrato foi Atualizado com sucesso')
        return redirect(url_for('contratos'))
    form.contract_months.data  = contrato.contract_months
    form.contract_start_date.data  =contrato.contract_start_date
    form.contract_terminated_date.data  =contrato.contract_terminated_date
    
    return render_template('pymob/contrato/updatecontrato.html',title='ATUALIZAR CONTRATO' ,form=form,alugueis=alugueis, contrato=contrato)


@app.route('/remover-contrato/<int:id>', methods=[ "POST", "GET"])
def deletecontrato(id):

    contrato = Contrato.query.filter_by(id=id).first()
    print(id)
    if request.method == "POST":
            if contrato:
                db.session.delete(contrato)
                db.session.commit()
                return redirect('/contratos')
            abort(404)
    return render_template('/pymob/contrato/deletecontrato.html')
            