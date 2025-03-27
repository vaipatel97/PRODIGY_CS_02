from flask import Flask, render_template, request, redirect, flash
from PIL import Image
import io
import random
import base64

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a strong secret key

def xor_encrypt(image, key):
    # Encrypts (or decrypts) the image by applying XOR on each pixel channel.
    img = image.convert("RGB")
    width, height = img.size
    pixels = img.load()
    encrypted_img = Image.new("RGB", (width, height))
    encrypted_pixels = encrypted_img.load()
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            encrypted_pixels[i, j] = (r ^ key, g ^ key, b ^ key)
    return encrypted_img

def swap_pixels_encrypt(image, seed):
    # Encrypts the image by shuffling (swapping) pixels based on a random seed.
    img = image.convert("RGB")
    width, height = img.size
    pixels = list(img.getdata())
    random.seed(seed)
    indices = list(range(len(pixels)))
    random.shuffle(indices)
    new_pixels = [None] * len(pixels)
    for i, new_index in enumerate(indices):
        new_pixels[new_index] = pixels[i]
    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(new_pixels)
    return encrypted_img

def swap_pixels_decrypt(image, seed):
    # Decrypts an image that was encrypted by pixel swapping using the same seed.
    img = image.convert("RGB")
    width, height = img.size
    pixels = list(img.getdata())
    random.seed(seed)
    indices = list(range(len(pixels)))
    random.shuffle(indices)
    original_pixels = [None] * len(pixels)
    for i, new_index in enumerate(indices):
        original_pixels[i] = pixels[new_index]
    decrypted_img = Image.new("RGB", (width, height))
    decrypted_img.putdata(original_pixels)
    return decrypted_img

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Validate image upload
        if "image" not in request.files or request.files["image"].filename == "":
            flash("Please upload an image file.")
            return redirect(request.url)
        
        file = request.files["image"]

        # Validate key (or seed)
        try:
            key = int(request.form.get("key"))
        except (ValueError, TypeError):
            flash("Key/Seed must be an integer.")
            return redirect(request.url)
        
        mode = request.form.get("mode")
        method = request.form.get("method")
        
        # Open the image
        try:
            image = Image.open(file.stream)
        except Exception as e:
            flash(f"Error opening image: {e}")
            return redirect(request.url)
        
        # Process based on method and mode
        if method == "xor":
            result_image = xor_encrypt(image, key)
        elif method == "swap":
            if mode == "encrypt":
                result_image = swap_pixels_encrypt(image, key)
            elif mode == "decrypt":
                result_image = swap_pixels_decrypt(image, key)
            else:
                flash("Invalid mode selected.")
                return redirect(request.url)
        else:
            flash("Invalid method selected.")
            return redirect(request.url)
        
        # Convert the processed image to a base64 string to embed in HTML.
        buffer = io.BytesIO()
        result_image.save(buffer, format="PNG")
        buffer.seek(0)
        img_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        # Pass the key along with the image data so it can be shown in the result.
        return render_template("result.html", image_data=img_data, key=key)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
