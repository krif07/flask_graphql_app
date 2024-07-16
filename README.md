# Instalar dependencias

pip install flask
pip install sqlalchemy
pip install strawberry-graphql
pip install uvicorn

# Construir y ejecutar el contenedor Docker

docker build -t flask_graphql_app .
docker run -p 5000:5000 flask_graphql_app

# pruebas en postman

GET
http://127.0.0.1:5000/graphql
query {
  cartItems {
    id
    name
    price
    quantity
    createdAt
    updatedAt
  }
}

POST - Listar Items del Carrito
http://127.0.0.1:5000/graphql
query {
  cartItems {
    id
    name
    price
    quantity
    createdAt
    updatedAt
  }
}

POST - Crear un Item en el Carrito
mutation {
  createCartItem(name: "Item 1", price: 9.99, quantity: 2) {
    id
    name
    price
    quantity
    createdAt
    updatedAt
  }
}

POST - Actualizar un Item del Carrito
mutation {
  updateCartItem(id: 1, name: "Updated Item", price: 19.99, quantity: 3) {
    id
    name
    price
    quantity
    createdAt
    updatedAt
  }
}

POST - Eliminar un Item del Carrito
mutation {
  deleteCartItem(id: 1)
}
