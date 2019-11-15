**Chapter 1: Abstract**

Road Detection From An Image Using Computer

Vision

**Abstract**

>   Given an image captured from a camera attached to a vehicle moving on a road
>   in which captured road may or may not be well levelled, or have clearly
>   delineated edges, or some prior known patterns on it, then road detection
>   from a single image can be applied to find the road in an image so that it
>   could be used as a part in automation of driving system in the vehicles for
>   moving the vehicle in correct road. In this process of finding the road in
>   the image captured by the vehicle, we can use some algorithms for vanishing
>   point detection using Hough transform space, finding the region of interest,
>   edge detection using canny edge detection algorithm and then road detection.
>   We use thousands of images of different roads to train our model so that the
>   model could detect the road which is present in the new image processed
>   through the vehicle.

Input to Project: Single image (may or may not) containing the road.

>   Output to Project: Single image (may or may not) containing the road
>   detected by computer.

**Sample Input:**

![](media/217bfc49a352a6ae67d530ff222a7b92.png)

**Figure 1.1:** Input of Image containing Road

**Sample Output:**

![](media/3195e4dfac7df4072ab097d8dbf17cd6.png)

**Figure 1.2:** Output of Image after processing.

>   **Chapter 2: Introduction to Self-Driving Cars and Automatic Road
>   Detection**

**2.1 Self-Driving Cars**

A self-driving car (sometimes called an autonomous car or driverless car) is a
vehicle that uses a combination of sensors, cameras, radar and artificial
intelligence (AI) to travel between destinations without a human operator. To
qualify as fully autonomous, a vehicle must be able to navigate without human
intervention to a predetermined destination over roads that have not been
adapted for its use.

Companies developing and/or testing autonomous cars include Audi, BMW, Ford,
Google, General Motors, Tesla, Volkswagen and Volvo. Google's test involved a
fleet of self-driving cars -- including Toyota Prii and an Audi TT -- navigating
over 140,000 miles of California streets and highways.

Levels of autonomy in self-driving cars

The U.S. National Highway Traffic Safety Administration (NHTSA) lays out six
levels of automation, beginning with zero, where humans do the driving, through
driver assistance technologies up to fully autonomous cars. Here are the five
levels that follow zero automation:

Level 1: Advanced driver assistance system (ADAS) aid the human driver with
either steering, braking or accelerating, though not simultaneously. ADAS
includes rear view cameras and features like a vibrating seat warning to alert
drivers when they drift out of the traveling lane.

Level 2: An ADAS that can steer and either brake or accelerate simultaneously
while the driver remains fully aware behind the wheel and continues to act as
the driver.

Level 3: An automated driving system (ADS) can perform all driving tasks under
certain circumstances, such as parking the car. In these circumstances, the
human driver must be ready to re-take control and is still required to be the
main driver of the vehicle.

Level 4: An ADS is able to perform all driving tasks and monitor the driving
environment in certain circumstances. In those circumstances, the ADS is
reliable enough that the human driver needn't pay attention.

Level 5: The vehicle's ADS acts as a virtual chauffeur and does all the driving
in all circumstances. The human occupants are passengers and are never expected
to drive the vehicle.

**2.2 Working of Self Driving Cars**

Lane lines are being drawn as the car drives. Also, you can see the radius of
curvature is being calculated to help the car steer. It is cheap to equip cars
with a front facing camera. Much cheaper than RADAR or LIDAR. Once we get a
camera image from the front facing camera of self-driving car, we make several
modifications to it. The steps I followed are detailed below:

1.  **Distortion correction**

    Image distortion occurs when a camera looks at 3D objects in the real world
    and transforms them into a 2D image. This transformation isn’t always
    perfect and distortion can result in a change in apparent size, shape or
    position of an object. So, we need to correct this distortion to give the
    camera an accurate view of the image. This is done by computing a camera
    calibration matrix by taking several chessboard pictures of a camera.

See example below of a distortion corrected image. Please note that the
correction is very small in normal lenses and the difference isn’t visible much
to the naked eye.

![](media/bde0831dd69bdec947ab49fdadc81edb.png)

