# PRODIGY_CS_02

# Pixel Manipulation-Based Image Encryption Tool🖼️

## Overview
The **Pixel Manipulation-Based Image Encryption Tool** is a secure and efficient way to encrypt and decrypt images using pixel transformation techniques. This tool ensures confidentiality by scrambling pixel values based on encryption keys, making unauthorized access difficult.

## 🚀Features  
- **Secure Image Encryption:** Encrypts images using pixel-level transformations.
- **Decryption Support:** Restores original images with the correct decryption key.
- **Fast Processing:** Optimized algorithms for quick encryption and decryption.
- **User-Friendly Interface:** Simple CLI or GUI-based interaction.
- **Supports Multiple Formats:** Works with PNG, JPG, and BMP images.
- **Cross-Platforms:** Built with Flask, ensuring compatibility across different platform systems.
- **Lightweight & Fast:** Optimized for speed and minimal resource usage.
- **XOR Encryption:** Uses a bitwise XOR operation to scramble image pixel values, making them unreadable without the decryption key.
- **Pixel Swapping:** Randomly swaps pixels within the image, further complicating the encryption.
- **Customizable Key/Seed:** Users can input a custom encryption key or seed for enhanced security.

## 🛠️Technology Used
- **Programming Languag:** Python for backend.
- **Web Framework:** Flask to handle HTTP requests and serve the web application.
- **Library:** PIL(Pillow)-Python Imaging Library used for image processing (e.g., loading, modifying pixels).
- **Bootstrap:** Frontend framework used for creating the responsive user interface.
- **HTML/CSS:** Markup and styling for the web pages.


## 🔐 How It Works
1. **Upload an Image:** Select an image to encrypt.
2. **Enter a Key:** Provide a key for encryption.
3. **Encrypt the Image:** The tool scrambles the image using XOR encryption and pixel swapping.
4. **Download Encrypted Image:** Save the encrypted file.
5. **Decrypt the Image:** Use the same key to restore the original image.

## 📥Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required (Python package manager) Libraries: `pip`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/vaipatel97/PRODIGY_CS_02.git
   ```
2. Navigate to the directory:
   ```bash
   cd PRODIGY_CS_02-main
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. The [requirements.txt] file should contain the following dependencies:
``` bash
Flask==2.1.2
Pillow==8.4.0
```
### Running the Application
5. After installing the dependencies, you can run the Flask app:
```python
python pixel_manipulation.py
```
6. This will start a development server. By default, the app will be available at: http://127.0.0.1:5000


## 📷Usage

1. **Upload Image:** Click the "Choose File" button to upload the image you want to encrypt.

2. **Enter Key:** Enter a unique key or seed (alphanumeric characters) for encryption. This will ensure that the encryption is unique and secure.
   
3. **Encrypt:** Click the "Encrypt" button to process the image and apply encryption.
 
4. **Download:** Once encryption is complete, download the encrypted image file.
   
5. **Decrypt:** To decrypt the image, upload the encrypted image, input the same key used for encryption, and click "Decrypt."

## ⚙️Example

1.User uploads ```image.jpg```.

2.User enters a ```key: 123```.

3.Tool encrypts the image using ```XOR``` and ```pixel swapping```.

4.Encrypted image ```image_encrypted.jpg``` is available for download.

5.User later uploads ```image_encrypted.jpg``` and enters the same key ```(123)``` to decrypt it and recover the original image.

## 🔒Security Considerations
- Keep your encryption key secure; without it, decryption is impossible.
- Avoid using weak or predictable keys.
- This tool does not store encryption keys, ensuring privacy.

## Future Enhancements
- Implement AES-based hybrid encryption.

## 🤝Contributing
Contributions are welcome! If you want to improve this tool, follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push the branch and create a pull request.

## 💬Contact
For any queries or suggestions, feel free to contact:
- Email: vaipatel97@gmail.com

## 🏷️Hashtags
#ImageEncryption #Cybersecurity #Python #PixelManipulation #EncryptionTool #DataSecurity

