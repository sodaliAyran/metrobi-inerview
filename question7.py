def get_max_value(capacity, carrot_types):
    carrot_weights = list(carrot_types.keys())
    carrot_prices = list(carrot_types.values())

    K = (capacity + 1) * [0]

    for i in range(capacity + 1):
        for j in range(len(carrot_types)):
            if carrot_weights[j] <= i:
                K[i] = max(K[i], K[i-carrot_weights[j]] + carrot_prices[j])

    return K[capacity]



bag1 = {5: 100, 7: 150, 3: 70}
capacity1 = 36
print(get_max_value(capacity1, bag1))

bag2 = {10: 40, 20: 100, 30: 120}
capacity2 = 50
print(get_max_value(capacity2, bag2))

bag3 = {10: 500, 20: 100, 30: 120}
capacity3 = 50
print(get_max_value(capacity3, bag3))