>   **Figure 2:** Describing the original image and undistorted image

1.  **Create a binary image**

    Now that we have the undistorted image, we can start our analysis. We need
    to explore different schemes so that we can clearly detect the object of
    interest on the road, in this case lane lines while ignoring the rest. I did
    this in two ways:

-   **Using Sobel operator to compute x-gradient**

    The gradient of an image can be used to identify sharp changes in colour in
    a black and white image. It is a very useful technique to detect edges in an
    image. For the image of a road, we usually have a lane line in either yellow
    or white on a black road and so x-gradient can be very useful.

-   **Explore other colour channels**

    HSV (Hue, Saturation and Value) colour space can be very useful in isolating
    the yellow and line white lines because it isolates colour (hue), amount of
    colour (saturation) and brightness (value). We can use the S colour channel
    in the image.

-   **Birds Eye View Image**

    After the thresholding operation, we perform a perspective transform to
    change the image to bird’s eye view. This is done because from this top view
    we can identify the curvature of the lane and decide how to steer the car.
    To perform the perspective transform, I identified 4 source points that form
    a trapezoid on the image and 4 destination points such that lane lines are
    parallel to each other after the transformation. The destination points were
    chosen by trial and error but once chosen works well for all images and the
    video since the camera is mounted in a fixed position. OpenCV can be used to
    perform this. See how clearly the curvature of the lane lines is visible in
    this view.

-   **Fit curve lines to the bird eye view image**

    In order to better estimate where the lane is, we use a histogram of the
    bottom half of image to identify potential left and right lane markings.
    Modification of this function to narrow down the area in which left and
    right lanes can exist so that highway lane separators or any other noise
    doesn’t get identified as a lane. Once the initial left and right lane
    bottom points are identified.

-   Plot the result identified by the system clearly. This plotting can be done
    filling the space area with transparent colour using OpenCV.

Thus, Self-Driving car works and road detection can be useful in detection of
road from an image captured from car.

.

>   **Chapter 3: Canny Edge Detection**

**3.1 Introduction to Canny Edge Detection**

Edges characterize boundaries and are therefore a problem of fundamental
importance in image processing. Edges in images are areas with strong intensity
contrasts – a jump in intensity from one pixel to the next. Edge detecting an
image significantly reduces the amount of data and filters out useless
information, while preserving the important structural properties in an image.

Canny edge detection algorithm is also known as the optimal edge detector.
Cranny’s intentions were to enhance the many edge detectors in the image.

-   The first criterion should have low error rate and filter out unwanted
    information while the useful information preserve.

-   The second criterion is to keep the lower variation as possible between the
    original image and the processed image.

-   Third criterion removes multiple responses to an edge.

Based on these criteria, the canny edge detector first smoothens the image to
eliminate noise. It then finds the image gradient to highlight regions with high
spatial derivatives. The algorithm then tracks along these regions and
suppresses any pixel that is not at the maximum using non-maximum suppression.
The gradient array is now further reduced by hysteresis to remove streaking and
thinning the edges.

![](media/a33bf6bd117aaeb5606b90b848c665bf.png)

>   **Figure 3:** Describing the processes in Canny Edge Detection

**3.2 Filter out noise**

**3.2.1 Convolution**

First step to Canny edge detection require some method of filter out any noise
and still preserve the useful image. Convolution is a simple mathematic method
to many common image-processing operators.

![](media/946527acafd42b201dab3f8cdb4a1047.png)

>   **Figure 4:** An example small image (left), kernel (right)

**3.2.2 Convolution operation:**

Convolution is performed by sliding the kernel or mask over a grey-level image.
The kernel starts from the top left corner and moves through entire image within
image boundaries. Each kernel position corresponds to a single output pixel.
Each pixel is multiplied with the kernel cell value and added together. The
output image will have M-m+1 rows and N-n+1 column, M image rows and N image
columns, m kernel rows and n kernel columns.

The output image will be smaller when compared to the original image. This is
due to the bottom and right edge pixels, which can’t be completely mapped by the
kernel therefore m –1 right hand pixel and n-1 bottom pixels can’t be used.

