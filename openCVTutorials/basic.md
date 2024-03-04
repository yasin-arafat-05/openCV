 
### - openCV Tutorial in Hindi:

[playlistLink](https://www.youtube.com/watch?v=0XD-N9-rzSI&list=PLTXuqKbKkxkTy764PhX1yil5hj-5va099&ab_channel=Aryanverma)


# -------------------------------------------01-------------------------------------------------

# Lecture-01:
- #### Introduction of the course:
<br><br><br>

# -------------------------------------------02-------------------------------------------------

# Lecture-02:
-   #### AI vs DL vs ML vs Computer-Vision:
-   `****`
<br><br><br>

# -------------------------------------------03-------------------------------------------------

# Lecture-03:
- ### What is openCV?

`openCV is a Open source programming library with real-time compouter vision capabilities.`

- ### BSD(Liscence) 
**Liscence**: Here we will know how openCV  change, redistribute and uses.
**It is free for both academic and commercial use**

- ### Modules of openCV
    - **Core:** This module is used for: basic core functions, Data structures, functionality to other moudules. **(Core Operation:)** addition, multiplication, subtraction etc. এই core operation গুলো অন্য moudles গুলোকে functionality provide করে বড় বড় task perform করার জন্য । `We already know that image is noting but the represtion of matrix form.`

    - **ImgProc:** Imgproc -> Image processing module. This module is used for color spaces, geometrical transforms, histograms, image filtering etc.

    - **DNN:** Deep Neural Network.

    - **ML:** Machine Learning uses: Regression task, Clustering tasks in images, anomaly detection and classicifation task.

    - **Video:** USED FOR, Video analysis including background subtraction, motion estimation and object-tracking algorithrms.

    - **highgui:** A high level UI module use for, Create and manipulate windows that can display images. Add trackbars to the windows, keyboard commands and handle mouse eveents.

    - **flann:** This moduleis used for 2D features framework. Thisi module includes feature detectors, descriptors and descriptor matchers.
    
    - photo
    - stiching
    - shape 
    - superres
    - videostab
    - viz
    - imgcodes
    - objdetect
    - features2d
    - calib3d
<br><br><br>


# -------------------------------------------04-------------------------------------------------
# Lecture-04:
### **Application:**
![photoOne](/openCVTutorials/photo/photoOne.jpeg)
![photoTwo](/openCVTutorials/photo/photoTwo.jpeg)
![photoThree](/openCVTutorials/photo/photoThree.jpeg)
<br><br><br>


# -------------------------------------------05-------------------------------------------------
# Lecture-05:
### **Image:**
![photoFour](/openCVTutorials/photo/photoFour.jpeg)
![photoFive](/openCVTutorials/photo/photoFive.jpeg)
<br><br><br>


# -------------------------------------------06-------------------------------------------------
# Lecture-06:
### **Color Spaces:**
![photoSix](/openCVTutorials/photo/photoSix.jpeg)
<br><br><br>


# -------------------------------------------07-------------------------------------------------

# Lecture-07:
### Numpy-1
<br><br><br>


# -------------------------------------------08-------------------------------------------------
# Lecture-08:
### Numpy-2
<br><br><br>

# -------------------------------------------09-------------------------------------------------
# Lecture-09:
### **Virtual Environment:**
`A Python virtual environment (venv) is simply a directory with a particular file structure.`
<br>
ধরি, আমি কোন প্রজেক্ট করবো সেখানে, একজায়গায় আমার python_openCV এর  4.8.0 আর অন্য project এ 4.9.1 লাগবে । 
এই ক্ষেত্রে আমাদের দুটি প্রজেক্টের dependency আলাদা আলাদা তাই  এক্ষেত্রে আমাদের virtual environment create করে কাজ করতে হবে । 
<br>

### **sys.argv[]:**
`SYS: System-specific parameters and functions.`
python test.py (parameter) যা ইচ্ছে তাই দিব এইগুলো argv[] এই  লিস্ট এর মধ্যে জমা হবে ।  
যেমনঃ এই খানে, শুরুতে filename then parameter গুলো সেভ হবে । 

### **Deactivate: venv**
`deactivate`
<br><br><br>

# -------------------------------------------10-------------------------------------------------
# Lecture-10:
`Image and video read Write`
<br><br><br>

# -------------------------------------------11-------------------------------------------------
# Lecture-11:
`Project: reverse a video.`
<br><br><br>

# -------------------------------------------12-------------------------------------------------
# Lecture-12:
`Work with shpae like: Lines, Shapes, Polygons, Text etc.`

### **Aliasing and Anti-aliasing:**
Aliasing and anti-aliasing are concepts related to image processing and computer graphics, particularly when dealing with digital images. They describe phenomena associated with the representation and processing of visual information.<br>
![Alt text](/openCVTutorials/photo/image12.png)
<br>

### **Aliasing:**
Aliasing occurs when there is an insufficient sampling rate to accurately represent a signal (such as an image or waveform)

### Anti-aliasing:**
Anti-aliasing is a technique used to reduce or eliminate aliasing artifacts in digital images. It involves applying various methods to smooth out jagged edges and reduce the visual impact of aliasing.
<br><br><br>

#### In openCV in line() function we have three line type: <br> i) line_4  <br> ii) line_8  <br> iii) line_AA
<br>

![Alt text](/openCVTutorials/photo/image13.png)

<br>

`line_4 and line_8 is aliasing.` <br>
`line_AA is anti-aliasing.` <br>
<br>

# -------------------------------------------13-------------------------------------------------
# Lecture-13:
`project: analog clock with openCV`

<br><br><br>



# -------------------------------------------14-------------------------------------------------


# Lecture-14:
### Rotation:
**Definition:** Rotation involves turning an object or image around a fixed point, known as the center of rotation. <br>
**Effect:** The image or object is rotated by a specified angle around the rotation center. <br>
**Mathematical Prove:**
Certainly! Let's derive the equations for a counterclockwise rotation in two dimensions using markdown language.<br>

### Roation করার জন্য আমাদের rotation matrix লাগবে যেইটা openCV তে implemented আছে । 
## Derivation of 2D Rotation Equations:
<br>

In the xy system, a point P is represented by polar coordinates $\((r, \alpha)\)$. In the x'y' system, after a counterclockwise rotation by an angle $\(\theta\)$, the polar coordinates become 
$\((r, \alpha - \theta)\)$.

Using trigonometric functions, the coordinates in the xy system are:

$\[
x = r \cos \alpha \quad (1)
\]$

$\[
y = r \sin \alpha \quad (2)
\]$

Now, applying trigonometric identities for differences, the coordinates in the x'y' system are:

$\[
x' = r \cos(\alpha - \theta) = r \cos \alpha \cos \theta + r \sin \alpha \sin \theta \quad (3)
\]$

$\[
y' = r \sin(\alpha - \theta) = r \sin \alpha \cos \theta - r \cos \alpha \sin \theta \quad (4)
\]$

Substituting equations (1) and (2) into equations (3) and (4), we get:

$\[
x' = x \cos \theta + y \sin \theta \quad (5)
\]$

$\[
y' = -x \sin \theta + y \cos \theta \quad (6)
\]$

These equations can be represented in matrix form as:

This matrix equation represents the standard form of a 2D rotation transformation.
![Alt text](/openCVTutorials/photo/image.png)

<br><br>

The inverse transformation is given by:

$\[
x = x' \cos \theta - y' \sin \theta \quad (8)
\]$

$\[
y = x' \sin \theta + y' \cos \theta \quad (9)
\]$

<br><br>

In matrix form:

![Alt text](/openCVTutorials/photo/image1.png)

These equations describe the transformation and its inverse in a 2D space after a counterclockwise rotation by an angle $\(\theta\)$.

### proof: 
<br> <br>
![Alt text](/openCVTutorials/photo/image3.png)
<br><br>
Clock wize হলে angle phi এর সামনে negative বসাবো । 
<br><br>
<br><br>

# Scaling: 

<br> <br>

### Fast we will know about zooming:

- **Optical Zooming:** An Optical zoom means moving the zoom lens so that it increases the magnification of light before it even reaches the digital sensor. <br>

- **Digital Zooming:** A digital zoom is not really zoom, it is simply **interpolating** the image after it has been acquired at the sensor(pixilation process). <br>
<br><br>

## **Scaling:**
In OpenCV, scaling refers to the process of resizing an image, changing its dimensions while preserving its aspect ratio or adjusting the aspect ratio if necessary. <br>
`aspect ratio = Width/Height.`
<br>

### Process :
- Increasing or decreasing the pixels in digital image
- We have an image and we Increase it (180%) 
- then we resampling the image(**before interpolation picture:**  <br>
আমরা যখন image এর height and width বাড়াবো তখন, pixel এর মধ্যেও  জায়গা  )
- then we assign new grayvalues(By the help of `Interpolation.`)
![Alt text](/openCVTutorials/photo/image4.png)

# `Interpolation: `
Interpolation is the process of estimating the values of a continous function from discreate samples. (আমরা জানি, image একটা function আর interpolation এর ক্ষেত্রে আমদের দুইটা পাশাপাশি pixel এর value দেওয়া আছে। কিন্তু আমাদের যেহেতু মাঝে space আসতেছে তাইলে এই space  এর মান বের করবো কিভাবে ?)
image function তাই, আমাদের যেহেতু দুইটা pixel এর মান জানা আছে তাই মাঝখানে কোন value তা বসতে পারে তা estimate করতে পারবো । 
<br>

**Each pixel in the image is represented by a vector v ∈ V indicating the location of that pixel, and it is paired with c ∈ C, which indicates the color of that pixel**
<br><br>

### openCV Give us 5 types of interpolation: 

- **Linear interpolation:**
- **Area**
- **Cuvic**
- **Nearest Neighbor Interpolation**
- **Sinusoidal Interpolation**

`Example of linear interpolation: `
<br>

![Alt text](/openCVTutorials/photo/image5.png)

## Scaling matrix: 
![Alt text](/openCVTutorials/photo/image8.png)

<br><br>

# **Image Translation:**
<br>

Shift an image in coordinate space by adding a specified value to the x and y coordinate.

![Alt text](/openCVTutorials/photo/image6.png)

![Alt text](/openCVTutorials/photo/image7.png)

<br><br><br>


# -------------------------------------------15-------------------------------------------------

# Lecture-15:
<br><br><br>



# -------------------------------------------16-------------------------------------------------

# Lecture-16:
# Convolutions and Filtering:
<br>

## `Convolution:`
In convolution, we basically apply a mathematical operator to each pixel and change its value in some way. To apply this mathematical operator, we use another matrix called a kernel.<br>
![Alt text](/openCVTutorials/photo/image9.png)

`Calculation:`
![Alt text](/openCVTutorials/photo/image10.png)

`কিন্তু আমরা যেহেতু, 3x3, 5x5 or oddxodd ব্যবহার করে  kernal এর middle point বরাবর output বসাচ্ছি, input এর শুরুতে যেইটা আছে সেইটা জন্য আমরা kearnal ব্যবহার করতে পারবো না । এর জন্য আমাদের padding with zero(i) এবং wrap around (ii). `


## `Frequency of a image: `<br>

Frequency refers to the rate of change of pixel values. So we can say that the sharp edges would be **high frequency** content because the pixel values change rapidly in that region. Going by that logic, plain areas would be **low frequency** content.
<br><br>

`(যেমনঃ আমার  মাথার চুল আর মুখ যেইখানে মিলিত হয়েছে যেখানে(rate of change of pixel value বেশি) । কিন্তু যেইখানে শুধু চুল আর চুল সেইখানে (rate of change of pixel value কম ।)llow frequency reagion )।` 
<br><br>

**Low pass filter:** Low pass filter is the type of frequency domain filter that attenuates the high frequency components and preserves the low frequency components.<br>

**Low pass Filters:**
- It is used for smoothing the image.
- It attenuates the high frequency.
- It allows the frequency below cut off frequency to pass through it
- It consists of resistor that is follwed by capacitor.
- It helps in removal of aliasing effect.
<br>
<br>

**High pass filter:** High pass filter is the type of frequency domain filter that attenuates the low frequency components and preserves the high frequency components.<br>

**High pass Filters:**
- It is used for sharpening the image.
- It attenuates the low frequency.
- High frequency is preserved in it.
- It allows the frequencies above cut off frequency to pass through it.
- It consists of capacitor that is follwed by a resistor.
- It helps in removal of noise.
<br>

# Applying Custom Filters to Image:
### Ex- Blurring an Image:

![Alt text](/openCVTutorials/photo/image11.png)

<br>
**Function Used:**
output = cv2.filter2D(src,depth,kernel,anchor,border_type) <br>

**Color depth in lecture: 06 -> No. of bits used to indicate teh color of a single image. Total depth = 3*8 = 24 bits.**
**kernal: -> matrix we see in Convolution** <br>
**anchor:** In the cv2.filter2D() function in OpenCV, the anchor parameter represents the relative position of the anchor point within the kernel. The anchor point is the pixel in the kernel to which the convolution operation is applied to calculate the new value of the central pixel in the output image.<br>
**border_type:** we see the padding with zero and wrap around. And there are few more in openCV.
<br><br><br>


# -------------------------------------------17-------------------------------------------------

# Lecture-17:
<br><br><br>



# -------------------------------------------18-------------------------------------------------

# Lecture-18:
#  openCV Project: PHOTO to WATER COLOR ART
<br><br><br>


