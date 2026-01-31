from rembg import remove
from PIL import Image

input_path = r'D:\HTML\suwi.jpg'
output_path = r'D:\HTML\suwi.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