**Step 1: Gaussian filtering to remove noise**

The first step of canny edge detection is to filter out any noise in the
original image before trying to locate and detect any edges. The Gaussian filter
is used to blur and remove unwanted detail and noise. By calculating a suitable
5 X 5 mask, the Gaussian smoothing can be performed using standard convolution
method. A convolution mask is much smaller than the actual image. As a result,
the mask is slid over the image, calculating every square of pixels at a time.

Gaussian filter uses 2D distribution to perform convolution. The larger the
width of the Gaussian mask, the lower is the detector's sensitivity to noise.
The weight of the matrix is concentrated at the center, therefore any noise
appearing in the outside columns and rows will be eliminated, as the weight
decreases outward from the center value. The localization error in the detected
edges also increases slightly as the Gaussian width is increased. The increasing
of standard deviation reduces or blurs the intensity of the noise.

![](media/820fb317d935a515187125f4616b6701.gif)

>   **Figure 4.1:** Gaussian filter in mathematical form

![](media/a3d09656f9ca81ee527dcff44fb101c7.jpg)

>   **Figure 5:** original image (top), Gaussian filtered image (bottom)

**Step 2: Sobel Operator**

After smoothing the image and eliminating the noise, the next step is to find
the edge strength by taking the gradient of the image. The Sobel operator
performs a 2-D spatial gradient measurement on an image.

Then, the approximate absolute gradient magnitude (edge strength) at each point
can be found by the formula below which is simpler to calculate compared to the
above exact gradient magnitude.

Approximate gradient magnitude given below:

$$
\left| G \right| = \left| G_{x} \right| + \left| G_{y} \right|
$$

The Sobel operator uses a pair of 3x3 convolution masks, one estimating the
gradient in the x-direction (columns) and the other estimating the gradient in
the y-direction (rows).

Sobel $$G_{x}$$ and $$G_{y}\$$masks shown below each one estimates gradient x
direction and y direction respectively:

![](media/0ae9012a36afd79924925b005430c6c3.png)

>   **Figure 6:** original image (left), with Sobel operation (right)

**Step 3: Finding Gradient angle**

Finding the edge direction is trivial once the gradient in the x and y
directions are known. However, you will generate an error whenever sum of
$$G_{x}$$ is equal to zero i.e. $$G_{x}$$ value in denominator meaning
calculating arctan of infinity. So, the edge direction will equal to 90 or 0
degrees depend on Gx value and 0 degrees depend on $$G_{y}$$ value.

The formula for finding the edge direction is given below:

$$
\theta = \operatorname{}\left( \frac{G_{y}}{G_{x}} \right)
$$

**Step 4: Tracing the edge in the image using** $$\mathbf{\theta}$$**(angle)**

Once the edge direction is known, the next step is to relate the edge direction
to a direction that can be traced in an image. So, if use the 5x5 matrix to
calculate the angle of the edge, the smaller the matrix the fewer angles would
have in the image.

| x | x | x | x | x |
|---|---|---|---|---|
| x | x | x | x | x |
| x | x | a | x | x |
| x | x | x | x | x |
| x | x | x | x | x |

By looking at the center pixel "**a**", there are four possible directions when
describing the surrounding pixels - **0 degrees** (in the horizontal direction),
**45 degrees** (along the positive diagonal), **90 degrees** (in the vertical
direction), or **135 degrees** (along the negative diagonal), **180 degrees**
region is just an mirror region of 0 degrees region. Therefore, any edge
direction calculated will be round up to the closest angle.

So, any edge direction falling within the **A and E** (0 to 22.5 & 157.5 to 180
degrees) is set to 0 degrees. Any edge direction falling in the **D** (22.5 to
67.5 degrees) is set to 45 degrees. Any edge direction falling in the **C**
(67.5 to 112.5 degrees) is set to 90 degrees. And finally, any edge direction
falling within the **B** (112.5 to 157.5 degrees) is set to 135 degrees.

![](media/a9d48ed4370e03721977a696507c091f.png)

**Figure 7**: Tracing the Edge of an Image

