# Matplotlib-->   visualization tool/library
# charts, mathmatics,
# it is one of the package, and open source library

# Step1--> import matplotlib.pyplot as plt
# mat--> mathmatics
# plot-->package
# lib--> library

# import matplotlib.pyplot as plt              

# pyplot--> It is a module which present inside the package ,
            # Inside pyplot all modules will be present
            # line charts--> stack.
            # bar chart--> area
            # scatter--> grid
            # list
# plt--> alias name 

# axis--> dimension
# axes--> Place of the chart

'''
x-axis
yaxis
Linstyle/ls
solid-->"-"
Dashed--> "--"
Dotted--> ":"
dashdot--> "-."
None
z-axiz
axes
change colour
'''
# Figure and Axes

# +--------------------------------------+
# |              Figure                  |
# |                                      |
# |   +------------------------------+   |
# |   |           Axes               |   |
# |   |                              |   |
# |   |        Graph/Chart           |   |
# |   |                              |   |
# |   +------------------------------+   |
# |                                      |
# +--------------------------------------+

# Figure → Complete window containing the graph.
# Axes → Area where the graph is drawn.


# Axis

# An axis represents a dimension.
#           Y-axis
#             ↑
#             |
#             |
#             |
# ------------+------------→ X-axis
#             |
#             |

# X-axis → Horizontal axis
# Y-axis → Vertical axis

# For 3D plots:

# X-axis
# Y-axis
# Z-axis

# Example:

# from mpl_toolkits.mplot3d import Axes3D
 
# to create line chart we need to use function 
# plot()--> what chart we nedd to create , show()--> display what chart we created


# Axes (Plural)
# Axis = One line (X or Y)
# Axes = Complete plotting area

#         Y-axis
#           ↑
#           |
#           |
# ----------+----------→ X-axis

# This whole plotting region is called Axes.

# plot--> plot function will accept multiple arguments

#linechart--> To show the trend analysis we use link chart

# import matplotlib.pyplot as plt
# student_life=["Study","Playing","Movies","Sleeping"]
# Hour=[15,30,45,24]
# plt.pie(Hour,labels=student_life,
#         colors=["green","yellow","pink","blue"],
#         explode=[0.0,0.0,0.0,0.0],
#         autopct="%1.0f%%")

# plt.show()


''' 
Histogram--->

--> It will distribute data on the basis of range.
--> It will accept only numerical data
--> It will take group wise orientation
--> by default it eill take 10 groups

'''
# 4. Parameters / Properties Table
# | Sr No | Parameter   | Meaning                   | Example           |
# | ----- | ----------- | ------------------------- | ----------------- |
# | 1     | x           | Input data                | `x=data`          |
# | 2     | bins        | Number of intervals       | `bins=5`          |
# | 3     | range       | Histogram range           | `range=(0,100)`   |
# | 4     | density     | Normalize frequencies     | `density=True`    |
# | 5     | weights     | Weight for each value     | `weights=w`       |
# | 6     | cumulative  | Cumulative histogram      | `cumulative=True` |
# | 7     | bottom      | Starting height           | `bottom=10`       |
# | 8     | histtype    | Histogram style           | `'bar'`           |
# | 9     | align       | Bin alignment             | `'left'`          |
# | 10    | orientation | Vertical/Horizontal       | `'horizontal'`    |
# | 11    | rwidth      | Relative bar width        | `0.8`             |
# | 12    | log         | Logarithmic scale         | `True`            |
# | 13    | color       | Bar color                 | `'red'`           |
# | 14    | label       | Legend label              | `'Marks'`         |
# | 15    | stacked     | Stack multiple histograms | `True`            |
# | 16    | edgecolor   | Border color              | `'black'`         |
# | 17    | linewidth   | Border thickness          | `2`               |
# | 18    | alpha       | Transparency              | `0.5`             |


# import matplotlib.pyplot as plt

# x=[10,11,12,13,14,15,20,21,21,23,24,30,31,32,33,40]
# plt.hist(x)
# plt.show()


# import matplotlib.pyplot as plt

# x=[10,11,12,13,14,15,20,21,21,23,24,30,31,32,33,40]
# plt.hist(x,bins=5)
# plt.show()

# color--->

# import matplotlib.pyplot as plt

# x=[10,11,12,13,14,15,20,21,21,23,24,30,31,32,33,40]
# plt.hist(x,bins=5, color="skyblue")
# plt.show()


# edgecolor--> 

# import matplotlib.pyplot as plt

# x=[10,11,12,13,14,15,20,21,21,23,24,30,31,32,33,40]
# plt.hist(x,bins=5, color="skyblue",edgecolor="green")
# plt.show()


# rwidth--->

# import matplotlib.pyplot as plt

# x=[10,11,12,13,14,15,20,21,21,23,24,30,31,32,33,40]
# plt.hist(x,bins=5, color="skyblue",edgecolor="green", rwidth=0.6)
# plt.show()


# bins=4--> 

# import matplotlib.pyplot as plt
# Marks=[20,21,23,30,31,32,33,40,41,50]
# plt.hist(Marks,bins=4)

# plt.show()


# import matplotlib.pyplot as plt
# Marks=[20,21,23,30,31,32,33,40,41,50]
# plt.hist(Marks,bins=4,edgecolor="yellow", color="blue",rwidth=0.4)

# plt.show()


''' 
20-->24-->3
25-->30-->1
31-->40-->4
41-->50-->2

'''
# histtype="step"--> it will show black

