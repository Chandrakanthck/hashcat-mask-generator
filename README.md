# hashcat-mask-generator
# Hashcat Mask Generator

## 📌 Overview

This repository contains a **Python script** to generate custom **Hashcat masks** dynamically based on user input. Additionally, a **batch script (`command.bat`)** is provided for easy execution of Hashcat using the generated mask files.

---

## ✅ Features

- 🔹 **Generate Hashcat-compatible masks dynamically**
- 🔹 **Accepts custom words and user-defined mask length**
- 🔹 **Saves the generated masks into a text file**
- 🔹 **Batch script to automate Hashcat execution**

---

## 🛠️ How to Use

### 🔹 1. Generate Hashcat Masks

Run the Python script and follow the prompts:

```bash
python hashcat_mask_generator.py
```

- Enter your **custom word list** separated by commas.
- Specify the number of `?1` masks you want.
- A file (`Patterns_X_Mask.txt`) will be **created based on your input**.

---

### 🔹 2. Edit the Batch Script (`command.bat`)

Modify the following sections **to fit your setup**:

```bat
:: Define hashcat path (update this if needed)
set HASHCAT_PATH=hashcat.exe

:: Define custom charset for ?1 (special characters and numbers)
set CHARSET=-1 0123456789!@#_.*

:: Define your hash file (update this to your hash file)
set HASH_FILE=hash.hc22000
```

---

### 🔹 3. Run Hashcat with the Generated Masks

1️⃣ Ensure `hashcat.exe` is in the **same directory** as `command.bat`.<br>
2️⃣ Place your generated mask file (`Patterns_X_Mask.txt`) in the **same folder**.<br>
3️⃣ Rename it to `masks.txt` **or update the batch file** to match your filename.<br>
4️⃣ Run the batch script:

```bat
command.bat
```

5️⃣ If a password is cracked, it will be displayed in `cracked.txt`.

---

## 📝 Notes

- ⚡ **Ensure Hashcat is correctly configured**.
- ⚡ **Modify the `CHARSET` to include/exclude special characters as needed**.
- ⚡ **Update `HASH_FILE` to your actual hash file before running the script**.

---

## 🤝 Contributions

🚀 Feel free to **submit pull requests** or **suggest improvements**!

💻 Happy Cracking! 🔥


