from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

# Image mapping
image_mapping = {
    'RightAtHome': 'RightAtHome',
    'MerryCassowary': 'MerryCassowary',
    'SayCuddle': 'SayCuddle',
    "I'mAllEars": 'ImAllEars',
    'Hanginthere': 'Hanginthere',
    'Magni-pheasant': 'Magni-pheasant',
    'MarineModel': 'MarineModel',
    'IcyUnicorn': 'IcyUnicorn',
    'HowlyCubs': 'HowlyCubs',
    'PreeningTime': 'PreeningTime',
    'Flippincouple': 'Flippincouple',
    'Pickpocket': 'Pickpocket',
    'BottlenoseBud': 'BottlenoseBud',
    'LionAround': 'LionAround'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_images = request.form.getlist('image')
        if selected_images:
            generate_collage(selected_images)
    return render_template('index.html', image_mapping=image_mapping, collage_url=None)

def generate_collage(selected_images):
    collage_size = (800, 800)
    collage = Image.new('RGB', collage_size)
    x_offset, y_offset = 0, 0

    for identifier in selected_images:
        image_filename = image_mapping.get(identifier)
        if image_filename:
            img = Image.open(f'static/images/{image_filename}.jpg')
            img = img.resize((collage_size[0] // 2, collage_size[1] // 2))
            collage.paste(img, (x_offset, y_offset))

            x_offset += img.width
            if x_offset >= collage_size[0]:
                x_offset = 0
                y_offset += img.height

    output_filename = 'static/collage.jpg'
    collage.save(output_filename)
    return output_filename

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

