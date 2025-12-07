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
    # Função para apagar e recriar os ADMs
    # ------------------------------
    def recriar_adms():
        # Apagar todos os registros
        Adms.query.delete()
        db.session.commit()

        # Recriar ADMs com nova ordem + cargos atualizados
        novos_adms = [
            Adms(name="Raquel Maia", cargo="Líder Geral", imagem="image/raquel-admin.png"),

            Adms(name="Letycia Locha", cargo="Líder Educacional", imagem="image/leti.jpg"),
            
            Adms(name="Karol Falcão", cargo="Líder Educacional", imagem="image/karol.jpg"),

            Adms(name="Ana Beatriz", cargo="Líder de Mídia Social", imagem="image/ana-admin.png"),

            Adms(name="Danielle Costa", cargo="Líder de Mídia Social", imagem="image/dani.jpg"),

            Adms(name="Sabrinne Sousa", cargo="Líder de Mídia Social", imagem="image/sabrinne-admin.jpg"),
        ]

        db.session.add_all(novos_adms)
        db.session.commit()
        print("ADMs recriados com sucesso!")

    # Chamada para recriar ADMs SEMPRE que rodar
    recriar_adms()

    # Criar integrantes caso ainda não existam
    if not Integrante.query.first():
        integrantes_para_adicionar = [
            Integrante(name="Karin Abe", bio="Voluntária de Moderação e Criação de Conteúdo", imagem="image/karin.jpg", cargo="Moderadora"),
            Integrante(name="Niedja Araújo", bio="Voluntária de Moderação e Criação de Conteúdo", imagem="image/niedja.jpg", cargo="Moderadora"),
            Integrante(name="Mariana Aragão", bio="Voluntária de Moderação e Criação de Conteúdo", imagem="image/mari.jpg", cargo="Moderadora"),
        ]

        db.session.add_all(integrantes_para_adicionar)
        db.session.commit()
        print("Integrantes adicionados com sucesso!")


# Rotas
app.add_url_rule('/', 'home', UserController.home)
app.add_url_rule('/sobre', 'sobrenos', UserController.sobrenos)

if __name__ == '__main__':
    app.run(debug=True)
