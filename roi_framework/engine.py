from .models import CostMetrics, BenefitMetrics

class ROIEngine:
    def __init__(self, project_name: str, costs: CostMetrics, benefits: BenefitMetrics, amortization_months: int = 12):
        self.name = project_name
        self.costs = costs
        self.benefits = benefits
        self.amortization_months = amortization_months

    def calculate_monthly_savings(self) -> float:
        """월간 절감된 순 이익 계산"""
        # 1. 인건비 절감액 (시간 절감 * 시간당 임금)
        hours_saved = self.benefits.manual_hours_base - self.benefits.manual_hours_after
        labor_savings = hours_saved * self.benefits.hourly_labor_rate
        
        # 2. 추가 발생 비용 (API + 인프라 + 유지보수 인건비)
        monthly_running_costs = (
            self.costs.monthly_api_cost + 
            self.costs.monthly_infrastructure_cost + 
            self.costs.monthly_maintenance_labor
        )
        
        # 3. 초기 구축 비용의 월별 분할 상환액 (Amortization)
        monthly_dev_amortization = self.costs.development_cost / self.amortization_months
        
        total_monthly_savings = labor_savings + self.benefits.error_reduction_value - (monthly_running_costs + monthly_dev_amortization)
        return total_monthly_savings

    def calculate_roi_percentage(self) -> float:
        """월간 ROI (%) 계산"""
        savings = self.calculate_monthly_savings()
        # 분모: 월간 발생하는 모든 비용 (운영비 + 개발비 분할액)
        monthly_total_expenditure = (
            self.costs.monthly_api_cost + 
            self.costs.monthly_infrastructure_cost + 
            self.costs.monthly_maintenance_labor +
            (self.costs.development_cost / self.amortization_months)
        )
        
        if monthly_total_expenditure == 0:
            return 0.0
        return (savings / monthly_total_expenditure) * 100

    def calculate_payback_period(self) -> float:
        """초기 구축 비용을 회수하는 데 걸리는 개월 수"""
        # 순수하게 '인건비 절감액'이 '초기 구축 비용'을 넘어서는 시점
        monthly_labor_savings = (self.benefits.manual_hours_before - self.benefits.manual_hours_after) * self.benefits.hourly_labor_rate
        # 운영 비용을 제외한 순수 인건비 절감액으로 초기 비용을 나눔
        if monthly_labor_savings <= 0:
            return float('inf')
        
        # 실제로는 운영비도 고려해야 하므로, '순 이익'이 0이 되는 시점을 찾는 것이 정확함
        # 여기서는 단순화하여 '순 이익'이 발생한다고 가정할 때의 payback 계산
        net_monthly_gain = self.calculate_monthly_savings()
        if net_monthly_gain <= 0:
            return float('inf')
            
        return self.costs.development_cost / net_monthly_gain

    def generate_report(self) -> str:
        savings = self.calculate_monthly_savings()
        roi = self.calculate_roi_percentage()
        payback = self.calculate_payback_period()
        
        report = [
            f"📊 [ROI Report: {self.name}]",
            f"-----------------------------------",
            f"💰 월간 순 이익(Net Savings): ${savings:,.2f}",
            f"📈 월간 ROI: {roi:.2f}%",
            f"⏳ 비용 회수 기간(Payback): {payback:.1f} months",
            f"-----------------------------------"
        ]
        return "\n".join(report)