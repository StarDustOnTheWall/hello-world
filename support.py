def print_func( par ):
    print ("Hello : ", par)
    return

def fib(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

import numpy
# split input and output
from numpy import array
# define array
data = array([[11, 22, 33],
		[44, 55, 66],
		[77, 88, 99],[15,16,17],[18,19,20],[21,22,23],[24,25,26]])
# separate data
X, y = data[:,:-1], data[:, -1]
print(X)
print(y)


# dataframe
import pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)

url = "/Users/xudi/DiXu/软件教程/python/study/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
print(data.shape)
print(data.head(20))
print(data.describe())
print(data.corr())
data.hist()
from matplotlib import pyplot
data.plot(kind='box')
from pandas.plotting import scatter_matrix
scatter_matrix(data)
#pyplot.show()

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import binarize
array = data.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
# summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:10,:])
birescaledX=binarize(rescaledX,threshold=0)
print(birescaledX[0:10,:])

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = LogisticRegression(solver='liblinear')
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy: %.3f%% (%.3f%%)" % (results.mean()*100.0, results.std()*100.0))
results2 = cross_val_score(model, X, Y, cv=kfold, scoring='neg_log_loss')
print("Logloss: %.3f (%.3f)" % (results2.mean(), results2.std()))
