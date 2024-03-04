 
### - openCV Tutorial in Hindi:

[playlistLink](https://www.youtube.com/watch?v=0XD-N9-rzSI&list=PLTXuqKbKkxkTy764PhX1yil5hj-5va099&ab_channel=Aryanverma)


# Lecture-01:
- #### Introduction of the course:

# Lecture-02:
-   #### AI vs DL vs ML vs Computer-Vision:
-   `****`

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
<br><br>

# Lecture-04:
### **Application:**
![photoOne](/openCVTutorials/photo/photoOne.jpeg)
![photoTwo](/openCVTutorials/photo/photoTwo.jpeg)
![photoThree](/openCVTutorials/photo/photoThree.jpeg)
<br><br>

# Lecture-05:
### **Image:**
![photoFour](/openCVTutorials/photo/photoFour.jpeg)
![photoFive](/openCVTutorials/photo/photoFive.jpeg)
<br><br>

# Lecture-06:
### **Color Spaces:**
![photoSix](/openCVTutorials/photo/photoSix.jpeg)
<br><br>

# Lecture-07:
### Numpy-1
<br><br>

# Lecture-08:
### Numpy-2
<br><br>

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

# Lecture-10:
# Lecture-11:
# Lecture-12:
# Lecture-13:

# Lecture-14:
### Rotation:
**Definition:** Rotation involves turning an object or image around a fixed point, known as the center of rotation. <br>
**Effect:** The image or object is rotated by a specified angle around the rotation center. <br>
**Mathematical Prove:**
Certainly! Let's derive the equations for a counterclockwise rotation in two dimensions using markdown language.<br>

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

<br><br>

# Lecture-15:
# Lecture-16:
# Lecture-17:
# Lecture-18:
# Lecture-19:
# Lecture-20:
