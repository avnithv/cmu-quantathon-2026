import random

def strat(an):
    return an == -2 or an == 1

def run_one(N):
    A = -2
    profit = 0
    for _ in range(N):
        bet = strat(A)
        flip = random.choice([-1, 1])

        A += flip
        if A == -3: A = 2
        if A == 3: A = -2
        
        if bet:
            profit += A + random.choice([-1, 1])

    return profit

def run_many(N, runs):
    tot_sum = 0
    for _ in range(runs):
       tot_sum += run_one(N)
    return tot_sum / runs

N, runs = map(int, input().split())
print(run_many(N, runs))

