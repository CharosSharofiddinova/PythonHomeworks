from PIL import Image
import numpy as np

# Load the image using PIL and convert to numpy array
image = Image.open("images/birds.jpg")
image_np = np.array(image)

# Flip the image horizontally and vertically
flipped_image = np.flipud(np.fliplr(image_np))  # flip up-down and left-right

# Step 3: Add random noise
noise = np.random.randint(0, 50, image_np.shape, dtype='uint8')  # small noise
noisy_image = np.clip(image_np + noise, 0, 255).astype('uint8')  # add and clip

#  Brighten channels (e.g., Red channel by 40)
brightened_image = image_np.copy()
brightened_image[:, :, 0] = np.clip(brightened_image[:, :, 0] + 40, 0, 255)  # Red channel

#  Apply a black mask to a 100x100 center region
masked_image = image_np.copy()
h, w = masked_image.shape[:2]
start_y = h // 2 - 50
start_x = w // 2 - 50
masked_image[start_y:start_y+100, start_x:start_x+100] = [0, 0, 0]

#  Save all results
Image.fromarray(flipped_image).save("output/flipped_image.jpg")
Image.fromarray(noisy_image).save("output/noisy_image.jpg")
Image.fromarray(brightened_image).save("output/brightened_image.jpg")
Image.fromarray(masked_image).save("output/masked_image.jpg")
