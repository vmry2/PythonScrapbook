import random

colors = ["Red", "Black", "Green"]
deck = list(range(1, 53))

results = random.choices(colors, weights=[18, 18, 2], k=10)

# random.shuffle(deck)
hand = random.sample(deck, k=5)
print(hand)
