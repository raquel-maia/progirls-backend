from models.banco import Adms, Integrante,db
from flask import render_template, request

class UserController:
    @staticmethod
    def home(): 
        return render_template('home.html')

    @staticmethod
    def sobrenos():
        adms = Adms.query.all()
        return render_template('sobrenos.html', adms=adms)
    
    @staticmethod
    def contato():
        return render_template('contato.html')
    
    @staticmethod
    def comunidade():

        cargo_filtro = request.args.get('cargo')

        # cargos únicos
        cargos = db.session.query(Integrante.cargo).distinct().all()
        cargos = [c[0] for c in cargos]

        query = Integrante.query

        if cargo_filtro:
            query = query.filter_by(cargo=cargo_filtro)

        integrantes = query.all()

        return render_template(
            "comunidade.html",
            integrante=integrantes,
            cargos=cargos
        )
