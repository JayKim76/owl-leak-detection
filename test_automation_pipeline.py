import os
from automation.reels.engine import ReelsPlannerEngine

def test_pipeline():
    print("🚀 Starting Automation Pipeline Test...")
    
    # 1. Mock Researcher Output
    research_report = """
    ### 🔍 AI Developer Trends
    #### **Agentic Workflow**
    - Focus on Planning and Reasoning.
    #### **LLMOps**
    - Focus on Deployment and Monitoring.
    """
    
    # 2. Initialize Engine
    engine = ReelsPlanner
    engine = ReelsPlannerEngine(persona_tone="Professional & Cutting-edge")
    
    # 3. Run Generation
    try:
        output_file = engine.generate_reels_plan(research_report)
        print(f"✨ Success! Output file created: {output_file}")
        
        # 4. Verify Content
        if os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if "Agentic Workflow" in content:
                    print("✅ Content Verification: Passed (Topic found)")
                else:
                    print("❌ Content Verification: Failed (Topic missing)")
        else:
            print("❌ File Creation: Failed")
            
    except Exception as e:
        print(f"❌ Pipeline Error: {e}")

if __name__ == "__main__":
    test_pipeline()