import openai

import requests

from PIL import Image

from io import BytesIO

# Set up OpenAI API key

openai.api_key = "YOUR_API_KEY_HERE"

# Set up default image size

IMAGE_WIDTH = 512

IMAGE_HEIGHT = 512

# Set up the list of available image styles

styles = {

    "Default": "image-alpha-001",

    "Abstract": "image-alpha-002",

    "Landscape": "image-alpha-003",

    "Portrait": "image-alpha-004",

    "Modern": "image-alpha-005"

}

# Set up the list of available image sizes

sizes = {

    "512x512": (512, 512),

    "256x256": (256, 256),

    "128x128": (128, 128)

}

def generate_image(prompt, style, size):

    # Get the OpenAI GPT-3 model ID

    model_id = "image-alpha-001"

    # Set up the image size

    width, height = sizes[size]

    # Generate the image

    response = openai.Completion.create(

        engine="davinci",

        prompt=prompt,

        max_tokens=1024,

        nft_model=model_id,

        nft_size=f"{width}x{height}",

        nft_styles=[styles[style]],

        response_format="url"

    )

    # Load the generated image

    image_url = response.choices[0].text

    image = Image.open(BytesIO(requests.get(image_url).content))

    return image

def main():

    # Get user input for the prompt

    prompt = input("Enter the text prompt: ")

    # Get user input for the style

    print("Available styles:")

    for name, _ in styles.items():

        print(f"- {name}")

    style = input("Enter the style name: ")

    # Get user input for the size

    print("Available sizes:")

    for name, _ in sizes.items():

        print(f"- {name}")

    size = input("Enter the size name: ")

    # Generate the image

    image = generate_image(prompt, style, size)

    # Show the image

    image.show()

    # Save the image to a file

    filename = f"{prompt.replace(' ', '_')}_{style}_{size}.png"

    image.save(filename)

if __name__ == "__main__":

    while True:

        main()

        input("Press any key to continue...")

cls()
