import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('blurry_image.jpg', cv2.IMREAD_COLOR)

# Convert the image to YCrCb color model 
image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Split the YCrCb image into Y, Cr and Cb channels
y, cr, cb = cv2.split(image_ycrcb)

# Define the CLAHE method
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))

# Apply the CLAHE to the Y channel
cl = clahe.apply(y)

# Merge the CLAHE enhanced Y channel with the original Cr and Cb channels
merged_channels = cv2.merge((cl,cr,cb))

# Convert image from YCrCb color model back to RGB color model
final_image = cv2.cvtColor(merged_channels, cv2.COLOR_YCrCb2BGR)

# Display the images
fig, axs = plt.subplots(1, 2, figsize=(20, 20))

axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original')
axs[0].axis('off')

axs[1].imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
axs[1].set_title('CLAHE\nPress "C" to save this image')
axs[1].axis('off')

# Maximize the plot window
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')

# Define the key press event
def on_key(event):
    if event.key.lower() == 'c':
        cv2.imwrite('clahe_image.jpg', cv2.cvtColor(final_image, cv2.COLOR_RGB2BGR))
        print('CLAHE image saved as clahe_image.jpg')

# Connect the key press event to the current figure
fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
