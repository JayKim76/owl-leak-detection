import json
import os

class ROIEngine:
    def __init__(self):
        pass

    def calculate_case(self, case_data):
        m = case_data['metrics']
        vol = m['monthly_volume']
        
        # 1. Manual Costs & Time
        manual_time_monthly = (m['manual_process']['time_per_task_minutes'] * vol) / 60
        manual_cost_monthly = manual_time_monthly * m['manual_process']['cost_per_minute']
        
        # 2. AI Costs & Time
        ai_time_monthly = (m['ai_process']['time_per_task_minutes'] * vol) / 60
        ai_variable_cost = m['ai_process']['cost_per_task_usd'] * vol
        ai_total_cost_monthly = ai_variable_cost + m['ai_process']['api_cost_per_month_usd']
        
        # 3. Deltas
        time_saved_hours = manual_time_monthly - ai_time_monthly
        cost_saved_usd = manual_cost_monthly - ai_total_cost_monthly
        productivity_gain = ((manual_time_monthly / ai_time_monthly) - 1) * 100 if ai_time_monthly > 0 else 0
        
        # 4. ROI (Simplified: (Savings - Cost) / Cost)
        # Note: Here cost is the new AI operational cost
        roi_percent = (cost_saved_usd / ai_total_cost_monthly) * 100 if ai_total_cost_monthly > 0 else 0

        return {
            "case_id": case_data['case_id'],
            "title": case_data['title'],
            "department": case_data['department'],
            "monthly_savings_usd": round(cost_saved_usd, 2),
            "monthly_time_saved_hours": round(time_saved_ss_hours := time_saved_hours, 2),
            "productivity_gain_percent": round(productivity_gain, 2),
            "roi_percent": round(roi_percent, 2),
            "annual_savings_projection": round(cost_saved_usd * 12, 2)
        }