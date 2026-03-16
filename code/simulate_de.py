import random

def strat(an):
    if an == -2: 
        return 0.25
    if an == 1:
        return 0.5
    return 0

def run_one(N):
    A = -2
    profit = 0
    for _ in range(N):
        q = strat(A)
        flip = random.choice([-1, 1])

        A += flip
        if A == -3: A = 2
        if A == 3: A = -2
        
        profit += q * (A) - q * q
        # profit += q * (A + random.choice([-1, 1])) - q * q

    return profit

def run_many(N, runs):
    tot_sum = 0
    for _ in range(runs):
       tot_sum += run_one(N)
    return tot_sum / runs

N, runs = map(int, input().split())
print(run_many(N, runs))