The bigger the matrix the greater number of angles one could get, which implies
the edge angle will be more precise i.e. will follow the edge better, but on the
down side it will be a bigger computation task as now the kernel/mask size is
bigger.

**Step 5: Non maximum Suppression**

After the edge directions are known, non-maximum suppression is applied. Non-
maximum suppression is used to trace along the gradient in the edge direction
and compare the value perpendicular to the gradient. Two perpendicular pixel
values are compared with the value in the edge direction. If their value is
lower than the pixel on the edge then they are suppressed i.e. their pixel value
is changed to 0, else the higher pixel value is set as the edge and the other
two suppressed with a pixel value of 0.

We wish to mark points along the curve where the magnitude is biggest. We can do
this by looking for a maximum along a slice normal to the curve (non-maximum
suppression). These points should form a curve. There are then two algorithmic
issues: at which point is the maximum, and where is the next one?

**Step 6: Hysteresis**

Finally, hysteresis is used as a means of eliminating streaking. Streaking is
the breaking up of an edge contour caused by the operator output fluctuating
above and below the threshold. If a single threshold, T1 is applied to an image,
and an edge has an average strength equal to T1, then due to noise, there will
be instances where the edge dips below the threshold. Equally it will also
extend above the threshold making an edge look like a dashed line. To avoid
this, hysteresis uses 2 thresholds, a high and a low. Any pixel in the image
that has a value greater than T1 is presumed to be an edge pixel, and is marked
as such immediately. Then, any pixels that are connected to this edge pixel and
that have a value greater than T2 are also selected as edge pixels. If you think
of following an edge, you need a gradient of T2 to start but you don't stop till
you hit a gradient below T1.

![](media/9a3ed1fade587d09c14394b23d37e50c.png)

**Figure 8**: showing Canny Edge Detection Process

![](media/a1ec7f28864f2df2fb98fdd8e62d0857.png)

**3.3 Sample Input and Output of Canny Edge Detection Algorithm:**

>   **Figure 9:** Describing the Input Image

![](media/b11c9f1b15bdeaf003093a3eb9a6f3d3.png)

**Figure 10**: describing the Output Image

>   **Chapter 4: HOUGH TRANSFORM SPACE**

The Hough transform is a feature extraction technique used in image analysis,
computer vision, and digital image processing The purpose of the technique is to
find imperfect instances of objects within a certain class of shapes by a voting
procedure. This voting procedure is carried out in a parameter space, from which
object candidates are obtained as local maxima in a so-called accumulator space
that is explicitly constructed by the algorithm for computing the Hough
transform.

The classical Hough transform was concerned with the identification of lines in
the image, but later the Hough transform has been extended to identifying
positions of arbitrary shapes, most commonly circles or ellipses. The Hough
transform as it is universally used today was invented by Richard Duda and Peter
Hart in 1972, who called it a "generalized Hough transform" after the related
1962 patent of Paul Hough. The transform was popularized in the computer
vision community by Dana H Ballard through a 1981 journal article titled
"Generalizing the Hough transform to detect arbitrary shapes"

**4.1 Theory**

In automated analysis of digital images, a sub problem often arises of detecting
simple shapes, such as straight lines, circles or ellipses. In many cases
an edge detector can be used as a pre-processing stage to obtain image points or
image pixels that are on the desired curve in the image space. Due to
imperfections in either the image data or the edge detector, however, there may
be missing points or pixels on the desired curves as well as spatial deviations
between the ideal line/circle/ellipse and the noisy edge points as they are
obtained from the edge detector. For. The purpose of the Hough transform is to
address this problem by making it possible to perform groupings of edge points
into object candidates by performing an explicit voting procedure over a set of
parameterized image objects (Shapiro and Stockman, 304). The simplest case of
Hough transform is detecting straight lines. In general, the
straight-line *y = mx + b* can be represented as a point (*b*, *m*) in the
parameter space. However, vertical lines pose a problem. They would give rise to
unbounded values of the slope parameter *m*. Thus, for computational reasons,
Duda and Hart proposed the use of the Hesse normal form. These reasons, it is
often non-trivial to group the extracted edge features to an appropriate set of
lines, circles or ellipses.