# import matplotlib.pyplot as plt
# Marks=[20,21,23,30,31,32,33,40,41,50]
# plt.hist(Marks,bins=4,edgecolor="yellow", color="blue",rwidth=0.4, histtype="step")

# plt.show()


#  histtype="stepfilled"---> it show color filled data
# import matplotlib.pyplot as plt
# Marks=[20,21,23,30,31,32,33,40,41,50]
# plt.hist(Marks,bins=4,edgecolor="yellow", color="blue",rwidth=0.4, histtype="stepfilled")

# plt.show()

# histtype="barstacked"--> it will show bar chat formate data 

# import matplotlib.pyplot as plt
# Marks=[20,21,23,30,31,32,33,40,41,50]
# plt.hist(Marks,bins=4,edgecolor="yellow", color="blue",rwidth=0.4, histtype="barstacked")

# plt.show()

# orientation="horizontal"-->
# import matplotlib.pyplot as plt
# Marks=[20,21,23,30,31,32,33,40,41,50]
# plt.hist(Marks,bins=4,edgecolor="yellow", color="blue",rwidth=0.4, histtype="barstacked",orientation="horizontal",alpha=0.5)

# plt.show()


# labels-->
# import matplotlib.pyplot as plt
# Marks=[20,21,23,30,31,32,33,40,41,50]
# plt.hist(Marks,bins=4,edgecolor="yellow", color="blue",rwidth=0.4, histtype="barstacked",orientation="horizontal",alpha=0.5)

# plt.xlabel("Marks_Data")
# plt.ylabel("inf_data")
# plt.title("Informations")
# plt.legend()
# plt.grid()

# plt.show()

# import matplotlib.pyplot as plt
# Marks=[20,21,23,30,31,32,33,40,41,50]
# plt.hist(Marks,bins=4,edgecolor="yellow", color="blue", orientation="horizontal",alpha=0.5)

# plt.xlabel("Marks_Data")
# plt.ylabel("inf_data")
# plt.title("Informations")
# plt.legend()
# plt.grid()

# plt.show()


# Vrtical--> orientation 

# import matplotlib.pyplot as plt
# Marks=[20,21,23,30,31,32,33,40,41,50]
# plt.hist(Marks,bins=4,edgecolor="red", color="Skyblue",alpha=0.5)

# plt.xlabel("Marks_Data")
# plt.ylabel("inf_data")
# plt.title("Informations")
# plt.legend()
# plt.grid()

# plt.show()


# import matplotlib.pyplot as plt
# Marks=[20,21,23,30,31,32,33,40,41,50]
# plt.hist(Marks,bins=4,edgecolor="red", color="Skyblue", rwidth=0.4, histtype="barstacked", alpha=0.5)

# plt.xlabel("Marks_Data")
# plt.ylabel("inf_data")
# plt.title("Informations")
# plt.legend()
# plt.grid()

# plt.show()



# 1.Which function is used to create
# a line chart in Matplotlib?
# ans-->plot()

# 2.Why do we use Line Charts?
# ans-->Line charts are used to show trends or changes over time.

# 3.What are the important parameters of plt.plot()?
# ans-->color
#     linestyle
#     linewidth
#     marker
#     label
#     markersize

# 4.What is the use of the marker parameter?
# ans-->It highlights individual data points on the line.

# 5.How do you add multiple lines to a graph
# ans--> plt.plot(x, y1, label='Line 1')
# plt.plot(x, y2, label='Line 2')
# plt.legend()

# 6.Which function is used to create a bar chart?
# ans-->bar()

# 7.Why do we use Bar Charts?
# ans->Bar charts are used to compare categorical data.

# 8.What is the difference between bar() and barh()
# ans--> bar()`            `barh()`             
# ------------------  -------------------- 
#  Vertical Bar Chart  Horizontal Bar Chart 

# 9.What is a Grouped Bar Chart?
# ans-->A chart used to compare multiple datasets side by side.

# 10.Which function is used to create a Pie Chart?
# ans-->pie()

# 11.Why do we use Pie Charts?
# ans-->Pie charts show parts of a whole or percentages.

# 12.What does autopct do?
# ans-->It displays percentage values on pie slices.

# 13.What is the use of explode?
# ans-->It separates a slice from the pie chart for emphasis

# 14.What is the purpose of startangle?
# ans-->It rotates the starting position of the pie chart.

# 15.Which function is used to create a Scatter Plot?
# ans-->scatter()

# 16.Why do we use Scatter Plots?
# ans-->Scatter plots show the relationship between two numerical variables.

# 17.What does the s parameter represent?
# ans-->t controls the size of scatter points.

# 18.What does the alpha parameter do?
# ans-->t controls the transparency of points.

# 19.How do you change marker styles in Scatter Plot?
# ans-->plt.scatter(x, y, marker='*')

# 20.Which function is used to create a Histogram?
# ans-->hist()

# 21.Why do we use Histograms?
# ans-->Histograms are used to show the distribution of numerical data.

# 22.What are Bins in Histogram?
# ans-->Bins are groups or intervals used to organize numerical data.

# 23.What is the default number of bins?
# ans-->10

# 24.Difference between Histogram and Bar Chart?
# Histogram   ------------ Bar Chart        
# Numerical Data          Categorical Data 
# Bars Touch              Bars Have Gaps   
# Shows Distribution      Shows Comparison 

# 25.How do you change the figure size?
# ans-->plt.figure(figsize=(10,5))

# 26.Which function displays the graph?
# ans-->plt,show()
