# PRODIGY_CS_02
---

# Pixel Manipulation-Based Image Encryption Tool 🛡️

The **Pixel Manipulation-Based Image Encryption Tool** is a web-based application designed to secure images through advanced encryption techniques. Using XOR encryption and pixel swapping, this tool allows users to protect their images with a unique key or seed, making visual data unreadable without the decryption key.

This project is built using **Python** (Flask), **PIL** (Python Imaging Library), and **Bootstrap**, ensuring a smooth user experience, fast processing, and secure encryption.

## 🚀Features 

- **Secure Image Encryption:** Uses pixel manipulation techniques to obscure image data.
- **Decryption Support:** Restore encrypted images to their original form.
- **XOR Encryption:** Uses a bitwise XOR operation to scramble image pixel values, making them unreadable without the decryption key.
- **Pixel Swapping:** Randomly swaps pixels within the image, further complicating the encryption.
- **Lightweight & Fast:**  Optimized for speed and minimal resource usage.
- **Web-Based Interface**: User-friendly interface to easily upload, encrypt, and decrypt images.
- **Customizable Key:** Users can input a custom encryption key or seed for enhanced security.
- **Lightweight & Fast**: Optimized for speed and minimal resource usage.
- **Cross-Platform**: Built with Flask, ensuring compatibility across different platforms.
  


## 🛠️Technologies Used 

- **Python**: Programming language used for backend logic.
- **Flask**: Lightweight web framework to handle HTTP requests and serve the web application.
- **PIL (Pillow)**: Python Imaging Library used for image processing (e.g., loading, modifying pixels).
- **Bootstrap**: Frontend framework used for creating the responsive user interface.
- **HTML/CSS**: Markup and styling for the web pages.

## 🔐How It Works 

1. Upload an image file to encrypt.
2. Provide a key that will be used for encryption.
3. Image is processed using XOR encryption and pixel swapping techniques to secure the image.
4. Download the encrypted image.
5. To view the original image, users input the same key/seed to decrypt it.

## 📥Installation 

### Prerequisites

- Python 3.x
- `pip` (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/KashifMalik777/PRODIGY_CS_02.git
cd PRODIGY_CS_02-main
```

### Install Dependencies

Use `pip` to install the required libraries:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain the following dependencies:

```
Flask==2.1.2
Pillow==8.4.0
```

### Running the Application

After installing the dependencies, you can run the Flask app:

```bash
python pixel_manipulation.py
```

This will start a development server. By default, the app will be available at:

```
http://127.0.0.1:5000
```

## 📷Usage 

1. **Upload Image**: Click the "Choose File" button to upload the image you want to encrypt.
2. **Enter Key**: Enter a unique key or seed (alphanumeric characters) for encryption. This will ensure that the encryption is unique and secure.
3. **Encrypt**: Click the "Encrypt" button to process the image and apply encryption.
4. **Download**: Once encryption is complete, download the encrypted image file.
5. **Decrypt**: To decrypt the image, upload the encrypted image, input the same key used for encryption, and click "Decrypt."

## ⚙️Example Workflow 

1. User uploads `image.jpg`.
2. User enters a key: `123`.
3. Tool encrypts the image using `XOR` and `pixel swapping`.
4. Encrypted image `image_encrypted.jpg` is available for download.
5. User later uploads `image_encrypted.jpg` and enters the same key (`123`) to decrypt it and recover the original image.

---


## 🔒Security Considerations 

- **Key Safety**: The security of the encrypted image depends heavily on the strength and secrecy of the key/seed. It is important to keep the key private.
- **Encryption Strength**: The tool employs basic XOR encryption and pixel manipulation, which is suitable for casual image protection. However, for high-security needs, consider using more advanced cryptographic methods.

## 🤝Contributing 

I welcome contributions! If you have ideas for improvements, fixes, or new features, feel free to open an issue or submit a pull request.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes.
4. Commit your changes: `git commit -m 'Add new feature'`.
5. Push to your fork: `git push origin feature-name`.
6. Open a pull request.

---

### 🏷️Tags 
- `#ImageEncryption`
- `#XOREncryption`
- `#PixelManipulation`
- `#WebApp`
- `#Python`
- `#Flask`
- `#Pillow`
- `#Bootstrap`
- `#DataPrivacy`
- `#ImageSecurity`
- `#Cryptography`
- `#DigitalWatermarking`
- `#EncryptionTool`
- `#PrivacyProtection`
- `#ImageProcessing`

---

## 💬Feel free to reach out via GitHub Issues or contact me directly at vaipatel97@gmail.com 
