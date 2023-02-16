import math
import matplotlib.pyplot as plt

coordinates={'x':[],'y':[]}

# coordinates['x']=[1,2,3,4,5]
# coordinates['y']=[1,2,3,4,5]
while(True):
    coordinates['x'].append(float(input("Enter x- cordinate")))
    coordinates['y'].append(float(input("Enter y- cordinate")))
    
    if len(coordinates['x'])>5:
        print("Can only input 4 data")
        break

plt.scatter(coordinates["x"],coordinates["y"])
plt.show()

a= input ("Which variable is predictor x or y ")
if (a=="x"):
    predictor=coordinates["x"]
    response=coordinates['y']
else:
    predictor=coordinates['x']
    response=coordinates['y']

def mean(numbers):
    length=len(numbers)
    mean_sum=0.0
    for number in numbers:
        mean_sum+=number
    return mean_sum/length

def standard_deviation(numbers):
    mean_number=mean(numbers)
    squared_sum=0
    length=len(numbers)

    for number in numbers:
        squared_sum += math.pow(number-mean_number,2)
    return math.sqrt(squared_sum / (length-1))

def covariance(numbers1,numbers2):
    mean_number1=mean(numbers1)
    mean_number2=mean(numbers2)
    length=len(numbers1)
    
    sum_product=0.0

    for num1,num2 in zip(numbers1,numbers2):
        sum_product+=((num1-mean_number1)*(num2-mean_number2))   

    return sum_product/(length-1)

def pearson_corelation(numbers1,numbers2):
    return covariance(numbers1,numbers2)/(standard_deviation(numbers1)*standard_deviation(numbers2))

pearson_value=pearson_corelation(predictor,response)
mean_predictor= mean(predictor)
mean_response= mean(response)
sd_predictor= standard_deviation(predictor)
sd_response= standard_deviation(response)

coefficent_b= pearson_value * (sd_predictor/sd_response)
coefficent_a= mean_response - coefficent_b* mean_predictor

print ("The equation is y = {0}  + {1} x".format(coefficent_a,coefficent_b))

def sst():
    sum=0.0
    for number in response:
        sum += pow(number-mean_response,2)
    return sum
def predicted_number():
    numbers=[]
    for number in predictor:
        numbers.append(coefficent_a + coefficent_b * number)
    return numbers


def ssr():
    sum=0.0
    numbers=predicted_number()
    for number in numbers:
        sum += pow(number-mean_response,2)
    return sum

r_squared = ssr()/sst()        
print ("r_squared is equal to {0}".format(r_squared))
plt.plot(predicted_number(),predictor)
plt.scatter(predicted_number(),predictor)
plt.show()




