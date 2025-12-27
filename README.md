# KryptosED

![App Icon](KryptosED/utils/images/icon.png)

## English

## Overview

**KryptosED** is a user-friendly tool for encrypting and decrypting files and folders, designed with a modern interface using `customtkinter`. This application provides robust AES-256 encryption with a real-time progress bar, allowing you to monitor encryption/decryption operations. Whether you want to secure your sensitive data, experiment with cryptography, or customize your workspace, this app combines security with user-friendly features.

---

## Why Use This App?

- **Military-Grade Security:** Uses AES-256 encryption, the same standard trusted by governments and security experts worldwide.
- **Real-Time Progress Tracking:** Monitor encryption/decryption operations with a visual progress bar that updates as files are processed.
- **Protect Your Data:** Easily encrypt sensitive information to keep it private from unauthorized access.
- **Learn Encryption:** Perfect for students and enthusiasts to understand modern encryption concepts.
- **Customize Everything:** Change fonts, colors, and images to make the app truly yours.
- **Preview Fonts:** Instantly see how different fonts look before applying them.

---

## Features

- **AES-256 File Encryption/Decryption:**  
  Encrypt or decrypt files with AES-256-CTR mode, one of the most secure encryption standards available. Each encryption generates a unique cryptographic key for maximum security.

- **Real-Time Progress Visualization:**  
  Watch encryption/decryption progress with a dynamic progress bar that updates as each 64KB chunk is processed.

- **Secure Key Management:**  
  Encryption keys are securely generated and saved as binary files. Option to automatically delete keys after successful decryption.

- **Modern Customizable UI:**  
  Built with `customtkinter` for a sleek, modern interface with easy appearance customization.

- **Font Preview Utility:**  
  Use `test_fonts.py` to preview and select from a wide range of fonts before implementing them in the main application.

- **Image & Icon Support:**  
  Easily swap out images and icons to personalize your experience.

- **Batch File Support via Compression:**  
  Encrypt multiple files by first compressing them into a single archive, then encrypting the archive as a single secure file.

---

## Getting Started

### 1. Installation

Make sure you have Python 3.7+ installed. Then, install the required libraries:

Debian / Ubuntu:
```bash
sudo apt install python3-tk
pip install -r requirements.txt
```
Fedora:
```bash
sudo dnf install python3-tkinter
pip install -r requirements.txt
```

Arch Linux
```bash
sudo pacman -S tk
pip install -r requirements.txt
```
**Required Libraries:**
- `PyCryptodome` - For AES-256 encryption implementation
- `customtkinter` - For modern UI components
- `tkinter` - For GUI elements and progress bars
- `Pillow` - For image manipulation and support

### 2. Running the App

Run the Python package:

```bash
python -m KryptosED
```

### 3. Encrypting Files

1. Click "Encrypt File" in the main interface
2. Select the file you want to encrypt
3. A progress bar will appear showing real-time encryption progress
4. After encryption completes, choose a location to save your encryption key
5. The encrypted file now replaces the original (keep the key file safe for decryption!)

### 4. Decrypting Files

1. Click "Decrypt File" in the main interface
2. Select the encrypted file
3. Select the corresponding `.key.bin` file
4. Watch the progress bar as your file is decrypted
5. Choose whether to keep or delete the key file after decryption

### 5. Multiple Files (Compression)

To encrypt or decrypt several files at once, use the app's compression feature:
1. Select multiple files or a folder containing your files.
2. The app will automatically compress them into a single archive (e.g., ZIP).
3. The archive is then encrypted or decrypted as a single file with progress tracking.
4. After decryption, the archive can be extracted to restore the original files.

*This is useful for securely handling batches of files and keeping everything organized.*

---

## Technical Details

### Encryption Method
- **Algorithm:** AES-256 (Advanced Encryption Standard with 256-bit key)
- **Mode:** CTR (Counter Mode) - Provides semantic security and parallel processing
- **Key Generation:** Cryptographically secure random key generation (32 bytes)
- **Nonce:** 8-byte random nonce for CTR mode, stored with encrypted file

### Security Features
- Each encryption operation generates a unique, random key
- Keys are never stored with encrypted data
- No password reuse - each file gets its own cryptographic key
- Progress bar doesn't compromise security - only shows processing status

### Performance
- Processes files in 64KB chunks for memory efficiency
- Real-time progress updates during processing
- Supports files of any size
- Minimal performance overhead for strong encryption

---

## Customizing the App

### Fonts

- Open `src/operation/utils/test_fonts.py` and run it:
  ```bash
  python src/operation/utils/test_fonts.py
  ```
- Browse the font samples.  
- Apply your chosen font in the main app by updating the relevant code section (see comments in the code).

### Images

- Add your image files to /images and change its name to `icon.png`.
- Update the image paths in the code in the variable `title_letter` and `font_letter` in `main.py`.
- Restart the app to see your changes.

### Colors & Styles

- Modify color and style parameters in the code (search for `customtkinter` settings).
- Experiment with different themes and layouts.

### Progress Bar Customization
The progress bar can be customized in `encryption.py` and `decryption.py`:
- Change chunk size for different performance characteristics
- Modify progress bar appearance (color, length, style)
- Add percentage labels or time estimates

---

## Compiling to an Executable (.exe)

Want to share your app as a standalone Windows executable?

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Compile your app:
   ```bash
   pyinstaller --onefile --windowed --name KryptosED --icon=KryptosED/utils/images/icon.png --add-data "KryptosED/utils/images/icon.png;KryptosED/utils/images" KryptosED/__main__.py
   ```
3. Find your `.exe` in the `dist` folder.

**Note:**  
PyInstaller automatically bundles all required dependencies from your Python environment into the executable. You do not need to install dependencies separately on the target machine.

---

## Security Best Practices

1. **Always backup your encryption keys** - Without the key, encrypted files are irrecoverable
2. **Store keys separately from encrypted data** - Never keep them in the same location
3. **Use strong passwords** for your system where keys are stored
4. **Delete keys securely** after use if you no longer need access to the data
5. **Verify file integrity** after decryption by checking file sizes and extensions

---

## Troubleshooting

- **"ModuleNotFoundError: No module named 'Crypto'"**  
  Install PyCryptodome: `pip install pycryptodome`

- **Progress bar doesn't update**  
  Ensure you're running the latest version with the updated encryption/decryption modules

- **Decryption fails**  
  Verify you're using the correct key file for the encrypted file. Each key is unique to its file.

- **Large files take time**  
  This is normal - AES-256 is processing every byte of your file for maximum security

---

## Credits

- Developed by **v0id0100**
- Uses **PyCryptodome** library for AES-256 implementation
- Built with **customtkinter** for modern GUI components
- Progress bar implementation using **tkinter.ttk**

---

**Disclaimer:** This tool is for educational and personal use. The developers are not responsible for any data loss or security breaches resulting from improper use of this software. Always maintain backups of important data before encryption operations.
