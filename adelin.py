#STOCK PRICE PREDICTION- Classification Problem

#imports
from sklearn.model_selection import train_test_split     
import numpy as np

#Reading csv file using numpy
wines = np.genfromtxt("/home/komali_priya/Documents/google.csv", delimiter=",", skip_header=0)
print("wines  ",wines)

#Normalizing
wines = wines.T
maxArray = []
for i in range (1 , len(wines)):
    maximum = max(wines[i])
    maxArray.append(maximum)
    k = 0
    for j in wines[i]:
        
        j = j/maximum
        wines[i][k] = j
        k = k+1
 
    
print(maxArray)
wines = wines.T

X = []
for i in range(len(wines)-1):
    X.append(wines[i])
X=np.asarray(X)

print("X is  ",X)

# Random Splitting of training and testing data 
X_train, X_test = train_test_split(X, test_size=0.4, random_state=36)
print("X_train is  ",X_train)

#Creating target lists
y_train = []
y_test = []
for i in X_train:
    j = int(i[0])
    j = j+1
    y_train.append(wines[j][1])
    
for i in X_test:
    j = int(i[0])
    j = j+1
    y_test.append(wines[j][1])

print("y_train",y_train)
train_target = []
for i in range(len(X_train)) :
    if (X_train[i][1] < y_train[i] ):
        train_target.append(1)     #"1" representing increase in stock price
    else:
         train_target.append(0)   #"0" representing decrease in stock price
print("train_target  ",train_target)

test_target = []
for i in range(len(X_test)) :
    if (X_test[i][1] < y_test[i] ):
        test_target.append(1)
    else:
         test_target.append(0)
print("test_target  ",test_target)

#TRAINING
#initializing weights
x0 = 1
w0 = 0.2
w1 = 0.2
w2 = 0.2 
w3 = 0.2 
w4 = 0.2
w00 = 0 
w11 = 0
w22 = 0
w33 = 0
w44 = 0

#function for modifying weights
def fun( w0 , w1 , w2 , w3 , w4 , x1 , x2 , x3 , x4 , target , w00 , w11 , w22 , w33 , w44 ):
    output = x0*w0 + x1*w1 + x2*w2 + x3*w3 + x4*w4
    n = 0.001
    w00 = w00 + n*(target-output)*(x0)
    w11 = w11 + n*(target-output)*(x1)
    w22 = w22 + n*(target-output)*(x2)
    w33 = w33 + n*(target-output)*(x3)
    w44 = w44 + n*(target-output)*(x4)
    w0 = w0 + w00
    w1 = w1 + w11
    w2 = w2 + w22
    w3 = w3 + w33
    w4 = w4 + w44
    return w0,w1,w2,w3,w4,w00,w11,w22,w33,w44
    

    
# Iterations
for i in range(1000):
    print("Iteration = ",i)
    for k in range(len(X_train)):
        x1 = X_train[k][1]
        x2 = X_train[k][2]
        x3 = X_train[k][3]
        x4 = X_train[k][4]
        target = train_target[k]
        w0,w1,w2,w3,w4,w00,w11,w22,w33,w44 = fun( w0 , w1 , w2 , w3 , w4 , x1 , x2 , x3 , x4 , target , w00 , w11 , w22 , w33 , w44 )


#TESTING
        
output01 = []  
for k in range(len(X_test)):
    x1 = X_test[k][1]
    x2 = X_test[k][2]
    x3 = X_test[k][3]
    x4 = X_test[k][4]
    target = test_target[k]
    #print(w0,w1,w2,w3,w4)
    output = x0*w0 + x1*w1 + x2*w2 + x3*w3 + x4*w4
    loss = ((target-output)**2)/2
    
    print("Loss : ",loss)
    print("output : ",output)   
    print("target : ",target)
    print("\n")
    if( output<0 ):
        output01.append(0)
    else:
        output01.append(1)
print("Target List :\n ",test_target)
print("Output List :\n ",output01) 

#Accuracy calculation
accuracy = 0
total = len(test_target) 
print("No. of testing tuples: ",total)
for i in range(len(test_target)):
    if( test_target[i] == output01[i] ):
        accuracy = accuracy+1
percentage = (accuracy*100)/total

print("Accuracy :  ",percentage)
        
   
    
            

        
    
    
 