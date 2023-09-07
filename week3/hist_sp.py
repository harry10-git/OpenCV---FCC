import cv2
import numpy as np

def histogram_specification(input_image, reference_image):
    # Read the input image and reference image
    img_input = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)
    img_reference = cv2.imread(reference_image, cv2.IMREAD_GRAYSCALE)

    # Calculate histograms for both images
    hist_input = cv2.calcHist([img_input], [0], None, [256], [0, 256])
    hist_reference = cv2.calcHist([img_reference], [0], None, [256], [0, 256])

    # Calculate cumulative distribution functions (CDFs) for both histograms
    cdf_input = hist_input.cumsum()
    cdf_reference = hist_reference.cumsum()

    # Normalize CDFs to [0, 255]
    cdf_input_normalized = (cdf_input / cdf_input[-1]) * 255
    cdf_reference_normalized = (cdf_reference / cdf_reference[-1]) * 255

    # Create a mapping lookup table
    mapping = np.interp(range(256), cdf_input_normalized, cdf_reference_normalized).astype(np.uint8)

    # Apply histogram specification using LUT
    img_output = cv2.LUT(img_input, mapping)

    return img_output

if __name__ == "__main__":
    input_image_path = 'inp_image.webp'
    reference_image_path = 'ref_image.webp'

    output_image = histogram_specification(input_image_path, reference_image_path)

    # Display or save the resulting image
    cv2.imshow('Input Image', cv2.imread(input_image_path))
    cv2.imshow('Reference Image', cv2.imread(reference_image_path))
    cv2.imshow('Histogram Specified Image', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
