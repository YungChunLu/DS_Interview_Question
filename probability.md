# Q1

Bobo the amoeba has a 25%, 25%, and 50% chance of producing 0, 1, or 2 offspring, respectively. Each of Bobo’s descendants also have the same probabilities. What is the probability that Bobo’s lineage dies out?

## Ans

Let's denote the probabilities of having 0, 1, or 2 offspring are $$p_{0}, p_{1}, \text{and}\;p_{2}$$.

There are three options in which Bobo's lineage could die out.  
1. If there is no offspring, the probability of lineage dying out is $$p_{0}$$  
2. If there is one offspring, the probability of lineage dying out is $$q$$ which is contingent on having one offspring.  
3. If there are two offspring, the probability of lineage dying out is $$q^2$$ which is contingent on having two offspring

The probability of being extinct is


$$
q = \begin{cases}
   \frac{p_{0}}{p_{2}} &\text{if } p_{2} > p_{0}  \\
   1 &\text{if } p_{0} \geqq p_{2}
\end{cases}
$$


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

---

# Q2

In any 15-minute interval, there is a 20% probability that you will see at least one shooting star. What is the probability that you see at least one shooting star in the period of an hour?

## Ans

* Basic probability theory

Assuming the pattern of shooting stat is independent and identical at each interval.

From the question, we can get the probability of no shooting star


$$
P(star = 0) = 1 - P(star \geq 1) = 1 - 0.2 = 0.8
$$


Then, the probability of seeing at least one shooting star in the period of an hour is


$$
P(star \geq 1) = 1 - P^4(star = 0) = 1 - (0.8)^4 = 0.5904
$$


* Poisson process

The number of shooting stars in a 15-minute interval follows a Poisson distribution with rate $$15\lambda$$.

So, the probability of no shooting star in a 15-minute interval


$$
P(star = 0) = e^{-15\lambda} = 1 - P(star \geq 1) = 1 - 0.2 = 0.8
$$


Therefore, the probability of no shooting star in a 60-minute interval


$$
P(star \geq 1) = 1 - P(star = 0) = 1 - e^{-60\lambda} = 1 - (e^{-15\lambda})^4 = 1 - (0.8)^4 = 0.5904
$$


## References

* [Quora Discussion](https://www.quora.com/In-any-15-minute-interval-there-is-a-20-probability-that-you-will-see-at-least-one-shooting-star-What-is-the-probability-that-you-see-at-least-one-shooting-star-in-the-period-of-an-hour)
* [Poisson distribution explanation](http://www.stat.wisc.edu/~wardrop/courses/301chapter4)

---

# Q3

How can you generate a random number between 1 and 7 with only a die?

## Ans

1. Roll the dice twice
2. Multiply the first roll by 6 and add the second
3. Keep doing the above two steps until the result is not 36

The reason is that we can evenly divide the 35 possible outcomes by 7. And because the die is fair, we can get equal probability between each group.

## References

* [Quora Discussion](https://www.quora.com/How-can-you-generate-a-random-number-between-1-7-with-only-a-die-1)

---

# Q4

How can you get a fair coin toss if someone hands you a coin that is weighted to come up heads more often than tails?

## Ans

1. Toss the coin twice
2. If head first and tail second, consider the result as head, or tail first and head second, consider result as tail.
3. Otherwise, keep tossing the coin twice until the result is valid

## References

* [Complete Analysis Paper](http://web.eecs.umich.edu/~qstout/abs/AnnProb84.html)

---

# Q5

You have an 50-50 mixture of two normal distributions with the same standard deviation. How far apart do the means need to be in order for this distribution to be bi- modal?

## Ans

The answer is $$|\mu1−\mu2|>2\sigma$$

Proof:

TBD

## References

* [Quora Discussion](https://www.quora.com/You-have-an-50-50-mixture-of-two-normal-distributions-with-the-same-standard-deviation-How-far-apart-do-the-means-need-to-be-in-order-for-this-distribution-to-be-bimodal-Why)



