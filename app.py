from flask import Flask
from strawberry.flask.views import GraphQLView
from database import engine
from models import Base
from schema import schema

app = Flask(__name__)

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql_view',
        schema=schema
    )
)

if __name__ == '__main__':
    app.run(debug=True)
