- Function to calculate the int. error

- Function to calvulate visual angles

- Dot function for plots

Dot plot function



Example with 1

dotplot(df=df, columns='A_err', subjects='subject', colors='k', xnames='Cond1')


#Example of the dotplot function with 1
![](https://github.com/davidbestue/funciones/blob/master/download%20(1).png)



Example with 2


dotplot(df=df, columns=['A_err', 'A_err_abs' ], subjects='subject', colors=['r', 'g'], xnames=['cond1', 'Cond2'],
        title='Conditions plot', xlabel='', ylabel='value')

#Example of the dotplot function with 2
![](https://raw.githubusercontent.com/davidbestue/funciones/master/download.png)

