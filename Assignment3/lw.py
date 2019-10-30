#Amogha Sekhar, A53301791, CSE 250A

#import necessary libraries
import random
import matplotlib.pyplot as plt

#initialize values
n=10 #number of bits
alpha= 0.1 #noise level
z= 120 #given
count= 10000000 #number of iterations

values= [2,5,8,10]

numerator= 0
denominator= 0
bits= [0 for i in range(10)] #initialize to 0
constant= ((1-alpha)/(1+alpha))

#lists to store values for 2,5,8,10 for different iteration counts
l = []
plot_points= count/500 #for 500 different values

for i in values:
    temp_list = []
    for j in range(count):

        #Randomly generate numbers between 0 and 1
        bits= [random.randint(0,1) for i in range(10)]

        #Calculating f(B)
        #f(B)= sigma i=1 to n (2^i-1)*Bi
        temp= [(2**i)*bits[i] for i in range(10)]
        f_B= sum(temp)

        # Calculating P(Z|B1, B2, . . . , Bn)
        power= abs(z- f_B)
        prob= constant * pow(alpha, power)
        #summing all probabilities for denominator value of equation
        denominator+= prob
        if bits[i-1]== 1: #indicator function
            numerator+= prob

        #calculating probabilities for every 20000 iterations for plot
        if j%plot_points == 0 and j>0:
            t= numerator/denominator
            temp_list.append(t)

    temp= numerator/denominator
    l.append(temp_list)
    print(i, temp)


#Probabilties for all iteration counts for 2,5,8,10
l_2 = l[0]
l_5 = l[1]
l_8 = l[2]
l_10= l[3]

x_axis= [num for num in range(20000, 10000000, 20000)]

#Plotting
plt.plot(x_axis, l_2)
plt.plot(x_axis, l_5)
plt.plot(x_axis, l_8)
plt.plot(x_axis, l_10)
plt.legend(['2' ,'5', '8', '10'])
plt.xlabel('Number of iterations')
plt.ylabel('Probability')
plt.show()
