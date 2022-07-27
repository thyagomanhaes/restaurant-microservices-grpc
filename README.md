# restaurant-microservices-grpc
Example of two microservices communication with gRPC, a client (Flask App) and a service of recommendations

# Steps
1. Create a virtual enviroment: `python -m venv venv`
2. Install the requirements for flask app microservice: `python -r marketplace/requirements.txt`
3. Install the requirements for recommendations microservice: `python -r recommendations/requirements.txt`

# create python modules from .proto file on recommendations microservice
`python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto`

# Run recommendations microservice
`cd recommendations/`
`python recommendations.py`



# create python modules from .proto file on marketplace microservice (Flask App)
`python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto`

# Run microservice Flask app
`FLASK_APP=marketplace.py flask run`
