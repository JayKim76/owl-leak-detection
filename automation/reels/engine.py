import os
import datetime
import re

class ReelsPlannerEngine:
    def __init__(self, persona_tone="Technical, Professional, Insightful"):
        self.persona_tone = persona_tone
        self.output_dir = "automation/reels/outputs"
        os.makedirs(self.output_dir, exist_ok=True)

    def parse_research_data(self, research_text):
        """리서치 보고서에서 핵심 키워드 및 주제를 추출합니다."""
        # 간단한 정규식 기반 추출 (실제 구현 시 LLM API 호출로 대체 가능)
        keywords = re.findall(r'\*\*(.*?)\*\*', research_text)
        topics = re.findall(r'#### \*\*(.*?)\*\*', research_text)
        return {"keywords": keywords, "topics": topics}

    def generate_reels_plan(self, research_text):
        """추출된 데이터를 바탕으로 릴스 스토리보드를 생성합니다."""
        data = self.parse_research_data(research_text)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        plan_path = os.path.join(self.output_dir, f"reels_plan_{timestamp}.md")

        if not data['topics']:
            return "No topics found in research data."

        with open(plan_path, "w", encoding="utf-8") as f:
            f.write(f"# 🎬 Reels Plan: {data['topics'][0]} Focus\n")
            f.write(f"**Generated at:** {datetime.datetime.now().isoformat()}\n")
            f.write(f"**Persona Tone:** {self.persona_tone}\n\n")
            
            f.write("## 🪝 1. The Hook (0-3s)\n")
            f.write(f"- **Visual:** Fast-paced text overlay: 'Stop building simple RAG.'\n")
            f.write(f"- **Audio:** Trending high-energy tech beat.\n\n")

            f.write("## 🧠 2. The Core Content (3-25s)\n")
            f.write(f"- **Visual:** Screen recording of code/architecture diagram ({data['keywords'][0] if data['keywords'] else 'AI Workflow'}).\n")
            f.write(f"- **Script:** 'Everyone talks about RAG, but the real game changer is {data['keywords'][0] if data['keywords'] else 'Agentic Workflow'}. Here is how it works...'\n\n")

            f.write("## 🚀 3. Call to Action (25-30s)\n")
            f.write("- **Visual:** Developer looking at camera or 'Follow for more AI Dev tips'.\n")
            f.write("- **Caption:** 'Want to master the next wave of AI? Follow @Datasys_AI 💻'\n\n")

            f.write("## 🏷️ 4. Hashtags\n")
            f.write(f"#AI #Developer #{data['keywords'][0].replace(' ', '') if data['keywords'] else 'AI_Tech'} #LLMOps #Automation")

        return plan_path

if __name__ == "__main__":
    # 테스트 실행 로직
    engine = ReelsPlannerEngine()
    sample_research = """
    #### **RAG (Retrieval-Augmented Generation) 심화**
    * **Chunking Strategy:** 텍스트 분할 전략.
    #### **Agentic Workflow**
    * **Planning & Reasoning:** 에이전트의 자율적 사고.
    """
    result_path = engine.generate_reels_plan(sample_research)
    print(f"✅ Plan generated at: {result_path}")