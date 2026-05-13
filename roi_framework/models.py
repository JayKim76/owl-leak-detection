from dataclasses import datac_class, field
from typing import Dict, Optional

@dataclass
class CostMetrics:
    """자동화 구축 및 유지에 드는 비용"""
    development_cost: float  # 초기 구축 비용 (인건비, 라이선스 등)
    monthly_api_cost: float  # 매월 발생하는 API 사용료
    monthly_infrastructure_cost: float  # 서버, 클라우드 등 유지 비용
    monthly_maintenance_labor: float  # 유지보수에 드는 인건비

@dataclass
class BenefitMetrics:
    """자동화로 인해 얻는 이득"""
    manual_hours_before: float  # 도입 전 작업에 소요되던 월간 시간
    manual_hours_after: float   # 도입 후 작업에 소요되는 월간 시간
    hourly_labor_rate: float    # 작업자의 시간당 평균 임금
    error_reduction_value: float = 0.0  # 오류 감소로 인한 잠재적 비용 절감액 (선택 사항)

@dataclass
    def automation_project(
        self,
        name: str,
        costs: CostMetrics,
        benefits: BenefitMetrics,
        amortization_period_months: int = 12
    ):
        self.name = name
        self.costs = costs
        self.benefits = benefits
        self.amortization_period_months = amortization_period_months