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

## References

* [Quora Discussion](https://www.quora.com/How-can-you-test-that-your-random-assignment-was-truly-random)
* [Twitter Engineering article by Robert Chang](https://blog.twitter.com/engineering/en_us/a/2015/detecting-and-avoiding-bucket-imbalance-in-ab-tests.html#)

---

# Q2

What might be the benefits of running an A/A test, where you have two buckets who are exposed to the exact same product?

## Ans

* What Is A/A testing used for?
  * It is done to check that the tool being used to run the experiment is statistically fair. In an A/A test, the tool should report no difference in conversions between the control and variation, if the test is implemented correctly.
* What might be the benefits?
  * An A/A test will test the randomizer because we would expect the metrics for users in each group to be around the same. When there is a statistical difference between the two groups, following are the possible reasons:
    * The buckets are not randomized properly
    * The hypothesis test is biased and data may violate the assumptions of the test
    * The tool has not been set up properly
  * Setting a baseline for future A/B tests
  * Deciding a minimum sample size

## References

* [Quora Discussion](https://www.quora.com/What-is-an-A-A-test)
* [Blog Post](https://vwo.com/blog/aa-test-before-ab-testing/)



