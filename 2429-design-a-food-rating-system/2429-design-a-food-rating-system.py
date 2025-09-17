import heapq
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_heap = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            heapq.heappush(self.cuisine_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heap[cuisine]
        while True:
            rating, food = heap[0]
            if self.food_to_rating[food] == -rating:
                return food
            heapq.heappop(heap)