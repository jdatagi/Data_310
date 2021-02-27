## Part 1: Convolutions

#### Question 1: Convolve the two 3x3 matrices that were assigned to you with your 9x9 matrix and calculate the resulting two matrices

#### Below is my 9x9 matrix and the 3x3 matrices that act as a filter.

The matrix

```
[[-1, -1, 1, 1, -1, 2,-1, 1, -1],
[0, -1, -1, -1, -1, -2, 1, -1, -1], 
[1, 0, 0, -2, -1, 2, 0, -1, -1],
[-1, 0, 1, 0, -1, 2, -1, -1, 0],
[-1, 0, -1, 2, 0, 1, 0, 1, -1],
[0,1, -1, 2, -2,1, 1, 0, 0],
[1, -1, -1, -1, 0, 2, 0, -1, 1],
[-1, 0, -1, 0, 0, -1, -1, -1, 0],
[0, 0, 0, 2, 0, 1, 1, 1, 0]]
```

Filter 1

```
[[0,1,1],
[0,0,1],
[0,1,1]]
```

Filter 2

```
[[1,0,1],
[1,0,0],
[0,0,0]]
```

I convolved the 9x9 matrix programmatically, however, my code is not optimized. If I do this again I will look for a streamlined solution that avoids the use of while statements as they present a large risk of crashing my program.

```
img = np.array([[-1, -1, 1, 1, -1, 2,-1, 1, -1],
                [0, -1, -1, -1, -1, -2, 1, -1, -1], 
                [1, 0, 0, -2, -1, 2, 0, -1, -1],
               [-1, 0, 1, 0, -1, 2, -1, -1, 0],
               [-1, 0, -1, 2, 0, 1, 0, 1, -1],
               [0,1, -1, 2, -2,1, 1, 0, 0],
               [1, -1, -1, -1, 0, 2, 0, -1, 1],
               [-1, 0, -1, 0, 0, -1, -1, -1, 0],
               [0, 0, 0, 2, 0, 1, 1, 1, 0]])
               
#ker = np.array([[0,1,1],[0,0,1],[0,1,1]])

ker = np.array([[1,0,1],[1,0,0],[0,0,0]])

output = np.zeros((7, 7))

a= 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
while a != 7:
    output[0,a] = np.sum(ker*img[0:3,a:a+3])
    a=a+1
while b != 7:
    output[1,b] = np.sum(ker*img[1:4,b:b+3])
    b=b+1
while c != 7:
    output[2,c] = np.sum(ker*img[2:5,c:c+3])
    c=c+1
while d != 7:
    output[3,d] = np.sum(ker*img[3:6,d:d+3])
    d=d+1
while e != 7:
    output[4,e] = np.sum(ker*img[4:7,e:e+3])
    e=e+1
while f != 7:
    output[5,f] = np.sum(ker*img[5:8,f:f+3])
    f=f+1
while g != 7:
    output[6,g] = np.sum(ker*img[6:9,g:g+3])
    g=g+1
```

The resulting 7x7 matrix for my first filter:
```
[[-1., -1., -4.,  0.,  4., -2., -3.],
[-1., -3., -4.,  0.,  0., -3., -4.],
[ 0., -1., -2.,  4.,  2., -1., -2.],
[ 0.,  4., -1.,  1.,  3.,  0., -2.],
[-4.,  1., -1.,  4.,  4.,  0.,  0.],
[-2., -1.,  0.,  0.,  0., -2.,  0.],
[-3.,  0.,  1.,  2.,  3.,  0.,  1.]]
```

The resulting 7x7 matrix for my second filter:

```
[[ 0., -1., -1.,  2., -3.,  1., -1.],
[ 0., -2., -2., -5., -1., -1.,  0.],
[ 0., -2.,  0.,  0., -2.,  3., -2.],
[-1.,  0., -1.,  4., -2.,  2., -1.],
[-2.,  3., -2.,  5., -2.,  3.,  0.],
[ 0.,  2., -4.,  2., -1.,  3.,  1.],
[-1., -2., -2.,  1.,  0.,  0.,  0.]]

```

#### Question 2: What is the purpose of using a 3x3 filter to convolve across a 2D image matrix?

The purpose of the filter seems to be to be extract certain filters from the image. It would seem that using a larger filter, such as a 3x3 filter as opposed to a 2x2 filter, would be able to capture and thus emphasize larger features that a smaller filter would not be able to capture. However, increasing the size of the filter also increases the computational cost. 

#### Question 3: Why would we include more than one filter? How many filters did you assign as part of your architecture when training a model to learn images of numbers from the mnist dataset?

It may be useful to include different filters to capture different filters. I could see a scenario where we would want to feed in the same image, but with different filters, into a nueral network in order for it to hone in on the different features emphasized by each filter, thus eliminating some of the noise in the image.

As for the the number mnist dataset, I only used one filter. However, my model may have been more accurate if I included more. 

## Part 2: From your 400+ observations of homes for sale, calculate the MSE for the following:
#### Question 1: The 10 biggest over-predictions
The Mean Squared Error is:  313645.45102606097

#### Question 2: The 10 biggest under-predictions
The Mean Squared Error is:  10350939.37663024

#### Question 3: The 10 most accurate results (use absolute value)
The Mean Squared Error is:  90.38137097992004

#### Question 4 In which percentile do the 10 most accurate predictions reside? Did your model trend towards over or under predicting home values?
The most accurate predictions reside between the 36th percentile and the 76th percentile. This seems to indicate the my model tends to under predict home values as a greater porportion of houses below the 50th percentile are outside of the range created by the 10 most accurate predictions than those above the 50th prediction. Additionally, the 10 biggest under-predictions had a larger MSE than the top 10 biggest over-predicitons. This most likely indicates that my model has trouble predicting the prices of houses in the bottom of the price range. 

#### Question 5: Which feature appears to be the most significant predictor in the above cases?
The most significant predictor in the above cases seems to be the number of bedrooms. In the top 10 underpredictions, hosues had fewer bedrooms than usual for that price range and for the top 10 overpredictions the opposite was true: there were more bedrooms than usual for the low price range. Moreover, the most accurate results tended to have less square footage which most likely increased the importance of the number of bedrooms on price this in turn would make sense if the model used bedrooms as the most important variable.

Code for the MSE section:

[Exercise_4_Final.py](https://github.com/jdatagi/Data_310/blob/gh-pages/Exercise_4_Final.py)



    
