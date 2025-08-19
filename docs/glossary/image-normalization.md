# Image normalization

In **image processing**, normalization is a process that changes the range of pixel intensity values, application includes phograms with poor constrast due to glare, for example. Normalization is sometimes called contast streching or histogram stretching. In more general fields of data processing, such as digital signal processing, it is referred to as dynamic range expansion.

The purpose of dynamic range expansion in the various applications is isually to bring the image, or other type of signal, into a range that is more familiar or normal to the senses, hence the term normalization. Oftex, the motivation is to achieve consistency in dynamic range for a set of data, signals or images to avoid mental distraction or fatigue. For example, a newpapaer will strive to make all the of the images in an issue share a similar range of grayscale.

Normalization transforms an n-dimensional grayscale image $I: \{\mathbb{X}\subseteq\mathbb{R}^n\} \rightarrow \{Min, .., Max\}$ with intensity values in the range $\{Min, Max\}$, into a new image ${I_N}: \{\mathbb{X}\subseteq\mathbb{R}^n\} \rightarrow \{newMin, .., newMax\}$ with intensity values in the range $(newMin, newMax)$.

The linear normalization of a grayscale digital image is performed according to the formula $$I_N = (I - Min)\frac{newMax - newMin}{Max - Min}+newMin$$

For example, if the intensity range of the image is 50 to 180 and the desired range is 0 to 255 the process entails subtracting 50 from each of pixel intensity, making the range 0 to 130. Then each pixel intensity is mulitplied by 255/130, making the range 0 to 255

Normalization might also be non linear, this happens when there isn't a linear relationship between $I$ and $I_N$. An example of non-linear normalization is when the normalization forllows a [sigmoid function](./sigmoid.md), in that case, the normalized image is computed according to the formula $$I_N = (newMax - newMin)\frac{1}{1+e^{-\frac{I-\beta}{\alpha}}}+newMin$$

Where $\alpha$ defines the width of the input intensity range, and $\beta$ defines the intensity around which the range is centered.

Auto-normalization in image processing software typically normalizes to the full dynamic range of the number system specified in the image file format.