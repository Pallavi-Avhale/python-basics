''' 
Seaborn-->
If we want to display any graph in seaborn we have to use matplotlib

-> iT'S USE FOR DATA VISUALISATION ONLY

Matplotlib                                                 seaborn

-> To use seaborn -->
import seaborn as sns

--> seaborn will work on the basis of dataset
--> It works on the basis of table formate

'''

# To check the current version of seaborn--> 

# import seaborn as sns
# print(sns.__version__)

# print()

#  To check the whatever data set we are using in seaborn 

# print(sns.get_dataset_names())

''' 
# o/p->
['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'dowjones', 'exercise', 
 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic']
 '''

# If we want to create line chart in seaborn we want to use linplot()
# when we want to create a line chart in matplotlib in seaborn use plot()



# Matplotlib() vs seaborn()
# Using matplotlib

# import matplotlib.pyplot as plt

# x=[10,20,30]
# y=[12,13,14]
# plt.plot(x,y)
# plt.show()
# Each data variable should be connected--> there will be a connection

# using scatter-->

# x=[10,20,30]
# y=[12,13,14]
# plt.scatter(x,y)
# plt.show()

# If two variable data will display diffrent--> there will be no connection

''' 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.DataFrame({"age":[23,45,67,89],"sal":[1000,2000,3000,4000]})
print(df)

# To create line chart in seaborn we need to pass two parameter x-axis and y-axis --> also we have to five the data for this parameter-->
# --> parameters--> x-axis, y-axis and data=df  
# --> sns.lineplot(x-axis,y-axis, data=dataframe_name)

sns.lineplot(x="age",y="sal", data=df) 

# sns.show()         #--> AttributeError: module 'seaborn' has no attribute 'show' --> It will won't work

plt.show()

'''

# hue--> If u want to distribute your data on the basis of  color 

''' 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

d=pd.DataFrame({"Month":["Jan","Feb","March"],"Sales":[100,200,300],
                "Region":["West", "South","North"],"Profit":[20,30,40]})

print(d)

# o/p-->
#    Month  Sales Region  Profit
# 0    Jan    100   West      20
# 1    Feb    200  South      30
# 2  March    300  North      40

sns.lineplot(x="Month",y="Sales",data=d,hue="Region")
plt.show()

'''

# legend=True  --> If we want to show our use legend=True( or by default it will show)
# legend=Flase --> if we want to hide our legend use legend=Flase

''' 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

d=pd.DataFrame({"Month":["Jan","Feb","March"],"Sales":[100,200,300],
                "Region":["West", "South","North"],"Profit":[20,30,40]})

print(d)

# o/p-->
#    Month  Sales Region  Profit
# 0    Jan    100   West      20
# 1    Feb    200  South      30
# 2  March    300  North      40

sns.lineplot(x="Month",y="Sales",data=d,hue="Region",legend=True)     #to show legend
plt.show()

'''

# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# d=pd.DataFrame({"Month":["Jan","Feb","March"],"Sales":[100,200,300],
#                 "Region":["West", "South","North"],"Profit":[20,30,40]})

# print(d)

# # o/p-->
# #    Month  Sales Region  Profit
# # 0    Jan    100   West      20
# # 1    Feb    200  South      30
# # 2  March    300  North      40

# sns.lineplot(x="Month",y="Sales",data=d, hue="Region",legend=False)     #to hide  legend
# plt.show()

'''
# use marker
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

d=pd.DataFrame({"Month":["Jan","Feb","March"],"Sales":[100,200,300],
                "Region":["West", "South","North"],"Profit":[20,30,40]})

print(d)

# o/p-->
#    Month  Sales Region  Profit
# 0    Jan    100   West      20
# 1    Feb    200  South      30
# 2  March    300  North      40

sns.lineplot(x="Month",y="Sales",data=d, hue="Region",marker="o")     
plt.show()

'''

'''
Lineplot Parameters List
1.x---->variable for the x-axis
2.y--->varibale for the y-axis
3.data--->DataFrame containing the data
4.hue--->separate data into multiple colored line
5.style--->Changes line styles based on categories
6.palettes-->color
7.markers-->Display markers at data Points
8.dashes--->controls line styles(True/Fasle)
9.legend--->Controls legend display.
10.sizes--->Controls line width ranges.
11.size--->Maps numeric variables to line widths.
12.hue_order-->Specifies order of hue categories.
13.estimator-->Method used to aggregate repeated values.
'''

"""
Palettes color List
    'deep',
    'muted',
    'bright',
    'pastel',
    'dark',
    'colorblind'
    'Blues',
    'BuGn',
    'BuPu',
    'GnBu',
    'Greens',
    'Greys',
    'Oranges',
    'OrRd',
    'PuBu',
    'PuBuGn',
    'PuRd',
    'Purples',
    'RdPu',
    'Reds',
    'YlGn',
    'YlGnBu',
    'YlOrBr',
    'YlOrRd'
    'viridis',
    'plasma',
    'inferno',
    'magma',
    'cividis'
""" 
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# Q=sns.load_dataset("Datasetname")
# or
# Q1=pd.read_csv("Datasetname")
# OR 
# Q3=pd.read_excel("Datasetname")

''' 
range
arange
heatmap
'''

''' 
Heatmap---> In build fucntion

Not recommend in dataset, due to larage dataset

It work on single column

heatmap is a 2D



'''

# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x)
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True)
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues")
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple")
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple",vmin=4)
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple",vmax=4)
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple",vmax=7,vmin=3)
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple",vmax=7,vmin=3,
#             annot_kws={"size":20,"color":"blue"},
#             xticklabels=["A","B","C"],yticklabels=["P","Q","R"])
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple",vmax=7,vmin=3,
#             annot_kws={"size":20,"color":"blue"},
#             xticklabels=["A","B","C"],yticklabels=["P","Q","R"],
#             fmt="d")
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple",vmax=7,vmin=3,
#             annot_kws={"size":20,"color":"blue"},
#             xticklabels=["A","B","C"],yticklabels=["P","Q","R"],
#             fmt="1f")
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple",vmax=7,vmin=3,
#             annot_kws={"size":20,"color":"blue"},
#             xticklabels=["A","B","C"],yticklabels=["P","Q","R"],
#             fmt=".1f")
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple",vmax=7,vmin=3,
#             annot_kws={"size":20,"color":"blue"},
#             xticklabels=["A","B","C"],yticklabels=["P","Q","R"],
#             fmt=".2f")
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple",vmax=7,vmin=3,
#             annot_kws={"size":20,"color":"blue"},
#             xticklabels=["A","B","C"],yticklabels=["P","Q","R"],
#             fmt=".2f",square=True)
# plt.show()

# print()
# import seaborn as sns
# import matplotlib.pyplot as plt
# x=[[1,2,3],[4,5,6],[7,8,9]]
# sns.heatmap(x,annot=True, cmap="Blues",linewidths=3,linecolor="purple",vmax=7,vmin=3,
#             annot_kws={"size":20,"color":"blue"},
#             xticklabels=["A","B","C"],yticklabels=["P","Q","R"],
#             fmt=".2f")
# plt.show()


# import seaborn as sns
# print("Seaborn------->", sns.__version__)

# print()
# import pandas as pd
# print("Pandas------->", pd.__version__)
# print()

# import numpy as np
# print("Numpy------->", np.__version__)
# print()

# import matplotlib.pyplot 
# print("Matplotlib------->", matplotlib.__version__)

# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[5,6,7]])
# print(x)

# sns.heatmap(x,annot=True,fmt="1%")

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[5,6,7]])
# print(x)

# sns.heatmap(x,annot=True,linewidths=0.7)

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[5,6,7]])
# print(x)

# sns.heatmap(x,annot=True,linewidths=0.7,linecolor="yellow")

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[5,6,7]])
# print(x)

# sns.heatmap(x,annot=True,linewidths=0.7,linecolor="yellow", cmap="Blues")

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[5,6,7]])
# print(x)

# sns.heatmap(x,annot=True,linewidths=0.7,linecolor="yellow", cmap="Blues", cbar=True)

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[5,6,7]])
# print(x)

# sns.heatmap(x,annot=True,linewidths=0.7,linecolor="yellow", cmap="Blues", 
#             cbar=True, square=True )

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[5,6,7]])
# print(x)

# sns.heatmap(x,annot=True,linewidths=0.7,linecolor="yellow", cmap="Blues", 
#             cbar=True, square=True , xticklabels=["A","B","C"], yticklabels=["P","Q","R"])

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[5,6,7]])
# print(x)

# sns.heatmap(x,annot=True,linewidths=0.7,linecolor="yellow", cmap="Blues", 
#             cbar=True, square=True , xticklabels=["A","B","C"], yticklabels=["P","Q","R"],
#             vmin=0, vmax=1)

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x)

# sns.heatmap(x,annot=True,linewidths=0.7,linecolor="yellow", cmap="Blues", 
#             cbar=True, square=True , xticklabels=["A","B","C"], yticklabels=["P","Q","R"],
#             vmin=0, vmax=12)

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x)

# sns.heatmap(x,annot=True,linewidths=0.7,linecolor="yellow", cmap="viridis", 
#             cbar=True, square=True , xticklabels=["A","B","C"], yticklabels=["P","Q","R"],
#             vmin=0, vmax=12, annot_kws={"size":20,"color":"red"})

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x)

# sns.heatmap(x,annot=True,linewidths=0.7,linecolor="yellow", cmap="viridis", 
#             cbar=True, square=True , xticklabels=["A","B","C"], yticklabels=["P","Q","R"],
#             vmin=0, vmax= 12, annot_kws={"size":20,"color":"pink"}, cbar_kws={"label":"color_information"})

# plt.xlabel("X-AXIS",fontsize=15,color="purple")
# plt.ylabel("Y-AXIS",fontsize=15,color="purple")
# plt.title("Heat_Map",fontsize=20,color="purple")

# plt.show()


# Perfect Positive Corelation ---> when two variable is present they both depend on each other, and both the variable value will be increasing

# Study        Marks
# 2             60
# 4             80
# 6             95

# Perfect Positive Corelation ---> When two variable is present they both are not depend on each other and the 
#                                  one variable value will be increasing else other varible value is decreasing

# web-series        Marks



# Correlation Formula (Text):

# r = Σ((x - x̄)(y - ȳ)) / √[Σ(x - x̄)² × Σ(y - ȳ)²]

# Where:

# r = Correlation coefficient
# x = Value of variable X
# y = Value of variable Y
# x̄ = Mean of X
# ȳ = Mean of Y
# Σ = Summation (total)

# w = d[["total_bill","tip"]].head()

# | total_bill (X) | tip (Y) |
# | -------------- | ------- |
# | 16.99          | 1.01    |
# | 10.34          | 1.66    |
# | 21.01          | 3.50    |
# | 23.68          | 3.31    |
# | 24.59          | 3.61    |


# Xˉ=516.99+10.34+21.01+23.68+24.59​
#     -------------------------
#               5

#    96.61
#    ----   =  Xˉ=19.322
#     5
# Yˉ=51.01+1.66+3.50+3.31+3.61​
#     -------------------------
#               5

    #  13.09​
#    ----   =  Yˉ=2.618
#     5



# |     X |    Y |   X−X̄  |    Y−Ȳ | (X−X̄)(Y−Ȳ)  | (X−X̄)²  | (Y−Ȳ)² |
# | ----: | ---: | -----: | -----: | ----------: | ------: | -----: |
# | 16.99 | 1.01 | -2.332 | -1.608 |       3.750 |   5.438 |  2.586 |
# | 10.34 | 1.66 | -8.982 | -0.958 |       8.605 |  80.676 |  0.918 |
# | 21.01 | 3.50 |  1.688 |  0.882 |       1.489 |   2.849 |  0.778 |
# | 23.68 | 3.31 |  4.358 |  0.692 |       3.016 |  18.992 |  0.479 |
# | 24.59 | 3.61 |  5.268 |  0.992 |       5.226 |  27.752 |  0.984 |


# Step 3: Calculate Sums

# ∑(X−Xˉ)(Y−Yˉ)=22.086
# ∑(X−Xˉ)2=135.707
# ∑(Y−Yˉ)2=5.745


# Step 4: Apply Correlation Formula

# Pearson Correlation:


            #      Σ[(X - X̄)(Y - Ȳ)]
            #  r=---------------------
            #     √[Σ(X - X̄)² × Σ(Y - Ȳ)²]

''' 
PAIRPLOT--->

EDA--> Exploratory Data Analysis
In pair plot only we use Numerical column to perform EDA
C1-C2-->IT CREATE SUBPLOT--> AT A TIME IT WILL CRAETE IT'S ALWAYS SCATTER OR HISTOGRAM --> BINS--. GROUPS

SYNTAX OF PAIR PLOT--> sns.pairplot(dataFram)--> the new varible use to store numerical data



'''

''' 
Barplot---> 
To use compare Number column (Numerical data) with Character data (String)

Part of Barplot-->
Countplot()---> We use only 1 axiz at a time--> either x-axiz or y-axis

90% we use Categorical data
Used to check categorical data



'''
import matplotlib.pyplot as plt
import seaborn as sns


df=sns.load_dataset("tips")
print(df)

sns.barplot(x="total_bill",y="day",data=df)
plt.show()


sns.barplot(x="total_bill",y="day",data=df,hue="sex")
plt.show()

sns.barplot(y="total_bill",x="day",data=df,hue="sex")
plt.show()

sns.countplot(x="day",data=df)
plt.show()

sns.countplot(x="sex",data=df)
plt.show()

sns.countplot(y="sex",data=df)
plt.show()

sns.countplot(x="smoker",data=df)
plt.show()

sns.countplot(x="time",data=df)
plt.show()

sns.countplot(x="smoker",data=df, hue="sex")
plt.show()

sns.countplot(y="smoker",data=df, hue="sex")
plt.show()

sns.countplot(x="smoker",data=df, hue="sex",palette="PuRd")
plt.show()