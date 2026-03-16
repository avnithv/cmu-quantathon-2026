import random

probs = [0] * 5
def strat(delta_s, first):
    global probs
    if first:
        probs[-2] = 1
    elif delta_s <= -2:
        probs = [0] * 5
        probs[delta_s+1] = 1
    elif delta_s >= 2:
        probs = [0] * 5
        probs[delta_s-1] = 1
    else:
        new_probs = [0] * 5

        for i in range(-2, 2):
            new_probs[i+1] += 0.5 * probs[i]
        new_probs[-2] += 0.5 * probs[2]

        for i in range(2, -2, -1):
            new_probs[i-1] += 0.5 * probs[i]
        new_probs[2] += 0.5 * probs[-2]


        p_obs = (new_probs[delta_s-1] + new_probs[delta_s+1])

        if p_obs == 0:
            print(probs, new_probs, delta_s)

        probs = [0] * 5
        probs[delta_s-1] = new_probs[delta_s-1] / p_obs
        probs[delta_s+1] = new_probs[delta_s+1] / p_obs

    profit = [0, 1, -0.5, 0.5, -1]
    coef_q = 0
    for i in range(-2, 3):
        coef_q += probs[i] * profit[i]
    
    opt = coef_q / 2
    return max(0, opt)

def run_one(N):
    A = -2
    profit = 0
    prev_s = 0
    cur_s = 0
    for i in range(N):
        bet = strat(cur_s - prev_s, i == 0)
        flip = random.choice([-1, 1])

        A += flip
        if A == -3: A = 2
        if A == 3: A = -2

        delta_s = A + random.choice([-1, 1])
        prev_s = cur_s
        cur_s += delta_s
        
        profit += bet * delta_s - bet * bet

    return profit

def run_many(N, runs):
    tot_sum = 0
    for _ in range(runs):
        tot_sum += run_one(N)
    return tot_sum / runs

N, runs = map(int, input().split())
print(run_many(N, runs))