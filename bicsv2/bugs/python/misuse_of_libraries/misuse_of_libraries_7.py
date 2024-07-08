import cv2

def image_processing_operations(image_path):
    image = cv2.imread(image_path)
    grayscale = cv2.imcvtcolor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.imgaussianblur(grayscale, (5, 5), 0)
    edges = cv2.imcanny(blurred, 50, 150)
    resized = cv2.imresize(image, (100, 100))

    results = {
        'original': image,
        'grayscale': grayscale,
        'blurred': blurred,
        'edges': edges,
        'resized': resized
    }

    return results
