## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

The risk of filtering these values out is that it might make our information inaccurate because we're removing any potential chances of human error that comes with calculating our heart rate data, which can be thought of as potential outliers.

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

In the context of heart rate, standard deviation describes the average amount in which individual heartbeats differentiate or deviate from the average heart rate

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

The times I notice a significant difference in values along the x-axis are minutes(and/or hours), 10, 20, and 30. As it shoots up from a heart rate of min/hour 10(57 HR) to min/hour 20(97 HR) back to mi/hourn (30 HR)

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

I do notice a difference in values in the standard deviation graph as it seems somewhat flipped compared to the averages graph, as where the averages graph had dips, the standard deviation graph peaked. I thought this was describing the sharp deviations by showing that the values were peaking, but the values were too small compared to the value of the averages
