from PIL import Image, ImageDraw, ImageFont

def generate_image(img_path):
    tree_image = Image.open(img_path)
    draw = ImageDraw.Draw(tree_image)

    font = ImageFont.load_default(size=20)

    draw.text((350,270), "Hello world", fill="black", anchor="ms", font=font)
    
    tree_image.save("test.jpg", "JPEG")
    


generate_image("./tree_models/ArbreGenealogique2.jpg")