import numpy as np
from PIL import Image, ImageFilter


class Algorithm:
    """ The master algorithm class """
    def __init__(self, width, height, tick=0.2):
        self.width = width
        self.height = height
        self.tick = tick

    def create_empty_array(self):
        return np.zeros((self.height, self.width), dtype=np.uint8)

    @staticmethod
    def remap_array(array, minimum, maximum):
        """
        Remap data :
        OldRange = (OldMax - OldMin)
        NewRange = (NewMax - NewMin)
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
        """
        copy_data = array
        minimum_value = array.min()
        maximum_value = array.max()
        old_range = maximum_value - minimum_value
        new_range = maximum - minimum
        for x in range(0, copy_data.shape[0]):
            for y in range(0, copy_data.shape[1]):
                copy_data[x, y] = (((copy_data[x, y] - minimum_value) * new_range) / old_range) + minimum
        return copy_data

    @staticmethod
    def convert_array_to_image(data, blur_radius=1):
        """ Create the current image
        """
        img = Image.fromarray(data, 'L')
        img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
        return img

    def process(self, data):
        pass

    def print_resolution(self):
        print(f"{self.width} X {self.height}")


class AlgorithmPoint(Algorithm):
    """ Algorithm based on points """
    def __init__(self, width, height, tick=0.2):
        Algorithm.__init__(self, width, height, tick)
        self.width = width
        self.height = height
        self.tick = tick

    def process(self, data):
        print("Process data...")
        # Create a numpy array (x=height, y=width)
        array = self.create_empty_array()
        # print(array[3000, 5000])
        for d in data:
            """ d[1]=height d[0]= width """
            if d[1] <= self.height and d[0] <= self.width:
                array[d[1], d[0]] += 1

        remapped_array = self.remap_array(array, 0, 255)
        return self.convert_array_to_image(data=remapped_array, blur_radius=1)

