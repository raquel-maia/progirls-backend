from models.banco import Adms
from flask import render_template

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
