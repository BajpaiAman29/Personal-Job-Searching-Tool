import requests

def search_jobs(skills):
    query = "devops engineer aws"
    print("[DEBUG] Searching with query:", query)
    
    url = "https://jsearch.p.rapidapi.com/search"
    
    # Your actual API key here (keep it secret in real apps)
    headers = {
        "X-RapidAPI-Key": "7fd6996507msha1478febb0665e7p1bfcd9jsna12aa8a83707",
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    # Request parameters
    params = {
        "query": query,
        "page": 1,
        "num_pages": 1,
        "country": "in",  # You can change to 'us' or any country code
        "date_posted": "all"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        print("📡 API Status:", response.status_code)

        if response.status_code != 200:
            print("❌ API error:\n", response.text)
            return []

        data = response.json()
        return data.get("data", [])

    except Exception as e:
        print("❌ Exception:", e)
        return []
# Test it
if __name__ == "__main__":
    skills = ["devops", "aws", "docker"]  # Replace with resume skills later
    job_results = search_jobs(skills)

    for i, job in enumerate(job_results, 1):
        print(f"\n🔹 Job {i}:")
        print(" Title:", job.get("job_title"))
        print(" Company:", job.get("employer_name"))
        print(" Location:", job.get("job_city"), job.get("job_country"))
        print(" Apply here:", job.get("job_apply_link"))
