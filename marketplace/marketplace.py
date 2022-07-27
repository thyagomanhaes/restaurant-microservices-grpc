# marketplace/marketplace.py
import os

from flask import Flask, render_template, request
import grpc

from recommendations_pb2 import FoodCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{recommendations_host}:50051"
)
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/",  methods=['GET', 'POST'])
def render_homepage():
    category = request.args.get('fname')
    print(category)

    if category is not None:
        if int(category) <= 2:
            recommendations_request = RecommendationRequest(
                user_id=1, category=int(category), max_results=3
            )
            recommendations_response = recommendations_client.Recommend(
                recommendations_request
            )
        return render_template(
            "homepage.html",
            recommendations=recommendations_response.recommendations,
        )
    
    return render_template(
        "homepage.html"
    )
