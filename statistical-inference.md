# Q1

In an A/B test, how can you check if assignment to the various buckets was truly random?

## Ans

According to my current knowledge, there is no formal methods to solve this question.

For ensuring the randomness, there are two properties we need to check

1. Whether background variables in each bucket are statistical equivalent
   1. For only two buckets, we can use $$\text{Hotelling's}\;T^{2}$$
   2. For multiple buckets, we can use MANOVA
2. Whether the sizes of the various buckets are imbalanced
   1. For checking the health size of multiple buckets at the same time, we can use [**multinomial goodness of test**](http://www.r-tutor.com/elementary-statistics/goodness-fit/multinomial-goodness-fit).
   2. For identifying which bucket is not healthy, we can use **two-sided binomial test**.



For checking

## References

* [Quora Discussion](https://www.quora.com/How-can-you-test-that-your-random-assignment-was-truly-random)
* [Twitter Engineering article by Robert Chang](https://blog.twitter.com/engineering/en_us/a/2015/detecting-and-avoiding-bucket-imbalance-in-ab-tests.html#)



