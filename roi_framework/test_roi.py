import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from roi_framework.models import CostMetrics, BenefitMetrics
from roi_framework.engine import ROIEngine

def run_test():
    # 시나리오: 고객 문의 자동 응답 봇 도입
    # 1. 비용 설정
    costs = CostMetrics(
        development_cost=5000.0,    # 초기 구축비 $5,000
        monthly_api_cost=200.0,     # LLM API 비용 $200
        monthly_infrastructure_cost=50.0, # 서버 비용 $50
        monthly_maintenance_labor=100.0   # 관리 인건비 $100
    )
    
    # 2. 이득 설정
    benefits = BenefitMetrics(
        manual_hours_before=160.0,   # 도입 전: 월 160시간 (Full-time 1명)
        manual_hours_after=20.0,     # 도입 후: 월 20시간 (검수용)
        hourly_labor_rate=30.0,      # 시간당 임금 $30
        error_reduction_value=300.0   # 오류 감소 가치 $300
    )
    
    # 3. 엔진 실행
    engine = ROIEngine(
        project_name="AI Customer Support Bot",
        costs=costs,
        benefits=benefits,
        amortization_months=12
    )
    
    print(engine.generate_report())

if __name__ == "__main__":
    run_test()