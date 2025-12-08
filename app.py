from flask import Flask
from config import Config
import os
from controllers.user_controller import UserController
from models.banco import db, Adms, Integrante

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))

app.config.from_object(Config)

# Inicializar o banco
db.init_app(app)

with app.app_context():
    db.create_all()

    # ------------------------------
    # Função para apagar e recriar os ADMs (sempre deixar comentado para não ficar recriando)
    # ------------------------------
    """ def recriar_adms():
        # Apagar todos os registros
        Adms.query.delete()
        db.session.commit()

        # Recriar ADMs com nova ordem + cargos atualizados
        novos_adms = [
            Adms(name="Raquel Maia", cargo="Líder Geral", imagem="image/raquel-admin.png"),

            Adms(name="Letycia Locha", cargo="Líder Educacional", imagem="image/leti.jpg"),
            
            Adms(name="Karol Falcão", cargo="Líder Educacional", imagem="image/karol.jpg"),

            Adms(name="Ana Beatriz", cargo="Líder de Organização", imagem="image/ana-admin.png"),

            Adms(name="Danielle Costa", cargo="Líder de Organização", imagem="image/dani.jpg"),

            Adms(name="Sabrinne Sousa", cargo="Líder de Organização", imagem="image/sabrinne-admin.jpg"),
        ]

        db.session.add_all(novos_adms)
        db.session.commit()
        print("ADMs recriados com sucesso!")

    # Chamada para recriar ADMs SEMPRE que rodar
    recriar_adms() """
    def recriar_integrantes():
        # Apagar todos os registros
        Integrante.query.delete()
        db.session.commit()
        integrantes_new = [
            Integrante(name="Karin Abe", bio="Voluntária de Criação de Conteúdo", imagem="image/karin.jpg", cargo="Social Media"),
            Integrante(name="Niedja Araújo", bio="Voluntária de Moderação", imagem="image/niedja.jpg", cargo="Moderadora"),
        ]

        db.session.add_all(integrantes_new)
        db.session.commit()
        print("Integrantes atualizadas com sucesso!")
    recriar_integrantes()


# Rotas
app.add_url_rule('/', 'home', UserController.home)
app.add_url_rule('/sobre', 'sobrenos', UserController.sobrenos)
app.add_url_rule('/contato', 'contato', UserController.contato)
app.add_url_rule('/comunidade', 'comunidade', UserController.comunidade)

if __name__ == '__main__':
    app.run(debug=True)
