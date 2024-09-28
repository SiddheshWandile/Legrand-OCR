import cv2
import pytesseract
import re

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding to make the text stand out
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    top_crop = thresh[0:100, :]   # Adjust as needed for the Serial Number
    bottom_crop = thresh[100:, :]  # Adjust as needed for the Cost

    return top_crop, bottom_crop

def extract_text_from_image(crop):
    text = pytesseract.image_to_string(crop, config='--psm 6') 
    return text.strip()

def extract_serial_and_cost(top_text, bottom_text):
    # print(f"Top Text: {top_text}")
    # print(f"Bottom Text: {bottom_text}")
    
    serial_number = re.search(r'Serial Number:\s*(\d+)', bottom_text)
    serial_number = serial_number.group(1) if serial_number else ''

    cost = re.search(r'Cost:\s*([\d,.]+)', bottom_text)
    cost = cost.group(1).replace(',', '') if cost else ''

    return serial_number, cost

def main(image_path):
    top_crop, bottom_crop = preprocess_image(image_path)

    top_text = extract_text_from_image(top_crop)
    bottom_text = extract_text_from_image(bottom_crop)

    top_number, bottom_number = extract_serial_and_cost(top_text, bottom_text)

    print(f"Extracted Serial Number: {top_number}")
    print(f"Extracted Cost: {bottom_number}")

if __name__ == "__main__":
    image_path = "images\sample_image.jpg"  
    main(image_path)
