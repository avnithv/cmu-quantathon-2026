import random

def run_one(N, stop):
    A = -2
    for i in range(N):
        flip = random.choice([-1, 1])

        A += flip
        if A == -3: A = 2
        if A == 3: A = -2
        
        if i == stop:
            return A + random.choice([-1, 1])

def run_many(runs):
    tot_sum = 0
    results = [0] * 7
    for _ in range(runs):
        stop = random.randint(1, 2026)
        profit = run_one(2027, stop)
        results[profit] += 1
    
    for i in range(7):
        results[i] /= runs 

    return results

print(*run_many(1000000))