![](media/f26491b0e416c0e402b0379040eda67b.gif)

>   **Figure 11**: Describing the Straight line represented in Hesse Normal Form

>   It is therefore possible to associate with each line of the image a
>   pair {\\displaystyle (r,\\theta )}(r, *θ*). The {\\displaystyle (r,\\theta
>   )}(r, theta) plane is sometimes referred to as *Hough space* for the set of
>   straight lines in two dimensions. This representation makes the Hough
>   transform conceptually very close to the two-dimensional Radon transform.
>   (They can be seen as different ways of looking at the same transform)

>   Given a *single point* in the plane, then the set of *all* straight lines
>   going through that point corresponds to a sinusoidal curve in the (*r, θ*)
>   plane, which is unique to that point. A set of two or more points that form
>   a straight line will produce sinusoids which cross at the (*r, θ*) for that
>   line. Thus, the problem of detecting collinear points can be converted to
>   the problem of finding concurrent curves.

**4.2 Implementation**

The linear Hough transform algorithm uses a two-dimensional array, called an
accumulator, to detect the existence of a line described by {\\displaystyle
r=x\\cos \\theta +y\\sin \\theta }r=x cos theta+ y sin theta. The dimension of
the accumulator equals the number of unknown parameters, i.e., two, considering
quantized values of r and θ in the pair (r, θ). For each pixel at *(x, y)* and
its neighborhood, the Hough transform algorithm determines if there is enough
evidence of a straight line at that pixel. If so, it will calculate the
parameters (r, θ) of that line, and then look for the accumulator's bin that the
parameters fall into, and increment the value of that bin. By finding the bins
with the highest values, typically by looking for local maxima in the
accumulator space, the most likely lines can be extracted, and their
(approximate) geometric definitions read off. (Shapiro and Stockman, 304) The
simplest way of finding these *peaks* is by applying some form of threshold, but
other techniques may yield better results in different circumstances –
determining which lines are found as well as how many. Since the lines returned
do not contain any length information, it is often necessary, in the next step,
to find which parts of the image match up with which lines. Moreover, due to
imperfection errors in the edge detection step, there will usually be errors in
the accumulator space, which may make it non-trivial to find the appropriate
peaks, and thus the appropriate lines.

The final result of the linear Hough transform is a two-dimensional array
(matrix) similar to the accumulator—one dimension of this matrix is the
quantized angle θ and the other dimension is the quantized distance r. Each
element of the matrix has a value equal to the sum of the points or pixels that
are positioned on the line represented by quantized parameters (r, θ). So, the
element with the highest value indicates the straight line that is most
represented in the input image.

**4.3 Variations and Extensions**

### 4.3.1 Using the gradient direction to reduce the number of votes

An improvement suggested by O'Gorman and Clowes can be used to detect lines if
one takes into account that the local gradient of the image intensity will
necessarily be orthogonal to the edge. Since edge detection generally involves
computing the intensity gradient magnitude, the gradient direction is often
found as a side effect. If a given point of coordinates (*x, y*) happens to
indeed be on a line, then the local direction of the gradient gives
the *θ* parameter corresponding to said line, and the *r* parameter is then
immediately obtained. (Shapiro and Stockman, 305) The gradient direction can be
estimated to within 20°, which shortens the sinusoid trace from the full 180° to
roughly 45°. This reduces the computation time and has the interesting effect of
reducing the number of useless votes, thus enhancing the visibility of the
spikes corresponding to real lines in the image.

### 4.3.2 Kernel-based Hough transform (KHT)

Fernandes and Oliveira suggested an improved voting scheme for the Hough
transform that allows a software implementation to achieve real-time performance
even on relatively large images (e.g., 1280×960). The Kernel-based Hough
transform uses the same {\\displaystyle (r,\\theta )}(r, theta) parameterization
proposed by Duda and Hart but operates on clusters of approximately collinear
pixels. For each cluster, votes are cast using an oriented elliptical-Gaussian
kernel that models the uncertainty associated with the best-fitting line with
respect to the corresponding cluster. The approach not only significantly
improves the performance of the voting scheme, but also produces a much cleaner
accumulator and makes the transform more robust to the detection of spurious
lines.

