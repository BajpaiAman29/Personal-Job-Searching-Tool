import PyPDF2
import re

# Function to extract the text from pdf:
def extract_text_from_pdf(file_path):
    text = ""
    
    with open(file_path,"rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or "" 
            
    return text.lower() # convert all text to lower case for easy matching

# Function to extract keywords from text:
def extract_skills_from_text(text):
    # define a list of devops related keywords
    
    skill_keywords = [
        "devops", "aws", "docker", "kubernetes", "jenkins",
        "linux", "git", "github", "bash", "terraform",
        "cloud", "python", "ansible", "azure", "monitoring",
        "ci/cd", "scripting", "automation", "infrastructure as code"
    ] 
    
# use regex to extract only words:
    words = re.findall(r'\b[a-zA-Z]+\b', text)

# keep only words that matches our resume
    matched_skills = list(set(word for  word in words if word in skill_keywords))
    return matched_skills

# Test it manually by running this file
if __name__ == "__main__":
    path = "resumes/resume.pdf"  # Change path if needed
    text = extract_text_from_pdf(path)
    skills = extract_skills_from_text(text)

    print("Skills found in resume:\n", skills)

