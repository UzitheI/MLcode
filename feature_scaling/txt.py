# suppose the price can be determined by the formula 
# price=w1x1+ w2x2+ b

# x1 represents the size in feet2 and x2 represents bedrooms and finally b is the base price 

# now, we can correctly determine the value of w1 and w2 to be closest to the actual value to get correct values, it is called feature scaling when we increase the values of w1 and w2  so as to reach the local minima much more faster 



# here the proper feature should be 
# w1=0.1, w2=50, b=50 in order to get the price of 500k 


# how to implement feature scaling 

# suppose our x1 runs from 300<=x1<=2000, now we can divide every value of x1 by 2000 to get the range from 0.15 to 1 which is scaling 

# there are multiple ways of feature scaling, one of them is 

# mean normalization 

# where we take the mean of x1 and x2 and use the formula 

# let u be the mean and we use 

# x1'=x1-u1/l1-s1
# where l1 and s1 are the largest and smallest value respectively 

# if you plot the value from the mean normalization we might get a more circular plot ranging only within -1 and 1 which makes it possible to get to local minima much more faster


# another re-scaling method is 

# z-score normalization 

# we need to find the standard deviation for this 

# we calculate the mean and S.D and then use the formula for every x1 

# x1=x1-u1/sd1, this is z score normalization 
# which might make the range 
# -0.67<=x1<=3.1 
# looking at the plot 
# this makes it 


# difference betweeen z-score normalization and normalization 

# z-score normalization is also called standardization and it doesnt have a particular range normalization is ranged from 0 to 1 or -1 to 1


# normalization is more useful when feature distribution is unclear and z-score distribution is consistent 


# z-score normalization makes it easier for computers to communicate with each other 


# the normalization process involves scaling using largest and smallest value and the z-score normalization involves the use of mean and standard deviaton 

# with feature scaling we have to aim for -1<=x1<=1 which also means that we can have comparable largest and smallest value 

# something like -100<=x3<=100 needs to be rescaled because it is too large 

# also something like -0.0001<=x4<=0.001 needs to rescaled because it is too small 




