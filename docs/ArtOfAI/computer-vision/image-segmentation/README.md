# Image segmentation using Tensorflow

### Table of contents
- [What is Image segmentation?](https://)
- Image segementation using tensorflow ([cpu](https://) | [gpu](/code/image-segmentation/image-segmentation-tensorflow-gpu.ipynb))
- [Image segmentation masks](https://)

### What is Image segmentation?

```
*In an image classification task, network assigns a label (or class) to each input image.* However suppose you want to know the shape of that object which pixels belong to which object, etc. In this case, you need to assign a class to each pixel of the image--this task is known as segmentation. A segmentation model returns much more details information about the image. Image segmentation has many applications in medical imaging, self-driving cars and sattilite imaging, etc.

```

In digital image processing and computer, **image segmentation** is the process of partitioning a digital image into multiple **image segment**, also known as **image regions** or **image objects** (set of pixels). More precisely, image segmentation is process of assign labels to every pixel in an image such that the pixels with the same label share certain characteristics.

### Goal of Segmentation

The goal of segmentation is to simply add/or change the representation of an image into something that is more meaningfull and easier to analyze. Image segmentation is typically is used to locate objects and boundaries (lines, curves, etc) in images.

The result of image segmentation is the a set of segments that collectively covers an entire image, or a set of [contours](/docs/glossary/contours.md) extracted from the image (see [edge detection](/docs/glossary/edge-detection.md))

### Image segmentation masks

A segmentation mask is a specific section of an image that is isolate the rest of an image. You can use the output of a segmentation mask to copy the extact areas of an image that has been assigned a labels the computer visio nmodel. For instance, a segmentation mask could be used to isolate diseased leaves on plant.

##### Detection vs Segmentation Masks

Given an image, how can we detect objects (such as people, dog,s apples, etc.) and use those detections in a meaningful way? We define the act of identifying the object in the image as detection.

```
Segmentation can be usefull when shape matters to classification!
```

Once we've detected an object and know where it exists whithin an image, we could then cut out the objects from the rest of the image. This is usefull when you want to highlight part of an image for manual inspection. We call this process creating a mask.

With a mask, you can focus only on the part of image that interests you - for example, a diseased leaf on a plant. Additionally masks ca nbe usefull when lots of similar object in an image exist or the space between object causes lots of problems with classification.

```
Masks reduces the amount of noise in an image by isolating a cut out for the region of interest
```

##### Segmentation Mask Uses Cases

There are many scenarios in which a segmentation mask would be useful, such as:
- Detecting and classifying types of projects on busy gorcery shelves
- Deletecting and classifying the make/model of cars in packaged parking lot.
- Distinguishing between people in crowded shopping mall.
- Tracking individual packages through a shipping center.

In all of these cases, being able to to isolate a particular item in an image is useful.

### [Image normalization](/docs/glossary/image-normalization.md)

**Image normalization** is the process of adjusting the **range and distribution** of pixel values in an image to make training more stable and efficient.



```py
def normalize(input_image, input_mask):
  input_image = tf.cast(input_image, tf.float32) / 255.0
  input_mask -= 1
  return input_image, input_mask
```