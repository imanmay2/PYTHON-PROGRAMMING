import matplotlib.pyplot as plt
import numpy as np


#WAP that will draw line diagram from (0,0) to position (6,250)
def diag1():
    plt.title("1st Line diagram!")
    xp=np.array([0,6])
    yp=np.array([0,250])
    plt.plot(xp,yp)
    plt.show()


#WAP that will draw line diagram from (1,3) to position (8,10)
def diag2():
    plt.title("2nd Line Diagram!")
    plt.plot(np.array([1,8]),np.array([3,10]))
    plt.show()

    
#WAP that will plot 2 points from (1,3) to position (8,10)
def point1():
    plt.title("Plotting 2 points")
    plt.plot(np.array([1,8]),np.array([3,10]),'o')
    plt.show()



# WAP that will draw multiple line diagram from position(1,3) to (2,8)to (6,1)
#   and finally to (8,10) with various configurations
def multi_line():
    plt.title("Multiple Lines!!")
    plt.plot(np.array([1,2,6,8]),np.array([3,8,1,10]),marker='*',ms='20',mec='r',mfc='r',ls='dotted',color='m',linewidth='20')
    plt.show()


# WAP that will draw line for only y co-ordinates given
def y_():
    plt.title("DEFAULT-X")
    plt.plot(np.array([3,8,1,10,5,7]))
    plt.show()


#WAP that will draw two lines of dotted and of red colour of users choice
    # And also label the x-axis and y-axis, according to the users choice.
    # Also set font for title of the graph , xlabel and ylabel.
    # Also put a grid.
def multi_():
    font_title={'family':'serif','color':'red','size':30}
    font_labels={'family':'serif','color':'blue','size':16}
    plt.title("SPEED V/S TIME",fontdict=font_title,loc='left')
    x_axis=input("Enter the name to label x-axis: ")
    y_axis=input("Enter the name to label y-axis: ")
    plt.plot(np.array([3,8,1,10]),marker='*',color='red',ls="dotted")
    plt.plot(np.array([6,2,7,16]),marker='*',color='red',ls="dotted")
    plt.xlabel(x_axis,fontdict=font_labels)
    plt.ylabel(y_axis,fontdict=font_labels)
    plt.grid(color='m',ls='dotted',lw=1)
    plt.show()


# WAP that will plot 2 graph along with grid side by side.
def sub_plot():
    plt.title("SUBPLOTTING",fontdict={'family':'serif','size':30})
    #PLOT 1
    plt.subplot(1,2,1)
    plt.plot(np.array([3,6,9,12,16]))
    #PLOT 2
    plt.subplot(1,2,2)
    plt.plot(np.array([4,8,12,16,20]))
    plt.show()


# WAP that will plot 2 graph along with grid side by side.
    # ALSO give title for each and also for the entire 2 graphs.
def sub_plot2():
    
    #PLOT 1
    plt.subplot(1,2,1)
    plt.plot(np.array([3,6,9,12,16]))
    plt.title("SALES",fontdict={'family':'serif','size':16,'color':'blue'})
    #PLOT 2
    plt.subplot(1,2,2)
    plt.plot(np.array([4,8,12,16,20]))
    plt.title("INCOMES",fontdict={'family':'serif','size':16,'color':'blue'})
    plt.suptitle("SUB PLOTTING",fontdict={'family':'serif','size':30,'color':'red'})
    plt.show()


#SCATTERRING THE PLOT....consider two plots and scatter in 2 different colours.
def scater():
    plt.scatter(np.array([10,4,12,56,34,23]),np.array([4,6,5,3,7,8,]),c='r')
    plt.scatter(np.array([15,9,17,61,39,28]),np.array([14,16,15,13,17,18,]),c='b')
    plt.show()



#SCATTER A PLOT HAVING UNIQUE COLORS FOR 6 POINTS.
def uniq_scatter():
    plt.title('UNIQUE COLOURS!!')
    plt.scatter(np.array([12,16,2,4,8,10]),np.array([1,2,3,4,5,6]),c=np.array(['m','b','r','g','k','y']))
    plt.show()
uniq_scatter()
