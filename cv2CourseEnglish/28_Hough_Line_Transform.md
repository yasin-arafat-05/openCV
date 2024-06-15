
# Lecture 28: `Hough Line Transform`

Hough Transform is a popular technique to detect any shape if you can represent that shape in a mathematical form Hough transform can detect the shape even if it is broken or distorted a little bit.


![Alt text](image-6.png)

`You have an image of a road and you want to detect these lane lines in this road image so the first step in order to detect these Lane lines in this road is to find the edge pixels using canny edge detection or any other edge detection method now after you found out the edges using any edge detection method you want a geometrical representation of that edge and in order to find out the geometrical representation for example you want to find out the slope of this edge or its intercept you can use half transform to represent these pixels or edges in the mathematical or geometrical form so after you find out the edges using any edge detector you just have the sequence of pixels so you can loop through all the pixels and somehow figure out the slope and intercepts but it's a very difficult task so we want some mechanism that gives more weight age to pixels that are already in line and this is what we can achieve using Hough transform.`

<br>

# Basic of Hough Line Transform:

A line can be represented by two equation i) Cartesian and ii) Polar . 

![Alt text](image-5.png)


In, cartesian we can represented the line in `xy space` and `mc space` 

![Alt text](image-7.png)

If we have two point in `xy space, Xa and Ya` then the equation of the line in `mc space` given below,

![Alt text](image-8.png)

If we have sevral point of a line in `xy space` then in `mc space` the m and c is same for all but the line is different.

![Alt text](image-9.png)


In polar codinate system:

![Alt text](image-10.png)

Given, a point in `xy space` (8,6)  then the line represtation in  `r theta space`(Hough transform in the parameter space (often referred to as Hough space or r,θ space))  is:

![Alt text](image-11.png)


for multiple lines:

![Alt text](image-12.png)

And in the `r theta sapce ` the intercept represent a line in hough space.

<br>

# Algorithrm of hough line transformation 

![Alt text](image-13.png)

<br>

`OpenCV implements two kind of half line transforms the first is the standard Hough transform which is done using HalfLines method the second type is the probabilistic half line transform which is done by HalfLinesP method. `

![Alt text](image-14.png)

<br>


# More about hough line transform:

In the context of the Hough transform, particularly for detecting lines in an image, the "r theta space" refers to the parameter space used in the Hough line transformation. Here's a breakdown:

1. **Hough Transform Basics**: 
   - The Hough transform is a technique used in image processing and computer vision to detect simple geometric shapes, such as lines or circles, within an image.

2. **Parameter Space**:
   - For detecting lines, the Hough transform uses a parameterization of lines in the form of $\( r, \theta \)$, where:
     - $\( r \)$ is the distance from the origin to the closest point on the line.
     - $\( \theta \)$ is the angle between the x-axis and the normal line connecting the origin to this closest point.

3. **r theta Space**:
   - The term "r theta space" (or $\( r, \theta \)$ space) specifically refers to the parameter space in which the Hough transform represents lines. 
   - In this space, each point corresponds to a line in the original image. The Hough transform accumulates votes in this parameter space for each point that could lie on a line.

4. **Accumulator Array**:
   - To implement the Hough transform, typically an accumulator array (or Hough accumulator) is used, where each cell corresponds to a possible line in the image. The accumulator cells are incremented based on detected edge points that might lie on these lines.

5. **Peak Detection**:
   - After accumulating votes, peaks in the accumulator array indicate the parameters $\( r \)$ and $\( \theta \)$ of the lines present in the image. These peaks correspond to the lines detected by the Hough transform.

Therefore, "r theta space" is essentially the Hough space or parameter space where the Hough transform operates to detect lines based on their $\( r \)$ (distance) and $\( \theta \)$ (angle) parameters. This space is crucial in understanding and implementing the Hough transform for line detection in images.

