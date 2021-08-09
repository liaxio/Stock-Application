# Stock-Application with LSTM model
 
this application is build using streamlit we application adding with pycharm software. Through this application, you can see the closing pirce, volume of desired stocks. 
- if 100 days crosses above the 200 moving avarage, there is an uptrend. If its below the 200 ma, then it is a downtrend. 
- yahoo finance :  for scaping the data 
- used bigger time frame for the data set to have accuracy in the model.
- datareader : to scrap data from yahoo 
- df.head : to see the starting data
- df.tail : end data
- plt.plot : to plot the closing price of stocks from the data 
- 100MA : it will start from the day of 101 value , take previous 100 closing value and find the mean. then plot  
          ma100 = ds.close.rolling(100).mean()
- df.shape : to show the rows and coloums. We will be working on one colume only which is closing price

          #spliting data into data training and data testing
          
- data_training : used previous dataset starting from zero index and will go 70% of the total values (70% training data)
- data_testing : started from that 70% and going till the complete length (30%testing data)

            #scaling data 
- imported MinMaxscaler from sklearn
- data_training_array :converted into array  to fit data in scaler range
- x_train || y_train : y_train depends on x_train. x_train is previous data(100 past day) , y_train is predisted (101 day)
- for loop : pushing values till the new day and add the new predicted to the  x_train
- convert x_train y_train into numpy array to provide the data to LSTM
- 
         #MACHINE LEARNING MODEL
          
- used keras package to import sequence [imension of the inner cells in LSTM] made 4 layers in LSTM model
         LSTM ( cell, input gate, output gate , forget gate)
- model.add(DENSE) :to connect all 4 layers.
 [Dense layer feeds all outputs from the previous layer to all its neurons, each neuron providing one output to the next layer]
- model.compile(adam opitimizer) : replacement optimization algorithm for stochastic gradient descent for training deep learning models.
                                   [Adam optimization is an algorithm that can be used to update network weights iteratively based on training data]
- saved the model as 'keras_model.h5'


      #MAKING PREDiCTION
 - x_test || y_test : x-test append with input data 0 till i 
                      y_test append with input data i to new data[0]
 - x_test.shape is x_test.shape is (877, 100, 1), y_test shape is 877
 - make prediction for x_test
 - find scale factor 
 - multiply scale factor with y prediction to get predicted value
- plot the value and make figure for predcition vs original price 
- 
                      
      
 
 
