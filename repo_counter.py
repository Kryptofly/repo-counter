import requests
import json

# Αντικατέστησε το 'your-username' με το πραγματικό όνομα χρήστη σου στο GitHub
username = "your-username"

# Σύνδεσμος API για να πάρεις τις πληροφορίες του χρήστη
url = f"https://api.github.com/users/{Kryptofly}/repos"

# Κάνουμε το αίτημα GET
response = requests.get(url)

if response.status_code == 200:
    # Μετατρέπουμε την απόκριση σε JSON
    repos = json.loads(response.text)
    # Μετράμε τον αριθμό των repositories
    repo_count = len(repos)
    print(f"Ο αριθμός των repositories για τον χρήστη {username} είναι: {repo_count}")
else:
    print("Κάτι πήγε στραβά. Δεν μπορώ να πάρω τα repositories.")

