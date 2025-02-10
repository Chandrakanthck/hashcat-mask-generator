# Hashcat Mask Generator

## 📌 Overview

This repository contains a **Python script** to generate custom **Hashcat masks** dynamically based on user input. Additionally, a **batch script (`ExecuteMask.bat`)** is provided for easy execution of Hashcat using the generated mask files.

---

## ✅ Features

- 🔹 **Generate Hashcat-compatible masks dynamically**
- 🔹 **Enter custom words and define mask length**
- 🔹 **Automatically save formatted mask patterns**
- 🔹 **Batch script to automate Hashcat execution**

---

## 🔹 Why Use Masking Instead of Wordlists?

- Creating a large wordlist takes **huge space and time**.
- Wordlists contain many **unnecessary words** for the process.
- Masking **shrinks the process**, generating combinations **on the fly**.
- Each mask contains **many possible variations**, **no need for extra storage**.
- This repository **simplifies the mask creation** for custom words/names with **numbers, special characters, uppercase, and lowercase combinations** using `?1` placement.
- The included **batch file makes execution easy on Windows**, allowing seamless **GPU acceleration** for **fast parallel processing**.
- Ensure you have the **necessary dependencies installed**, such as **CUDA Toolkit** for optimal Hashcat performance.

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

### 🔹 2. Edit the Batch Script (`ExecuteMask.bat`)

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

1️⃣ Ensure `hashcat.exe` is in the **same directory** as `ExecuteMask.bat`.<br>
2️⃣ Place your generated mask file (`Patterns_X_Mask.txt`) in the **same folder**.<br>
3️⃣ Rename it to `masks.txt` **or update the batch file** to match your filename.<br>
4️⃣ Run the batch script:

```bat
ExecuteMask.bat
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

