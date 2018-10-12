# LSTM小例子，虽然我什么都不懂，但是能跑出结果就很开兴了
# 一个一个开始搞吧
# 呜呜呜，感觉被骗了，matlab 有相应的LSTM版本,但是没有LSTM回归的，就感觉很气啊，哼，希望matlab 2018b能有吧
import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# 前面都是一堆的包，没甚么好注释的
dataframe = read_csv('AirPassengers.csv', usecols=[1],
                     engine='python', skipfooter=3)
# 注意这个地方啊，usecols=[1]，就是说只使用第一行(从第0行开始数的);
# 这个数据只有 144个
dataset = dataframe.values  # dtype=int64
# 其实就是时间序列的值了
# 将整型变为float
dataset = dataset.astype('float32')  # 类型转换

plt.plot(dataset)  # 想想自己傻的很，原来这样也可以，可以不要自变量的取值范围的
plt.show()  # 显示图形


# X is the number of passengers at a given time (t) and Y is the number of passengers at the next time (t + 1).

# convert an array of values into a dataset matrix
# 这个地方我也比较迷
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return numpy.array(dataX), numpy.array(dataY)


# fix random seed for reproducibility
numpy.random.seed(7)
# 正则化数据
# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)  # 这个地方把所有的都变了，包括test,所以后面要把test再变回来

# split into train and test sets
train_size = int(len(dataset) * 0.67)  # %67的是训练数据
test_size = len(dataset) - train_size
train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
# 这个地方是将训练数据和测试数据分开，trainX是0：93号数据，trainY是1：94号数据
# use this function to prepare the train and test datasets for modeling
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
# reshape input to be [samples, time steps, features]，变换维度
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# create and fit the LSTM network,创建LSTM模型
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)

# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)  # 转换回来 94个 [124.275 129.42 (94,1)
trainY = scaler.inverse_transform([trainY])  # 转换回来   94个[118 ,132
testPredict = scaler.inverse_transform(testPredict)  # [314.82578,353.67865... 46
testY = scaler.inverse_transform([testY])  # [301 356.....]  46

trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:, 0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:, 0]))
print('Test Score: %.2f RMSE' % (testScore))
# shift train predictions for plotting
trainPredictPlot = numpy.empty_like(dataset)
trainPredictPlot[:, :] = numpy.nan
trainPredictPlot[look_back:len(trainPredict) + look_back, :] = trainPredict
# 1-94号元素赋值了
# shift test predictions for plotting
testPredictPlot = numpy.empty_like(dataset)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(trainPredict) + (look_back * 2) + 1:len(dataset) - 1, :] = testPredict
# 97-142号元素赋值了
# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset))  # 转换回来
plt.plot(trainPredictPlot)  # 画图像
plt.plot(testPredictPlot)  # 画图像
plt.show()