import re
import csv
import os

class ROIExtractionEngine:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        # 정규표현식 패턴: 비정형 텍스트 내의 특정 키워드 기반 추출
        self.pattern = re.compile(
            r"Industry:\s*(?P<industry>.*?)\n"
            r"Process:\s*(?P<process>.*?)\n"
            r"Metric:\s*(?P<metric>.*?)\n"
            r"Pre-AI:\s*(?P<pre_ai>.*?)\n"
            r"Post-AI:\s*(?P<post_ai>.*?)\n"
            r"Improvement:\s*(?P<improvement>.*?)\n"
            r"Source:\s*(?P<source>.*)",
            re.MULTILINE
        )

    def parse(self):
        if not os.path.exists(self.input_scale): # 오타 수정 필요 (self.input_file)
            pass 

    def run(self):
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        matches = []
        for match in self.pattern.finditer(content):
            matches.append(match.groupdict())

        if not matches:
            print("❌ 추출된 데이터가 없습니다. 패턴을 확인하세요.")
            return

        keys = matches[0].keys()
        with open(self.output_file, 'w', encoding='utf-8', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(matches)
        
        print(f"✅ 성공: {len(matches)}개의 데이터가 {self.output_file}에 저장되었습니다.")
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        matches = []
        for match in self.pattern.finditer(content):
            matches.append(match.groupdict())

        if not matches:
            print("❌ 추출된 데이터가 없습니다. 패턴을 확인하세요.")
            return

        keys = matches[0].keys()
        with open(self.output_file, 'w', encoding='utf-8', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(matches)
        
        print(f"✅ 성공: {len(matches)}개의 데이터가 {self.output_file}에 저장되었습니다.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python extraction_engine.py <input_txt> <output_csv>")
    else:
        engine = ROIExtractionEngine(sys.argv[1], sys.argv[2])
        engine.run