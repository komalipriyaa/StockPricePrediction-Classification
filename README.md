# StockPricePrediction-Classification

STOCK PRICE PREDICTION-CLASSIFICATION PROBLEM
USING ADALINE AND NEURAL NETWORKS


ABSTRACT:
Stock market is a very challenging and interesting field. In this paper we are trying to classify whether the target prices are going to increase or decrease the next day. We are predicting the target price individually for 5 different companies. In each company 4 attributes are considered which help us predict the prices. The techniques used for this is adaline . By using these algorithms, we are trying to find connection weight for each attribute, which helps us in predicting the target price of the stock. An input for each attribute is given to a sigmoid function after that it is amplified based on its connection weight. The experimental results show that using this approach for predicting whether the stock price has increased or decreased is promising. In each case the algorithms were able to predict with an accuracy of at least 75%. 
 
 Keywords:
Machine Learning, stock market, Adaline , neural networks.

INTRODUCTION:
A stock market, equity market or share market is the aggregation of buyers and sellers (a loose network of economic transactions, not a physical facility or discrete entity) of stocks (also called shares). The prediction of the stock prices has always been a challenging task. It has been observed that the stock prediction of any company does not necessarily depend on the economic conditions of the country. It is not directly linked with the economic development of the country or particular area anymore. Thus the prediction of stock price has become even more difficult than before.
There are many factors that influence the stock price. At the most fundamental level, supply and demand in the market determine stock price. When demand for shares exceeds supply, which means the buyers are more than sellers, the prices increase. When demand is less than supply, meaning that buyers are less than sellers, the prices decrease.
Fluctuations in the economy feature what are commonly referred to as booms and depressions also affect the stock prices. Under favourable conditions share prices are at their peak and their lowest point is experienced during depressions. Share prices gradually rise during recovery and fall during recessions. Political factors that range from relations with other nations to government policies can affect share prices.
In this project, we are trying to predict whether the highest price is going to increase or    decrease on the next day. In this paper, we are trying to predict the price of five different companies (Google, Microsoft, Adobe, Apple, IBM). For each company, we are predicting the price of the stock of three different companies. For each company we are trying to predict whether the highest price is increasing or decreasing the next day. Thus, it is a classification problem with only two classes.
In this paper we use two evolutionary strategies to predict the stock price. They are:
Using  Adaline Technique.

ADALINE:
    AdaLiNe , abbreviated as Adaptive Linear Neuron, is a primitive single layered Artificial Neural Network.  It is a slight modification of the standard (McCulloch-Pitts) Perceptron.
    The main difference between the Perceptron and AdaLiNe is that the activation function is removed and the weights are adjusted according to the weighted sum of the inputs, in the learning phase where as in perceptron, the weighted sum of inputs is passed to an activation function(in general, signum function).
    It can also be implemented with multiple layers which then becomes a multi-layered Adaline,  namely MADALINE.The sole layer in the Adaline contains multiple nodes where each node takes multiple inputs and generates one output. 
Variables:
    xi - input attribute
    wi- weight corresponding to the attribute xi
    ∆wi- change in the weights 

Algorithm:    
    Step 1: Initialise the weights (value in range(0,1)).
    Step 2: Calculate the weighted sum(∑wixi).
    Step 3: Modify the weights and go to step 2 until the error is minimised.
Error is calculated using the Least Mean Square method.
    E = ∑1/2(target-output)2
Modifying Weights:
    wi 🡨 wi + ∆wi
    where  ∆wi = ƞ(target-output)xi 

 
The average accuracy obtained is 74.45%.





NEURAL NETWORKS
These artificial networks may be used for predictive modelling , adaptive control and applications where they can be trained via a dataset. Self-learning resulting from experience can occur within networks, which can derive conclusions from a complex and seemingly unrelated set of information.
Variables:
    xij -  input from unit I into unit j
    wij - weight from unit I to unit j
    ∆wji – change in weight

Algorithm:
    Step1: Initialize the network weights (value in range (0, 1))
    Step2: Calculate the output 
    Step3: Modify the weights and repeat the Step2 until the error is minimised
Error is calculated using the Least Mean Square Method.
Modifying Weights:
    wji  🡨  wji + ∆wji
    ∆wji = ƞ ẟj xji 


 
The average accuracy obtained is 75.5 %.





RESULT:
There are different ways to predict the stock. In this paper Neural Networks and Adaline methods are used. The stock classification problem has initially been solved using the genetic algorithm technique.
The genetic algorithm approach has given an accuracy of 73.87%[2] . Whereas, Adaline has produced even more promising results. The average accuracy for the Adaline technique is 74.75% . In this paper we have taken into consideration five different companies namely, Apple, Microsoft, Google, IBM and Adobe. They have produced an accuracy of 76%, 75%, 77.75%, 72.5% and 71% respectively.
The neural networks technique has also produced excellent results. The average accuracy being 75.5% . It has produced an accuracy of 77%, 76.4%, 72.6%, 74.75%, 76.78% for the companies Google, Microsoft , Adobe,Apple IBM respectively.

CONCLUSION AND FUTURE WORK:
The evolutionary techniques used  in this field looks promising and this is a very wide and interesting domain. Therefore, there is a lot of scope for futher research. This is a real world  problem , thus an algorithm with even more accuracy would be even more useful. As the used algorithms in this paper have produced an accuracy around 75% , these are a very good approach to classify the stock . We have used an input tuples of 1000 for each company. Results can be produced for smaller and even bigger data using the same logic.


REFERENCES:
[1] Jyh-Shing Roger Jang, Chuen-Tsai Sun, EijiMizutani, “Neuro-Fuzzy and Soft Computing, A Computational Approach to Learning and Machine Intelligence”, Prentice Hall, Upper Saddle River, NJ 07458, pp. 175-180.
[2]Sonal sable, Ankita Porwal, Upendra Singh, “Stock Price Prediction Using Genetic Algorithms And Evolution Strategies”, International Conference on Electronics, Communication and Aerospace Technology, 2017.
[3] Tom M. Mitchell, “Machine Learning”, McGraw-Hill Science/Engineering/Math, pp. 86-101.
[4]Fabrizio Romano, “Learning Python, Learn to code like a professional with Python-an open source, versatile, and powerful programming language”, Prod. Ref.: 1171215, Pact Publishing Ltd., Birmingham B3 2PB, UK.
[5]Mahdi PakdamanNaeini, HamidrezaTaremian, HomaBaradaran Hashemi, “Stock Market Value Prediction Using Neural Networks”, 2010 International Conference on Computer Information Systems and Industrial Management Applications(CISIM), DOI: 10.1109/CISIM.2010.5643675, Source: IEEE Xplore.
