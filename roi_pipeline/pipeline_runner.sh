#!/bin/bash
# ROI Extraction Pipeline Runner

INPUT="roi_pipeline/raw_research_data.txt"
OUTPUT="roi_pipeline/roi_metrics_extracted.csv"

echo "🚀 [Pipeline] 데이터 추출 프로세스를 시작합니다..."
python3 roi_pipeline/extraction_engine.py "$INPUT" "$OUTPUT"

if [ -f "$OUTPUT" ]; then
    echo "📊 [Pipeline] 결과 확인:"
    column -s, -t < "$OUTPUT"
else
    echo "❌ [Pipeline] 오류: 결과 파일이 생성되지 않았습니다."
    exit 1
fi

echo "🏁 [Pipeline] 모든 작업이 완료되었습니다."