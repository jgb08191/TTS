import os
import json

# 경로 설정
json_root = r"C:\Users\win\Desktop\데이터\011.한국어 아동 음성 데이터\01.데이터\2.Validation\라벨링데이터\kor_formatted"
wav_root = r"C:\Users\win\Desktop\데이터\011.한국어 아동 음성 데이터\01.데이터\2.Validation\원천데이터\kor_formatted"

count = 0
error_count = 0

for dirpath, _, filenames in os.walk(json_root):
    for fname in filenames:
        if fname.endswith(".json"):
            json_path = os.path.join(dirpath, fname)

            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                label = data["Transcription"]["LabelText"]
                wav_name = data["File"]["FileName"]
                base_name = os.path.splitext(wav_name)[0]

                # 원본 lab 저장할 위치 = 해당 wav 경로
                rel_path = os.path.relpath(json_path, start=json_root)
                rel_dir = os.path.dirname(rel_path)
                wav_dir = os.path.join(wav_root, rel_dir)
                lab_path = os.path.join(wav_dir, base_name + ".lab")

                os.makedirs(wav_dir, exist_ok=True)
                with open(lab_path, "w", encoding="utf-8") as f:
                    f.write(label.strip() + "\n")

                print(f"{lab_path} 생성 완료")
                count += 1

            except Exception as e:
                print(f"오류: {fname} - {e}")
                error_count += 1

print(f"\n📦 완료: lab {count}개 생성, 실패 {error_count}개")