### 4.3.3 3-D Kernel-based Hough transform for plane detection (3DKHT)

Limberger and Oliveira suggested a deterministic technique for plane detection
in unorganized point clouds whose cost is {\\displaystyle n\\log(n)}nlogn in the
number of samples, achieving real-time performance for relatively large datasets
(up to {\\displaystyle 10\^{5}}105 points on a 3.4 GHz CPU). It is based on a
fast Hough-transform voting strategy for planar regions, inspired by the
Kernel-based Hough transform (KHT). This 3D Kernel-based Hough transform (3DKHT)
uses a fast and robust algorithm to segment clusters of approximately co-planar
samples, and casts votes for individual clusters (instead of for individual
samples) on a ({\\displaystyle \\theta ,\\phi ,\\rho }theta, sigma, row)
spherical accumulator using a trivariate Gaussian kernel. The approach is
several orders of magnitude faster than existing (non-deterministic) techniques
for plane detection in point clouds, such as RHT and RANSAC, and scales better
with the size of the datasets. It can be used with any application that requires
fast detection of planar features on large datasets.

### 4.4 Hough transform of curves, and its generalization for analytical and non-analytical shapes

Although the version of the transform described above applies only to finding
straight lines, a similar transform can be used for finding any shape which can
be represented by a set of parameters. A circle, for instance, can be
transformed into a set of three parameters, representing its center and radius,
so that the Hough space becomes three dimensional. Arbitrary ellipses and curves
can also be found this way, as can any shape easily expressed as a set of
parameters.

