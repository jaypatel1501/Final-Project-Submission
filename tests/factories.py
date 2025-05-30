import factory
from factory.fuzzy import FuzzyChoice, FuzzyInteger
from service.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    category = FuzzyChoice(choices=["Electronics", "Toys", "Books"])
    price = FuzzyInteger(10, 500)
    available = FuzzyChoice(choices=[True, False])
