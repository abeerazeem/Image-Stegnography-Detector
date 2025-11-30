import numpy as np
from PIL import Image

def embed_lsb(img_path, payload_ratio=0.5):

    img = Image.open(img_path)
    if img.mode != "RGB":
        img = img.convert("RGB")

    arr = np.array(img, dtype=np.uint8)
    flat_arr = arr.flatten()

    num_pixels = flat_arr.size
    num_bits_to_embed = int(num_pixels * payload_ratio)


    msg_bits = np.random.randint(0, 2, num_bits_to_embed)


    flat_arr[:num_bits_to_embed] = (flat_arr[:num_bits_to_embed] & 0xFE) | msg_bits

    new_arr = flat_arr.reshape(arr.shape)
    return Image.fromarray(new_arr)
