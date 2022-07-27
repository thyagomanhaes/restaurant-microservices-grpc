from concurrent import futures
import random

import grpc

from recommendations_pb2 import (
    FoodCategory,
    FoodRecommendation,
    RecommendationResponse
)
import recommendations_pb2_grpc

foods_by_category = {
    FoodCategory.CHINESE: [
        FoodRecommendation(id=1, name="Yaksoba"),
        FoodRecommendation(id=2, name="Pastel"),
        FoodRecommendation(id=3, name="Rato"),
    ],
    FoodCategory.HAMBURGUER: [
        FoodRecommendation(
            id=4, name="The Hitchhiker's Guide to the Galaxy"
        ),
        FoodRecommendation(id=5, name="Ender's Game"),
        FoodRecommendation(id=6, name="The Dune Chronicles"),
    ],
    FoodCategory.JAPANESE: [
        FoodRecommendation(
            id=7, name="The 7 Habits of Highly Effective People"
        ),
        FoodRecommendation(
            id=8, name="How to Win Friends and Influence People"
        ),
        FoodRecommendation(id=9, name="Man's Search for Meaning"),
    ],
}

class RecommendationService(
    recommendations_pb2_grpc.RecommendationsServicer
):
    def Recommend(self, request, context):
        if request.category not in foods_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")

        books_for_category = foods_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(
            books_for_category, num_results
        )

        return RecommendationResponse(recommendations=books_to_recommend)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()