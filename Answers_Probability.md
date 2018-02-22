# Q1
Bobo the amoeba has a 25%, 25%, and 50% chance of producing 0, 1, or 2 offspring, respectively. Each of Bobo’s descendants also have the same probabilities. What is the probability that Bobo’s lineage dies out?

## Ans

 Let's denote the probabilities of having 0, 1, or 2 offspring are $p_{0}, p_{1}, p_{2}$.

 There are three options in which Bobo's lineage could die out.
1. If there is no offspring, the probaility of lineage dying out is **$p_{0}$**
2. If there is one offspring, the probaility of lineage dying out is **$q$** which is contingent on having one offspring.
3. If there are two offspring, the probability of lineage dying out is **$q^2$** which is contigent on having two offspring

Let's assume $q = \lim_{n\to\infty} q_{n}$. Then the full probability of being extinct is

$$q = p_{0} + p_{1} q + p_{2} q^2$$

After solving this quadratic equation, we can get $p = 1\:or\:\frac{p_{0}}{p_{2}}$
## References

* [Quora Discussion](https://www.quora.com/Bobo-the-amoeba-has-a-25-25-and-50-chance-of-producing-0-1-or-2-offspring-respectively-Each-of-Bobos-descendants-also-have-the-same-probabilities-What-is-the-probability-that-Bobos-lineage-dies-out)