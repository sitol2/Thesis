def categorize_material(pdf_text):
    text_lower = pdf_text.lower()
    
    pro_keywords = ["advanced", "certification", "professional", "case study"]
    kid_keywords = ["kids", "children", "story time", "preschool"]
    
    if any(keyword in text_lower for keyword in pro_keywords):
        return "Professionals"
    elif any(keyword in text_lower for keyword in kid_keywords):
        return "Kids"
    else:
        return "Adults" # Default category
    
file_path = r"C:\Users\Keinji Velina\OneDrive\Desktop\Thesis\Learning Materials\Raw Modules\Volume-5-Fire-Safety-for-Business-Establishments.pdf"
print(categorize_material(file_path))