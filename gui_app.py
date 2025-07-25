import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from extract_resume import extract_text_from_pdf, extract_skills_from_text
from job_search import search_jobs

# ------------------- Upload + Job Search Logic -------------------

def upload_and_process():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title="Select your resume PDF"
    )
    if not file_path:
        return

    try:
        text = extract_text_from_pdf(file_path)
        skills = extract_skills_from_text(text)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f" Skills Found:\n", "section")
        result_text.insert(tk.END, f"{', '.join(skills)}\n\n")

        result_text.insert(tk.END, " Searching for jobs...\n\n", "section")

        jobs = search_jobs(skills)
        if not jobs:
            result_text.insert(tk.END, " No jobs found.\n", "error")
        else:
            for i, job in enumerate(jobs, 1):
                result_text.insert(tk.END, f"🔹 Job {i}\n", "job")
                result_text.insert(tk.END, f"🔸 Title: {job.get('job_title')}\n", "label")
                result_text.insert(tk.END, f" Company: {job.get('employer_name')}\n")
                result_text.insert(tk.END, f" Location: {job.get('job_city')} - {job.get('job_country')}\n")
                result_text.insert(tk.END, f" Apply: {job.get('job_apply_link')}\n\n", "link")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ------------------- GUI Styling -------------------

root = tk.Tk()
root.title("🛠️ DevOps Job Notifier")
root.geometry("820x650")
root.configure(bg="#f0f2f5")
root.resizable(False, False)

# Custom Fonts and Colors
font_title = ("Helvetica", 20, "bold")
font_button = ("Helvetica", 12, "bold")
font_output = ("Consolas", 10)

# Heading
title = tk.Label(root, text="🛠️ DevOps Job Notifier", font=font_title, bg="#f0f2f5", fg="#222")
title.pack(pady=15)

# Upload Button
upload_button = tk.Button(
    root,
    text="📄 Upload Resume (.pdf)",
    command=upload_and_process,
    font=font_button,
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    padx=20,
    pady=10,
    bd=0,
    relief="ridge",
    cursor="hand2"
)
upload_button.pack(pady=10)

# Output Text Box
result_text = scrolledtext.ScrolledText(
    root,
    height=28,
    width=96,
    font=font_output,
    bg="white",
    fg="#333",
    padx=10,
    pady=10,
    wrap=tk.WORD,
    borderwidth=2,
    relief="groove"
)
result_text.pack(padx=20, pady=10)

# Custom tag styles for highlighting
result_text.tag_configure("section", foreground="#0B5394", font=("Helvetica", 11, "bold"))
result_text.tag_configure("label", foreground="#1C4587", font=("Helvetica", 10, "bold"))
result_text.tag_configure("link", foreground="blue", underline=1)
result_text.tag_configure("job", foreground="#3c3c3c", font=("Helvetica", 11, "bold"))
result_text.tag_configure("error", foreground="red", font=("Helvetica", 11, "italic"))

# Launch
root.mainloop()
