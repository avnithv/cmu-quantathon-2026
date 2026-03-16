import math

def compute_expected_profit_naively(N):
    lambda_1 = math.cos(2 * math.pi / 5)
    lambda_2 = math.cos(4 * math.pi / 5)
    
    def prob(n, k):
        term1 = 2 * (lambda_1**n) * math.cos(2 * math.pi * (k+2) / 5)
        term2 = 2 * (lambda_2**n) * math.cos(4 * math.pi * (k+2) / 5)
        return 0.2 * (1 + term1 + term2)
    
    total_expected_profit = 0.0
    
    for n in range(N):
        prob_neg2 = prob(n, -2)
        prob_1 = prob(n, 1)
        
        expected_profit_at_turn = (0.5 * prob_neg2) + (1.0 * prob_1)
        total_expected_profit += expected_profit_at_turn
        
    return total_expected_profit

def compute_profit(N):
    lambda_1 = (math.sqrt(5) - 1) / 4
    lambda_2 = (-math.sqrt(5) - 1) / 4
    
    term1 = 0.3 * N
    term2 = ((2 * lambda_2 + 1) / 5) * ((1 - lambda_1**N) / (1 - lambda_1))
    term3 = ((2 * lambda_1 + 1) / 5) * ((1 - lambda_2**N) / (1 - lambda_2))
    
    return term1 + term2 + term3

def compare_profits(N):
    profit_sum = compute_expected_profit_naively(N)
    profit_closed_form = compute_profit(N)
        
    # Print the comparison
    print(f"Results for N = {N}")
    print("-" * 40)
    print(f"Summation Loop: {profit_sum:.15f}")
    print(f"Closed Form:    {profit_closed_form:.15f}")
    print(f"Difference:     {abs(profit_sum - profit_closed_form):.3e}\n")
    

compare_profits(4)
compare_profits(2026)
