from extract_resume import extract_text_from_pdf, extract_skills_from_text
from job_search import search_jobs

# Step 1: Load resume and extract skills
resume_path = "resumes/resume.pdf"  # Make sure this path is correct
text = extract_text_from_pdf(resume_path)
skills = extract_skills_from_text(text)

print("\n Skills found in resume:")
print(skills)

# Step 2: Search for jobs using those skills
print("\n Searching jobs using your skills...\n")
jobs = search_jobs(skills)

# Step 3: Show results
if not jobs:
    print("No jobs found.")
else:
    for i, job in enumerate(jobs, 1):
        print(f"\n 🔹Job {i}:")
        print(" Title:", job.get("job_title"))
        print(" Company:", job.get("employer_name"))
        print(" Location:", job.get("job_city"), job.get("job_country"))
        print(" Apply here:", job.get("job_apply_link"))
        
        
        



