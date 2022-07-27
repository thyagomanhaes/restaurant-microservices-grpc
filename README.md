# restaurant-microservices-grpc
Example of two microservices communication with gRPC, a client (Flask App) and a service of recommendations

# Para gerar os módulos python a partir do arquivo .proto
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto

# Para rodar o serviço de recomendações
cd recommendations/
python recommendations.py

# Para rodar o serviço flask
FLASK_APP=marketplace.py flask run