import cv2
import numpy as np

from ..models.image import Image

def imageMatchingHandler(image1: np.array, image2: np.array) -> float:
    """Image Matching Hnadler

    Args:
        image1 (np.array): image1 to match
        image2 (np.array): image2 to match


    Returns:
        float:  percentage matched
    """

    return matcher(image1, image2)


def matcher(image1: np.array, image2: np.array) -> float:
    """Image Matching Function

    Args:
        image1 (np.array): image1 to match
        image2 (np.array): image2 to match

    Returns:
        float: 
    """
    sift = cv2.SIFT_create()

    keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(descriptors1, descriptors2, k = 2)

    good = []
    for m,n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])

    num_matches = len(good)
    return (num_matches * 100 / len(keypoints1))