The generalization of the Hough transform for detecting analytical shapes in
spaces having any dimensionality was proposed by Fernandes and
Oliveira.[[11]](https://en.wikipedia.org/wiki/Hough_transform#cite_note-11) In
contrast to other Hough transform-based approaches for analytical shapes,
Fernandes' technique does not depend on the shape one wants to detect nor on the
input data type. The detection can be driven to a type of analytical shape by
changing the assumed model of geometry where data have been encoded
(e.g., Euclidean space, projective space, conformal geometry, and so on), while
the proposed formulation remains unchanged. Also, it guarantees that the
intended shapes are represented with the smallest possible number of parameters,
and it allows the concurrent detection of different kinds of shapes that best
fit an input set of entries with different dimensionalities and different
geometric definitions (e.g., the concurrent detection of planes and spheres that
best fit a set of points, straight lines and circles).

For more complicated shapes in the plane (i.e., shapes that cannot be
represented analytically in some 2D space), the Generalized Hough transform is
used, which allows a feature to vote for a particular position, orientation
and/or scaling of the shape using a predefined look-up table.

### 4.5 Circle detection process

Altering the algorithm to detect circular shapes instead of lines is relatively
straightforward.

-   First, we create the accumulator space, which is made up of a cell for each
    pixel. Initially each cell is set to 0.

-   For each edge point (i, j) in the image, increment all cells which according
    to the equation of a circle {\\displaystyle
    (i-a)\^{2}+(j-b)\^{2}=r\^{2}}((i-a)2+(j-b)2=r2) could be the centre of a
    circle. These cells are represented by the letter {\\displaystyle a}*a* in
    the equation.

-   For each possible value of {\\displaystyle a}*a* found in the previous step,
    find all possible values of {\\displaystyle b}*b* which satisfy the
    equation.

-   Search for local maxima in the accumulator space. These cells represent
    circles that were detected by the algorithm.

If we do not know the radius of the circle we are trying to locate beforehand,
we can use a three-dimensional accumulator space to search for circles with an
arbitrary radius. Naturally, this is more computationally expensive.

Y circle's area is still present within it.

### 4.6 Detection of 3D objects (Planes and cylinders)

Hough transform can also be used for the detection of 3D objects in range data
or 3D point clouds. The extension of classical Hough transform for plane
detection is quite straightforward. A plane is represented by its explicit
equation {\\displaystyle z=a_{x}x+a_{y}y+d}z=axx+ayy+d for which we can use a 3D
Hough space corresponding to {\\displaystyle a_{x}}ax, {\\displaystyle
a_{y}}ay and {\\displaystyle d}d. This extension suffers from the same problems
as its 2D counterpart i.e., near horizontal planes can be reliably detected,
while the performance deteriorates as planar direction becomes vertical (big
values of {\\displaystyle a_{x}}ax and {\\displaystyle a_{y}}ay amplify the
noise in the data). This formulation of the plane has been used for the
detection of planes in the point clouds acquired from airborne laser
scanning [[13]](https://en.wikipedia.org/wiki/Hough_transform#cite_note-13) and
works very well because in that domain all planes are nearly horizontal.

For generalized plane detection using Hough transform, the plane can be
parametrized by its normal vector {\\displaystyle n}n (using spherical
coordinates) and its distance from the origin {\\displaystyle \\rho
}row resulting in a three dimensional Hough space. This results in each point in
the input data voting for a sinusoidal surface in the Hough space. The
intersection of these sinusoidal surfaces indicates presence of a plane. A more
general approach for more than 3 dimensions requires search heuristics to remain
feasible.

Hough transform has also been used to find cylindrical objects in point
clouds using a two-step approach. The first step finds the orientation of the
cylinder and the second step finds the position and radius.

### 4.7 Using weighted features

One common variation detail. That is, finding the bins with the highest count in
one stage can be used to constrain the range of values searched in the next.

**4.7.1 Carefully chosen parameter space**

A high-dimensional parameter space for the Hough transform is not only slow, but
if implemented without forethought can easily overrun the available memory. Even
if the programming environment allows the allocation of an array larger than the
available memory space through virtual memory, the number of page swaps required
for this will be very demanding because the accumulator array is used in a
randomly accessed fashion, rarely stopping in contiguous memory as it skips from
index to index.

>   Consider the task of finding ellipses in an 800x600 image. Assuming that the
>   radii of the ellipses are oriented along principal axes, the parameter space
>   is four-dimensional. (x, y) defines the centre of the ellipse, and a and b
>   denote the two radii. Allowing the centre to be anywhere in the image, adds
>   the constraint 0\<x\<800 and 0\<y\<600. If the radii are given the same
>   values as constraints, what is left is a sparsely filled accumulator array
>   of more than 230 billion values.

>   A program thus conceived is unlikely to be allowed to allocate sufficient
>   memory. This doesn't mean that the problem can't be solved, but only that
>   new ways to constrain the size of the accumulator array are to be found,
>   which makes it feasible. For instance:

1.  If it is reasonable to assume that the ellipses are each contained entirely
    within the image, the range of the radii can be reduced. The largest the
    radii can be is if the centre of the ellipse is in the centre of the image,
    allowing the edges of the ellipse to stretch to the edges. In this extreme
    case, the radii can only each be half the magnitude of the image size
    oriented in the same direction. Reducing the range of a and b in this
    fashion reduces the accumulator array to 57 billion values.

2.  Trade accuracy for space in the estimation of the centre: If the centre is
    predicted to be off by 3 on both the x and y axis this reduces the size of
    the accumulator array to about 6 billion values.

3.  Trade accuracy for space in the estimation of the radii: If the radii are
    estimated to each be off by 5 further reduction of the size of the
    accumulator array occurs, by about 256 million values.

4.  Crop the image to areas of interest. This is image dependent, and therefore
    unpredictable, but imagine a case where all of the edges of interest in an
    image are in the upper left quadrant of that image. The accumulator array
    can be reduced even further in this case by constraining all 4 parameters by
    a factor of 2, for a total reduction factor of 16.

>   By applying just, the first three of these constraints to the example stated
>   about, the size of the accumulator array is reduced by almost a factor of
>   1000, bringing it down to a size that is much more likely to fit within a
>   modern computer's memory.

#### 4.8 Efficient ellipse detection algorithm

Yonghong Xie and Qiang Ji give an efficient way of implementing the Hough
transform for ellipse detection by overcoming the memory issues As discussed in
the algorithm (on page 2 of the paper), this approach uses only a
one-dimensional accumulator (for the minor axis) in order to detect ellipses in
the image. The complexity is O(N3) in the number of non-zero points in the
image.

**4.9 Limitations**

The Hough transform is only efficient if a high number of votes fall in the
right bin, so that the bin can be easily detected amid the background noise.
This means that the bin must not be too small, or else some votes will fall in
the neighboring bins, thus reducing the visibility of the main
bin.[[18]](https://en.wikipedia.org/wiki/Hough_transform#cite_note-18)

Also, when the number of parameters is large (that is, when we are using the
Hough transform with typically more than three parameters), the average number
of votes cast in a single bin is very low, and those bins corresponding to a
real figure in the image do not necessarily appear to have a much higher number
of votes than their neighbors. The complexity increases at a rate
of {\\displaystyle {\\mathcal {O}}\\left({A\^{m-2}}\\right)}O(Am-2) with each
additional parameter, where {\\displaystyle A}A is the size of the image space
and *{\\displaystyle m}m* is the number of parameters. (Shapiro and Stockman,
310) Thus, the Hough transform must be used with great care to detect anything
other than lines or circles.

Finally, much of the efficiency of the Hough transform is dependent on the
quality of the input data: the edges must be detected well for the Hough
transform to be efficient. Use of the Hough transform on noisy images is a very
delicate matter and generally, a denoising stage must be used before. In the
case where the image is corrupted by speckle, as is the case in radar images,
the Radon transform is sometimes preferred to detect lines, because it
attenuates the noise through summation.

**Chapter 5: Existing System vs Proposed System**

**5.1 Existing System**

In the current existing system is permitted only to use in ideal road conditions
such as runway. This could not be used in general roads because the edge
detection used till now was Simulink Edge Detection which is implemented in
MATLAB. The secondary thing is in current system Hough transform Space is only
used for angle rotation and has very limited road dataset to detect the objects
in single dimension of an image.

**5.2 Proposed System**

In our proposed system we use Canny Edge Detection replacing the Simulink Edge
Detection which is recent and efficient implementation in Python instead of
MATLAB. Since, Python is the Scripting and Statistical Modelling Language it
supports faster execution for mathematical functions which could be used by
Canny Edge Detection technique. Secondly, we use Hough Transform Space for
3-Dimensional Object detection which could faster and accurate compared to
single dimension object detection.

>   **Chapter 6: Code Snippets**

**6.1 Working Environment**

We use PyCharm IDE as a Working Environment along with Jupyter Notebook for
testing the unit code segments in our project.

**6.2 Code Snippet for Image Capturing**

![](media/15abb9300b3bf9bd6b63155d6dee08a3.png)

**6.3 Code Snippet for Gaussian Blur**

![](media/e4dd51cde1920700838421f3ed169566.png)

![](media/20ddb4608f2878fb304f8f45e30c4376.png)

**6.4 Code Snippet for Hough Transform Space**

**Chapter 7: Future Works and Conclusion**

This project is entirely based on image processing and road detection in
self-driving cars in which has a great scope in future. We would complete the
entire implementation further and then has a scope of the code to implement and
test in reality for research purposes. The updates in algorithms can be done
easily since we do modular implementation and works could be continued in future
for change in implementation of model. We use the pickle file of model to insert
in required areas and then could be easily transferred onto products. So, this
could easily avoid compiling the entire large code every time.

>   **Chapter 8: References**

-   **Road Detection from a Single Image** by Hui Kong – IEEE Publications

-   **Lane Detection for Autonomous Vehicles Using Open CV** by Aditya Singh
    Rathore – IRJET Publications

-   **Autonomously Identifying Perceptron Failures in Self Driving Car** by
    Manikandasriram Srinivasan RamaGopal, Cyrus Anderson, Ram Vasudevan

-   **Autonomous Vehicle and Real Time Raod Lane Detection and Tracking** by
    Farid Bounini, Denis Gingras, Université de Sherbrooke,Sherbrooke, Canada.
