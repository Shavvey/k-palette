import pathlib as plib
from PIL import Image
import numpy as np
from numpy.typing import NDArray


@staticmethod
def get_pixel_data(file_path: plib.Path) -> NDArray:
    # open image, force into 3-channel RBG space
    image = Image.open(file_path).convert("RGB")
    return np.asarray(image)


def get_resize_image(file_path: str, resize_dims: tuple[int, int]):
    image = Image.open(file_path).convert("RGB")
    image = image.resize(resize_dims)
    image.save("images/image_resized.png")

def k_means(k: int):
    pass
