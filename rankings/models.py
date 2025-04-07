from django.db import models
import math

class Package(models.Model):
    name = models.CharField(max_length=100)
    total_downloads = models.IntegerField(default=0)
    weekly_downloads = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)
    contributors = models.IntegerField(default=0)
    contributions = models.IntegerField(default=0)
    days_since_last_release = models.IntegerField(default=0)
    score = models.FloatField(default=0.0)

    def calculate_score(self):
        """
        Calculate a weighted score based on multiple metrics.
        All weights are randomly assigned and can be tweaked based on importance.
        """

        # WEIGHTS (To be Fine-Tuned)
        w_total_downloads = 0.15
        w_weekly_downloads = 0.20
        w_stars = 0.10
        w_contributors = 0.10
        w_contributions = 0.10
        w_release_decay = 0.20
        w_freshness_boost = 0.15

        # SAFE LOG FUNCTION
        def safe_log(val):
            return math.log1p(val)  # log(1 + val)

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

    def __str__(self):
        return self.name
