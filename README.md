# Image Enhancement using CLAHE

This Python script demonstrates the use of the Contrast Limited Adaptive Histogram Equalization (CLAHE) method for enhancing the contrast of an image. The script uses OpenCV, NumPy, and Matplotlib libraries.

## Code Description

1. **Import Libraries**: The script begins by importing the necessary libraries - `cv2` for image processing, `numpy` for numerical operations, and `matplotlib.pyplot` for plotting.

2. **Load Image**: The script reads an image file named 'blurry_image.jpg' in color mode.

3. **Color Model Conversion**: The image is then converted from the BGR color model to the YCrCb color model. This is done because the Y channel in YCrCb represents luminance, which is what we want to apply the histogram equalization to.

4. **Split Channels**: The YCrCb image is split into its constituent channels - Y, Cr, and Cb.

5. **Define and Apply CLAHE**: A CLAHE object is created with a clip limit of 3.0 and a tile grid size of 8x8. This object is used to apply the CLAHE method to the Y channel.

6. **Merge Channels**: The enhanced Y channel is then merged back with the original Cr and Cb channels.

7. **Convert Back to BGR**: The image is converted back from the YCrCb color model to the BGR color model.

8. **Display Images**: The original and final images are displayed side by side using Matplotlib. The images are displayed in the RGB color model, so they are first converted from BGR to RGB.

9. **Save Image**: The script also includes a key press event that allows the user to save the final image by pressing the 'c' key.

## Usage

To run the script, you need to have Python installed along with the `cv2`, `numpy`, and `matplotlib` libraries. You can then run the script using any Python IDE or from the command line using the command `python script_name.py`.

Please replace 'script_name.py' with the name of the script file. Also, make sure that the image 'blurry_image.jpg' is in the same directory as the script or provide the full path to the image in the `cv2.imread()` function.

## Output

The script displays the original and the CLAHE enhanced images side by side. Press 'c' to save the final image as 'clahe_image.jpg'.

This script is a simple demonstration of the CLAHE method and can be modified or expanded based on your specific requirements.
