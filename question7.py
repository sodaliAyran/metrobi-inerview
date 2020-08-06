def get_max_value(capacity, carrot_types):
    K = [[0 for x in range(capacity + 1)] for x in range(len(carrot_types) + 1)]
    carrot_weights = list(carrot_types.keys())
    carrot_prices = list(carrot_types.values())

    for i in range(len(carrot_types) + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif carrot_weights[i-1] <= w:
                K[i][w] = max(carrot_prices[i-1] + K[i-1][w-carrot_weights[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[len(carrot_types)][capacity]


val = [60, 100, 120]
wt = [10, 20, 30]
bag1 = {5: 100, 7: 150, 3: 70}
capacity1 = 36
print(get_max_value(capacity1, bag1))

bag2 = {10: 60, 20: 100, 30: 120}
capacity2 = 50
print(get_max_value(capacity2, bag2))
