import json
import pdfminer.high_level
import docx
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    return pdfminer.high_level.extract_text(BytesIO(pdf_file.read()))

def extract_text_from_docx(docx_file):
    doc = docx.Document(BytesIO(docx_file.read()))
    return " ".join([para.text for para in doc.paragraphs])

def validate_resume(uploaded_file, role):
   
    with open("skills.json", "r") as f:
        skills_data = json.load(f)
    

    required_skills = set(skill.lower() for skill in skills_data.get(role, []))
    
    if not required_skills:
        return "No skill requirements defined for this role"
    

    file_type = uploaded_file.name.split(".")[-1].lower()
    try:
        if file_type == "pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        elif file_type == "docx":
            resume_text = extract_text_from_docx(uploaded_file)
        else:
            return "Unsupported file format"
    except Exception as e:
        return f"Error processing file: {str(e)}"

    resume_words = set(word.lower() for word in resume_text.split())
    

    matched_skills = required_skills.intersection(resume_words)
    match_percentage = (len(matched_skills) / len(required_skills)) * 100
    
   
    result = {
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(required_skills - matched_skills),
        "match_percentage": match_percentage
    }
    
 
    if match_percentage >= 70:
        approval = "✅ Strong Match"
    elif match_percentage >= 50:
        approval = "✅ Moderate Match"
    elif match_percentage >= 30:
        approval = "⚠️ Partial Match"
    else:
        approval = "❌ Low Match"
    
    output = f"""
    {approval} ({match_percentage:.1f}%)
    
    **Matched Skills:** {', '.join(result['matched_skills']) or 'None'}
    
    **Missing Skills:** {', '.join(result['missing_skills']) or 'None'}
    """
    
    return output