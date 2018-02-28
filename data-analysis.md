# Q1

# Q2

What is $$R^2$$ ? What are some other metrics that could be better than $$R^2$$ and why?

## Ans

To start, let's recap$$R^2$$. It's a statistical measure of how close the data are to the fitted model. It's also known as the coefficient of determination.

$$R^2$$ should be between 0 and 1.

* When $$R^2$$ is 0, it represents that the model explains none of the variability of the response data around its mean
* When $$R^2$$ is 1, it represents that the model explains all of the variability of the response data around its mean

Following are the drawbacks of $$R^2$$:

* It's only useful for linear regression because $$R^2$$ will not between 0 and 1 when the model is not linear.
* $$R^2$$ will be a biased estimate based on the sample
* $$R^2$$ does not indicate whether a regression model is adequate. You can have a low R-squared value for a good model \(which have statistical importance on the coefficient\), or a high R-squared value for a model that does not fit the data.
* $$R^2$$ can not determine whether the coefficient estimates and predictions are biased, which is why we must assess the residual plots.

The definition of$$R^2$$ is


$$
R^2 = \frac{\text{Explained variation}}{\text{Total variation}} = \frac{SS_{exp}}{SS_{total}} = \frac{SS_{total}-SS_{res}}{SS_{total}} = 1 - \frac{SS_{res}}{SS_{total}}
$$



$$
\begin{alignedat}{3}
SS_{total} = \text{Total variation} = \displaystyle\sum_{i}(y_{i}-\overline{y})^2 \\
SS_{exp} = \text{Explained variation} = \displaystyle\sum_{i}(\hat{y}_{i}-\overline{y})^2 \\
SS_{res} = \text{Residual variation} = \displaystyle\sum_{i}(y_{i}-\hat{y}
_{i})^2 \\
\end{alignedat}
$$


We should keep in mind that $$SS_{total} = SS_{exp} + SS_{res}$$ is only valid when the model is linear regression and has an intercept.

Here is the proof,


$$
\displaystyle\sum_{i}(y_{i}-\overline{y})^2 = \displaystyle\sum_{i}(\hat{y}_{i}-\overline{y})^2 + \displaystyle\sum_{i}(y_{i}-\hat{y}_{i})^2 + 2\displaystyle\sum_{i}(\hat{y}_{i}-\overline{y})(y_{i}-\hat{y}_{i})
$$


Because the model is linear regression,


$$
\begin{gathered}
\hat{y}_{i} = a + bx_{i} \\
\overline{y}_{i} = a + b\overline{x}_{i}\\
\hat{y}_{i} - \overline{y}_{i} = b(x_{i} - \overline{x}_{i}) \\
y_{i} - \hat{y}_{i} = (y_{i} - \overline{y}_{i}) - (\hat{y}_{i} - \overline{y}_{i}) = (y_{i} - \overline{y}_{i}) - b(x_{i} - \overline{x}_{i})
\end{gathered}
$$


So, we can deduct the cross-term into


$$
\begin{alignedat}{3}
2\displaystyle\sum_{i}(\hat{y}_{i}-\overline{y})(y_{i}-\hat{y}_{i}) = 2\hat{b}\displaystyle\sum_{i}(x_{i} - \overline{x}_{i})((y_{i} - \overline{y}_{i}) - \hat{b}(x_{i} - \overline{x}_{i})) \\
= 2\hat{b}(\displaystyle\sum_{i}(x_{i} - \overline{x}_{i})(y_{i} - \overline{y}_{i}) - \hat{b}(x_{i} - \overline{x}_{i})^2) \\
= 2\hat{b}(\displaystyle\sum_{i}(x_{i} - \overline{x}_{i})(y_{i} - \overline{y}_{i}) - \hat{b}\displaystyle\sum_{i}(x_{i} - \overline{x}_{i})^2)
\end{alignedat}
$$


By minimizing the sum of squared errors, we can get


$$
\hat{b} = \frac{\displaystyle\sum_{i}(x_{i}-\overline{x})(y_{i}-\overline{y})}{\displaystyle\sum_{i}(x_{i}-\overline{x})^2}
$$


Therefore,


$$
\begin{alignedat}{4}
2\displaystyle\sum_{i}(\hat{y}_{i}-\overline{y})(y_{i}-\hat{y}_{i}) \\
= 2\hat{b}(\displaystyle\sum_{i}(x_{i} - \overline{x}_{i})(y_{i} - \overline{y}_{i}) - \hat{b}\displaystyle\sum_{i}(x_{i} - \overline{x}_{i})^2) \\
= 2\hat{b}(\displaystyle\sum_{i}(x_{i} - \overline{x}_{i})(y_{i} - \overline{y}_{i}) - \displaystyle\sum_{i}(x_{i} - \overline{x}_{i})(y_{i} - \overline{y}_{i})) \\
= 0
\end{alignedat}
$$


## Reference

* [Blog by Jim Frost](http://blog.minitab.com/blog/adventures-in-statistics-2/regression-analysis-how-do-i-interpret-r-squared-and-assess-the-goodness-of-fit)
* [Proof of the equation](https://en.wikipedia.org/wiki/Explained_sum_of_squares#cite_note-Mendenhall-1)
* [Derivation of linear regression](https://en.wikipedia.org/wiki/Simple_linear_regression)
* [Derivation of least squares](https://en.wikipedia.org/wiki/Proofs_involving_ordinary_least_squares)
* [Why $$R^2$$ is problematic](http://blog.minitab.com/blog/adventures-in-statistics-2/five-reasons-why-your-r-squared-can-be-too-high)



