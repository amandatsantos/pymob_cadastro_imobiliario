
from flask import render_template,session, request,url_for, flash, redirect

from imob import app, db,  bcrypt

from .forms import LoginForm, RegistrationForm
from .models import User



@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'FAvor fazer login ' , 'danger')
        return redirect(url_for('login'))
    return render_template('admin/index.html', title='pagina admin')



@app.route('/registrar', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, username=form.username.data,
                   email=form.email.data,                 
                   password=hash_password)
                   
        db.session.add(user)
        db.session.commit()
        flash(f'Obrigado {form.name.data} por resgistrar' , 'success')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html',title='Registrar Usuario' ,form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user= User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,  form.password.data):
            session['email'] = form.email.data 
            flash(f'ola {form.email.data} voce esta logado' , 'success')      
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash(f'Não foi possivel logar no sistema','danger')

    return render_template ('admin/login.html', form=form, title='pagina login')
    
