# PopularCode - Popularity Ranking Engine for Open Source Packages

This is a Proof-of-Concept (PoC) Django project that ranks open source packages based on multiple metrics like downloads, GitHub stars, contributors, release activity, and more.  

---

##  Features

- Dynamic scoring algorithm using:
  - Total downloads
  - Weekly downloads
  - GitHub stars
  - Contributors and contributions
  - Days since last release
- Scores calculated using log-scaling and decay for older packages
- Clean, responsive UI with Bootstrap
- Local database with randomly generated sample data > Github and Package Manger APIs


---

## Example Score Calculation (Simplified)

The package score is calculated with the following logic:

```
# NORMALIZED SCORE COMPONENTS
        s_downloads = w_total_downloads * safe_log(self.total_downloads)
        s_weekly = w_weekly_downloads * safe_log(self.weekly_downloads)
        s_stars = w_stars * safe_log(self.stars)
        s_contributors = w_contributors * safe_log(self.contributors)
        s_contributions = w_contributions * safe_log(self.contributions)

        # Older packages get lower scores (Activity Decay)
        s_decay = w_release_decay * (1 / (1 + self.days_since_last_release))

        # Recent release boost
        s_fresh = w_freshness_boost * (100 / (1 + self.days_since_last_release))

        self.score = round(
            s_downloads +
            s_weekly +
            s_stars +
            s_contributors +
            s_contributions +
            s_decay +
            s_fresh, 2
        )
```

Weights (`w1` to `w6`) are customizable in `models.py`.

---

![Screenshot 2025-04-07 204307](https://github.com/user-attachments/assets/85a75758-bf11-4bf5-a68b-a217abbd1e25)


## Installation & Running (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/package-rank.git
cd package-rank
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Populate with Random Data

```bash
python manage.py populate_packages
```

### 6. Start Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to view the PoC.

---



