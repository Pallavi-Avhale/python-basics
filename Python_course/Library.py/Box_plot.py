''' 
BOXPLOT

all the numerical data will be distributed into 
it will distributed based Quarterly


x=[10,20,30,40,50,60,70,80,90,100]

min-> 10
max-> 100
median-> 55

A Box Plot (or Box-and-Whisker Plot) is a graphical representation used to summarize the distribution of numerical data using the five-number summary:

Minimum Value
First Quartile (Q1)
Median (Q2)
Third Quartile (Q3)
Maximum Value

It helps visualize the spread, center, and outliers of the data.


Minimum    Q1      Median      Q3     Maximum
   |--------|=========|=========|--------|
                <--- Box --->


'''
# import matplotlib.pyplot as plt
# x=[10,20,30,40,50,60,70,80,90,100]
# plt.boxplot(x)
# plt.show()

''' 
min--> 10
max--> 90
median--> 50 -->Q2
first_quarter--> 
           20+30=50/2=25

Third_quarter--> 
           70+80= 150/2= 75

'''

# ------------------------------------------------------------

# import matplotlib.pyplot as plt
# x=[10,20,30,40,50,60,70,80,90]
# plt.boxplot(x)
# plt.show()


''' 
min--> 10
max--> 90
median--> 50 -->Q2
first_quarter--> 10,20,30,40,50----> 30 (Q1)
          

Third_quarter--> 60,70,80,90---> 70 Q3
          

'''

# vert-> To make Horzontal as well as vertical
# vert=True is vertical , By default if not mention it will take it as vertical
# vert=Flase --> Horizontal 

# import matplotlib.pyplot as plt
# v=[1,2,3,4,5,6,7,8,9,10]
# plt.boxplot(v,vert=True)
# plt.show()


''' 
min--> 1
max--> 10
median--> 5.5 -->Q2
first_quarter--> 1,2,3,4,----> 2+3/2= (Q1)
     
Third_quarter--> 
          

'''
# vert=Flase --> Horizontal  

# import matplotlib.pyplot as plt
# v=[1,2,3,4,5,6,7,8,9,10]
# plt.boxplot(v,vert=False)
# plt.show()


# label-->

# import matplotlib.pyplot as plt
# v=[1,2,3,4,5,6,7,8,9,10]
# plt.boxplot(v,vert=True, patch_artist=True)
# plt.grid()
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Boxplot")

# plt.show()


