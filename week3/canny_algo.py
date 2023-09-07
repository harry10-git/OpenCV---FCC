import cv2
import n


def apply_canny(image, low_threshold, high_threshold):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Calculate gradient magnitude and direction using Sobel operators
    gradient_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
    gradient_direction = np.arctan2(gradient_y, gradient_x)

    # Non-maximum suppression
    gradient_direction = np.degrees(gradient_direction)
    gradient_direction[gradient_direction < 0] += 180
    suppressed_image = np.zeros_like(gradient_magnitude)

    for i in range(1, gradient_magnitude.shape[0] - 1):
        for j in range(1, gradient_magnitude.shape[1] - 1):
            angle = gradient_direction[i, j]
            if 0 <= angle < 22.5 or 157.5 <= angle <= 180:
                if gradient_magnitude[i, j] >= gradient_magnitude[i, j - 1] and gradient_magnitude[i, j] >= \
                        gradient_magnitude[i, j + 1]:
                    suppressed_image[i, j] = gradient_magnitude[i, j]
            elif 22.5 <= angle < 67.5:
                if gradient_magnitude[i, j] >= gradient_magnitude[i - 1, j - 1] and gradient_magnitude[i, j] >= \
                        gradient_magnitude[i + 1, j + 1]:
                    suppressed_image[i, j] = gradient_magnitude[i, j]
            elif 67.5 <= angle < 112.5:
                if gradient_magnitude[i, j] >= gradient_magnitude[i - 1, j] and gradient_magnitude[i, j] >= \
                        gradient_magnitude[i + 1, j]:
                    suppressed_image[i, j] = gradient_magnitude[i, j]
            elif 112.5 <= angle < 157.5:
                if gradient_magnitude[i, j] >= gradient_magnitude[i - 1, j + 1] and gradient_magnitude[i, j] >= \
                        gradient_magnitude[i + 1, j - 1]:
                    suppressed_image[i, j] = gradient_magnitude[i, j]

    # Double thresholding and edge tracking by hysteresis
    edges = np.zeros_like(suppressed_image)
    strong_edges = suppressed_image > high_threshold
    weak_edges = (suppressed_image >= low_threshold) & (suppressed_image <= high_threshold)

    edges[strong_edges] = 255
    visited = np.zeros_like(edges)

    for i in range(1, edges.shape[0] - 1):
        for j in range(1, edges.shape[1] - 1):
            if strong_edges[i, j] and not visited[i, j]:
                visited[i, j] = 1
                dfs(i, j, edges, visited, weak_edges)

    return edges


def dfs(i, j, edges, visited, weak_edges):
    neighbors = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                 (i + 1, j + 1)]
    for ni, nj in neighbors:
        if 0 <= ni < edges.shape[0] and 0 <= nj < edges.shape[1] and weak_edges[ni, nj] and not visited[ni, nj]:
            visited[ni, nj] = 1
            edges[ni, nj] = 255
            dfs(ni, nj, edges, visited, weak_edges)


if __name__ == "__main__":
    input_image_path = "./img1/butter.jpg"  # Change this to your input image path

    low_threshold = 30
    high_threshold = 100

    original_image = cv2.imread(input_image_path)
    edge_image = apply_canny(original_image, low_threshold, high_threshold)

    # Display the original image and the edge-detected image
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Edge-Detected Image", edge_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()