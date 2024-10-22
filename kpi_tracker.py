import time
from datetime import datetime

class KPITracker:
    def __init__(self):
        self.total_interactions = 0
        self.user_engagements = {}
        self.satisfaction_scores = []
        self.first_response_times = []
        self.resolution_rates = []

    def log_interaction(self, user_id):
        self.total_interactions += 1
        if user_id in self.user_engagements:
            self.user_engagements[user_id] += 1
        else:
            self.user_engagements[user_id] = 1

    def log_satisfaction(self, score):
        self.satisfaction_scores.append(score)

    def log_response_time(self, start_time):
        response_time = time.time() - start_time
        self.first_response_times.append(response_time)

    def log_resolution(self, resolved):
        self.resolution_rates.append(1 if resolved else 0)

    def get_metrics(self):
        average_satisfaction = sum(self.satisfaction_scores) / len(self.satisfaction_scores) if self.satisfaction_scores else 0
        average_response_time = sum(self.first_response_times) / len(self.first_response_times) if self.first_response_times else 0
        resolution_rate = sum(self.resolution_rates) / len(self.resolution_rates) if self.resolution_rates else 0

        return {
            "Total Interactions": self.total_interactions,
            "Active Users": len(self.user_engagements),
            "Average Satisfaction Score": average_satisfaction,
            "Average First Response Time": average_response_time,
            "Resolution Rate": resolution_rate,
        }

# Create a global KPI tracker instance
kpi_tracker = KPITracker()
