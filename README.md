
# Linares plot.  
linares_plot.py    

Linares plot consist of a ***sinaplot*** plus a box that contains the mean and the 95% confidence interval done by bootstrap.  
Yo need to previously install sinaplot from https://github.com/mparker2/seaborn_sinaplot  

You can plot all the trials or subject by subject in the sinaplot.
You can decide the range of CI (also define the range 95 if comparing to 0 and 69 if compearing two lines).  
The CI is always calculated by bootstrap. If you decide to plot subject by subject, the CI is calculated accordingly.  
This is decided with the argument: ***by_subj=True***
(You shuffle radomly when plotting all data (when False) or you shuffle keeping the subjects structure when plotting the subjects mean (when True).  

The legend is also implemented in a fancy way: no box and the text in color. The legend juts appears when there is "hue".  

The box can be filled or not


Examples of hue linares plot of (trials & subject)


### Plot Box:  
All the data, no hue
```
linares_plot(x='Response', y='EventBaseline', order=['Correct', 'Wrong'], df=df, palette=[c_correct, c_wrong], 
            alpha=0.2, point_size=7, reps=50)
```

![](https://github.com/davidbestue/funciones/blob/master/imgs/box_standard.png)


### Plot Box by subject:  
By subject, no hue, no fill the box

```
linares_plot(x='Response', y='EventBaseline', order=['Correct', 'Wrong'], df=df, palette=[c_correct, c_wrong], 
            alpha=0.2, point_size=7,  by_subj=True, subj_col='SubjectName', reps=50)
```

![](https://github.com/davidbestue/funciones/blob/master/imgs/bysubj_boxwhite.png)


By subject, no hue, ***fill the box***: use the argument fill_box=True and the alpha_box to set the opacity.  

```
linares_plot(x='Response', y='EventBaseline', order=['Correct', 'Wrong'], df=df, palette=[c_correct, c_wrong], 
            alpha=0.2, point_size=7,  by_subj=True, subj_col='SubjectName', reps=50, fill_box=True, alpha_box=0.2)
```

![](https://github.com/davidbestue/funciones/blob/master/imgs/bysubj_boxcolor.png)



### Plot Box hue: 

Add a hue and a legend. 
```
linares_plot(x='Response', y='EventBaseline', order=['Correct', 'Wrong'], df=df, palette=[c_correct, c_wrong], 
             hue='pers_l', hue_order=['High', 'Low'],
            alpha=0.2, point_size=7,  by_subj=True, subj_col='SubjectName', reps=50,
            fill_box=True, alpha_box=0.2)


```

![](https://github.com/davidbestue/funciones/blob/master/imgs/hue_bysubj.png)



### Plot line: 
Instead of the box, use a line to connect the data (continious x). Use the argument:  plot_box='line'
```
linares_plot(x='CenteredLevel', y='EventBaseline', order=[-2,-1,0,1,2], df=df, palette=['navy'], 
            alpha=0.2, point_size=7,  by_subj=True, subj_col='SubjectName', reps=50, plot_box='line')

```
![](https://github.com/davidbestue/funciones/blob/master/imgs/line_bysubj.png)



### Plot line hue: 
Instead of the box, use a line to connect the data (continious x). Use the argument:  plot_box='line'
```
linares_plot(x='CenteredLevel', y='EventBaseline', order=[-2,-1,0,1,2], hue='Response',
             hue_order=['Correct', 'Wrong'],  palette=[c_correct, c_wrong], 
             df=df, CI=0.68, alpha=0.2, point_size=7,  by_subj=True, subj_col='SubjectName', reps=50, plot_box='line')

```
![](https://github.com/davidbestue/funciones/blob/master/imgs/line_hue_bysubj.png)



### Plot mean: 
Instead of the box, use just the mean and the error bars. Use the argument:  plot_box='mean'.  
The Confidence interval is defined with the argument CI (in all the plots). Default is 0.95.  

```
linares_plot(x='CenteredLevel', y='EventBaseline', order=[-2,-1,0,1,2], df=df, palette=['navy'], CI=0.68,
            alpha=0.2, point_size=7,  by_subj=True, subj_col='SubjectName', reps=50, plot_box='mean')

```
![](https://github.com/davidbestue/funciones/blob/master/imgs/mean_bysubj.png)



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







