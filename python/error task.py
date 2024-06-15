def image_info(image_id,image_title):
    if not isinstance(image_id,int):
        raise TypeError("Image_id must contain integers")
    if not isinstance(image_title,str):
        raise TypeError("Image_title must contain string")
    return f"Image {image_title} has id {image_id}"

try:
    image=image_info(5136,'my cat')
    print(image)
except TypeError as e:
    print(e)