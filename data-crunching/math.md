#Some useful math operations!

##PLEASE NOTE: This is not a stats class. We're just giving you tools, it's up to you to ensure that you apply them appropriately. 
|Function | Use | Example | Need to import |
|---------|-----|---------|----------------|
|tstat, pval = stats.ttest_ind(list1, list2) | Do a simple t-test and get a p-value | tstat, pval = stats.ttest_ind(subset1, subset2) | from scipy import stats |
|npr.permutation(object) | Randomly permute the data object | npr.permutation(subset2) | from numpy import random as npr |
|object.mean() | Get mean of object | subset2.mean() | import numpy |
|object1.cov(object2) | Estimate coefficient of covariance between two objects | subset1.cov(subset2) | import pandas |
|object1.corr(oject2, method='spearman') | Perform a Kendall, Spearman or Pearson correlation test | subset1.corr(subset2) | import pandas |
|rolling_mean(data frame, window).plot(style='k') | Get and plot a rolling mean in your data frame with window size x. Plot it | rolling_mean(df, 1).plot(style='k') | import pandas
|


