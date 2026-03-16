# CMU Quantathon

Thanks to [CMU Quant Club](https://cmuquant.com/) for hosting this event. During the competition, I focused my efforts mainly on [Problem 2](Quantathon2026Problems.pdf) and wrote an [analysis](problem2_analysis.pdf) on it. The strategies, proofs, and simulation code were developed solely by myself. I only used AI to verify the formulas I derived, both mathematically and with code. 

For parts a-e, there was a clear optimal answer, which I computed, proved, and verified via simulation. Part f asked for a strategy if information on certain variables was hidden, introducing uncertainty into the system. My strategy used Bayes theorem to compute the probability the system was in a given state (which I learned afterwards is also called a Bayesian filter). Based on these probabilities, it would compute the expected profit and the optimal decision at each time step. Simulations showed that even with the hidden information, this strategy was, on average, able to generate up to 83% of the maximum possible expected profit.

Overall, this was pretty fun and I learned quite a bit. I only wish the problems were slightly more complex ~~(and not fully solvable by AI)~~.
