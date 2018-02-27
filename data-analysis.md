# Q1

# Q2

What is $$R^2$$ ? What are some other metrics that could be better than $$R^2$$ and why?

## Ans

To start, let's recap$$R^2$$ . It's a statistical measure of how close the data are to the fitted model. It's also known as the coefficient of determination.

The definition of$$R^2$$ is


$$
R^2 = \frac{\text{Explained variation}}{\text{Total variation}} = 1 - \frac{\text{Residual variation}}{\text{Total variation}} = 1 - \frac{SS_{res}}{SS_{total}}
$$



$$
\begin{alignedat}{3}
SS_{total} = \text{Total variation} = \displaystyle\sum_{i}(y_{i}-\overline{y})^2 \\
SS_{exp} = \text{Explained variation} = \displaystyle\sum_{i}(f_{i}-\overline{y})^2 \\
SS_{res} = \text{Residual variation} = \displaystyle\sum_{i}(y_{i}-f_{i})^2 \\
\end{alignedat}
$$


$$R^2$$ should be between 0 and 1.

* When $$R^2$$ is 0, it represents that the model explains none of the variability of the response data around its mean
* When $$R^2$$ is 1, it represents that the model explains all of the variability of the response data around its mean

## Reference

* [Blog by Jim Frost](http://blog.minitab.com/blog/adventures-in-statistics-2/regression-analysis-how-do-i-interpret-r-squared-and-assess-the-goodness-of-fit)



