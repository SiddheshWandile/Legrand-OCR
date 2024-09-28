# Legrand OCR Project

This project is designed to extract specific details (Serial Number and Cost) from an image using Optical Character Recognition (OCR) with Python. The main goal is to process images of product labels, automatically detect and extract the serial number and cost, and store or display this data in a usable format.

## Features
- Extracts Serial Number and Cost from images using **Tesseract OCR**.
- Supports image preprocessing for improved text extraction.
- Uses regular expressions to accurately capture specific patterns for serial numbers and costs.

## Prerequisites

Before you can run the project, ensure you have the following installed:

1. **Python 3.x**: [Download Python](https://www.python.org/downloads/)
2. **Tesseract OCR**: Download and install Tesseract OCR based on your operating system:
   - For Windows, download the installer from [here](https://github.com/UB-Mannheim/tesseract/wiki) and follow the setup instructions.
   - After installation, ensure Tesseract is added to your system’s PATH.
   
3. Python Libraries:
   - Install the required libraries using the following command:
     ```bash
     pip install -r requirements.txt
     ```

