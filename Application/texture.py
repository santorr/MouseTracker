import numpy as np
from PIL import Image, ImageFilter
import math


class Texture:
    def __init__(self, width, height):
        """ Create an array texture """
        self.width = width
        self.height = height

        self.array = np.zeros((self.height, self.width), dtype=np.uint8)

    def print_new_data(self, x_origin, y_origin, radius=2):
        """ Increment a specific cell """
        try:
            for x in range(-radius, radius):
                temp = int(math.sqrt(radius*radius - x * x))
                for y in range(-temp, temp):
                    self.array[y+y_origin, x+x_origin] += 1
        except:
            pass

    def reset(self):
        """ Fill array with 0 """
        self.array.fill(0)

    def get_image(self, blur_radius=1):
        """ Create the current image
        :param blur_radius: the blur value
        :type blur_radius: int
        :rtype: Image
        :returns: "Return an image clamp(0, 255) with mouse data"
        """
        remap_data = np.uint8(self.remap_data(0, 255))
        img = Image.fromarray(remap_data, 'L')
        img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
        return img

    def remap_data(self, minimum, maximum):
        """
        Remap data :
        OldRange = (OldMax - OldMin)
        NewRange = (NewMax - NewMin)
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
        """
        copy_data = self.array

        minimum_value = self.array.min()
        maximum_value = self.array.max()

        old_range = maximum_value - minimum_value
        new_range = maximum - minimum

        for x in range(0, copy_data.shape[0]):
            for y in range(0, copy_data.shape[1]):
                copy_data[x, y] = (((copy_data[x, y] - minimum_value) * new_range) / old_range) + minimum

        return copy_data

    def return_array(self):
        """ Return the array data """
        return self.array
