
# linares_plot.py  

Linares plot consist of a sina plot plus a box that contains the mean and the 95% confidence interval done by bootstrap.  
Yo need to previously install sinaplot from https://github.com/mparker2/seaborn_sinaplot  
```
linares_plot(x='order', y='interference', hue='delay', df= df, pallete='viridis', order=[1,2], hue_order=[0.2, 7], point_size=1.5,  alpha=0.4, width=0.6 )  
```
![](https://github.com/davidbestue/funciones/blob/master/imgs/linares_plot.png)



# Dot plot function

Example with 1

```
dotplot(df=df, columns='A_err', subjects='subject', colors='k', xnames='Cond1')
```

![](https://github.com/davidbestue/funciones/blob/master/imgs/download%20(1).png)





Example with 2

```
dotplot(df=df, columns=['A_err', 'A_err_abs' ], subjects='subject', colors=['r', 'g'], xnames=['cond1', 'Cond2'],
        title='Conditions plot', xlabel='', ylabel='value')
```


![](https://raw.githubusercontent.com/davidbestue/funciones/master/imgs/download.png)


# bootstrap.py

Generates the inf and superior confidence interval of an array. 
Commented you have an example of how to run it in parallel for multiple samples.

It is bootstrap with replacement. It takes an array of the same length of the original but there is going to be repeted measures.

It is suggested to put it into the site-pakeges folder

'C:\Users\David\Anaconda3\envs\python3\Lib\site-packages\bootstrap.py'


Simple example
```
from bootstrap import *

a = np.random.rand(1000)
n = bootstrap_repl(a, ci=95, n=1000, stat=np.mean)

print(n)
(0.4736973603664837, 0.5102396146145342)
```


Serie/ paralel example (paralel is suggested!)
```
As = [np.random.rand(1000) for i in range(0,100)]

#### Serie
n=[]
for a in As:
    n.append(bootstrap_repl(a))

print(n)
[(0.4736973603664837, 0.5102396146145342), (0.49254558510255847, 0.5286548899342883), ... , (0.4704919715461403, 0.5052919240356857)]


#### Paralel
numcores = multiprocessing.cpu_count()
n = Parallel(n_jobs = numcores)(delayed(bootstrap_repl)(a) for a in As)

print(n)
[(0.4736973603664837, 0.5102396146145342), (0.49254558510255847, 0.5286548899342883), ... , (0.4704919715461403, 0.5052919240356857)]
```

# Decode function

From an activity decodes the population vector

```
decode(RE)
```

Output is an angle 0-360 degrees. Negative values are computed as positive in the opposite quadrant (q1;q3, q2:q4)


# remove_outliers.py

Remove the otliers of many columns at the same time! From the initial dataframe)
Input a list with the names of the columns (Pandas dataFrame)
Output the dataframe without outliers and a boxplot for each of the columns analyzed


```
df_b_r = remove_outlier_mult_columns( df_b_r, ['beer','rand'])
```

![](https://github.com/davidbestue/funciones/blob/master/imgs/img_outliers.png)  


# statistical_annotation.ipynb  

Example of how to add statistical annotations on a boxplot

![](https://github.com/davidbestue/funciones/blob/master/imgs/stat_anot.png)    







