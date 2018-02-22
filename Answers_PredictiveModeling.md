1. (Given a Dataset) Analyze this dataset and give me a model that can predict this response variable.
	1. Because of having the response variable, we know this question is a supervised question. 
	2. Determine whether this question is classification or regression.
	3. For classification question, we can simply use decision tree classifier to tackle it.
	4. For regression question, we can use linear regression to tackle it.
5. What error metric would you use to evaluate how good a binary classfier is? What if the classes are imbalanced? What if there are more than 2 groups?
	1. The error metric for evaluating a binary classfier:
		* Precision-Recall, AUC-ROC, confusion matrix, f1-score 
	2. When the dataset is imbalanced
		* When the 2 groups are equally important, we should use ROC-AUC to evaluate it. But when we only care one rare group, we should use Precision-Recall to evalute it.
	3. References:
		* [Kaggle Discussion](https://www.kaggle.com/general/7517)
		* [Cross Validated](https://stats.stackexchange.com/questions/7207/roc-vs-precision-and-recall-curves)