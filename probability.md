# Q1

Bobo the amoeba has a 25%, 25%, and 50% chance of producing 0, 1, or 2 offspring, respectively. Each of Bobo’s descendants also have the same probabilities. What is the probability that Bobo’s lineage dies out?

## Ans

Let's denote the probabilities of having 0, 1, or 2 offspring are $$p_{0}, p_{1}, and\;p_{2}$$.

There are three options in which Bobo's lineage could die out.  
1. If there is no offspring, the probability of lineage dying out is $$p_{0}$$  
2. If there is one offspring, the probability of lineage dying out is $$q$$ which is contingent on having one offspring.  
3. If there are two offspring, the probability of lineage dying out is $$q^2$$ which is contigent on having two offspring

Let's assume $$q = \lim_{n\to\infty} q_{n}$$, where $$q_{n}$$ is the probability of being extinct in n steps. Then the full probability of being extinct is


$$
q = p_{0} + p_{1} q + p_{2} q^2
$$


After solving this quadratic equation, we can get $$q = 1\:or\:\frac{p_{0}}{p_{2}}$$

For proving $$q_{n}$$ is bounded, let's start with n = 1


$$
q_{1} = p_{0} < \frac{p_{0}}{p_{2}}
$$


Let's assume, the sequence is bounded when $$n = k$$ , then we get


$$
q_{k} < \frac{p_{0}}{p_{2}}
$$


So, when $$n = k + 1$$


$$
\begin{alignedat}{0}
   q_{k+1} \\ 
   = p_{0} + p_{1}q_{k} + p_{2}q_{k}^2 \\ 
   < p_{0} + p_{1} + p_{2}q_{k}^2 \\
   = (1-p_{2}) + p_{2}q_{k}^2 \\
   < (1-p_{2}) + \frac{p_{0}^2}{p_{2}} \\
   = \frac{p_{0}^2}{p_{2}} - p_{0}^2 \\
   < \frac{p_{0}^2}{p_{2}} \\
   < \frac{p_{0}}{p_{2}}
\end{alignedat}
$$


For proving $$q_{n}$$ is a monotonic sequence, let's start with


$$
q_{n+1} - q_{n} = p_{0}-(1-p_{1})q_{n}+p_{2}q_{n}^2 = p_{2}(1-q_{n})(\frac{p_{0}}{p_{2}}-q_{n})
$$


Because $$0<p_{2}, q_{n}<1$$ and $$\lim_{n\to\infty} q_{n}=\frac{p_{0}}{p_{2}}$$ , we can get $$q_{n+1} - q_{n}>0 => q_{n+1} > q_{n}$$

## References

* [Quora Discussion](https://www.quora.com/Bobo-the-amoeba-has-a-25-25-and-50-chance-of-producing-0-1-or-2-offspring-respectively-Each-of-Bobos-descendants-also-have-the-same-probabilities-What-is-the-probability-that-Bobos-lineage-dies-out)
* [How to prove monotone and bounded sequences](https://math.stackexchange.com/questions/491709/monotone-and-bounded-sequences-proof?newreg=e0308813d2a640009fa33e7ec72a1e08)



