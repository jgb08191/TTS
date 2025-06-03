import os
import json

json_dir = "C:/your/path/to/jsons"       # 🔁 여기에 JSON 폴더 경로 입력
output_dir = "C:/your/path/to/labs"      # 🔁 .lab 파일 저장할 폴더

os.makedirs(output_dir, exist_ok=True)

for fname in os.listdir(json_dir):
    if fname.endswith(".json"):
        json_path = os.path.join(json_dir, fname)

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        try:
            label = data["Transcription"]["LabelText"]
            wav_name = data["File"]["FileName"]  # 예: E00011844-AMG33.wav
            base_name = os.path.splitext(wav_name)[0]  # 확장자 제거

            lab_path = os.path.join(output_dir, base_name + ".lab")

            with open(lab_path, "w", encoding="utf-8") as f:
                f.write(label.strip() + "\n")

            print(f"✅ {base_name}.lab 생성 완료")

        except KeyError:
            print(f"⚠️ {fname}: 필요한 key가 없음")
