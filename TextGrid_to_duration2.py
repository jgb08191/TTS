import os
import json
import glob
import textgrid
from tqdm import tqdm

# 설정
TEXTGRID_DIR = r"C:\Users\win\Desktop\aligned_output_val"
WAV_BASE_DIR = r"C:\Users\win\Desktop\데이터\011.한국어 아동 음성 데이터\01.데이터\2.Validation\원천데이터\kor_formatted"
OUTPUT_JSON_PATH = "val_duration.json"
HOP_LENGTH = 256
SAMPLING_RATE = 22050
FRAME_DURATION_SEC = HOP_LENGTH / SAMPLING_RATE  # 약 0.0116초

# .wav 파일 사전 구축 (속도 향상)
wav_map = {}
for root, _, files in os.walk(WAV_BASE_DIR):
    for file in files:
        if file.endswith(".wav"):
            fname = os.path.splitext(file)[0]
            wav_map[fname] = os.path.join(root, file)

output_data = []

for tg_path in tqdm(glob.glob(os.path.join(TEXTGRID_DIR, "**", "*.TextGrid"), recursive=True)):
    try:
        tg = textgrid.TextGrid.fromFile(tg_path)
        phones = []
        durations = []

        phone_tier = next(t for t in tg.tiers if "phone" in t.name.lower())

        for interval in phone_tier:
            phone = interval.mark.strip()
            if phone in ["", "spn"]:  # 무음, 잡음 제외
                continue
            duration_sec = interval.maxTime - interval.minTime
            duration = int(round(duration_sec / FRAME_DURATION_SEC))
            phones.append(phone)
            durations.append(duration)

        filename = os.path.splitext(os.path.basename(tg_path))[0]
        audio_path = wav_map.get(filename)

        if not audio_path:
            print(f"[경고] {filename}.wav 경로를 찾을 수 없습니다.")
            continue

        output_data.append({
            "text": filename,  # 실제 문장은 별도로 추가 필요
            "phonemes": phones,
            "durations": durations,
            "audio_filepath": audio_path.replace("\\", "/")
        })

    except Exception as e:
        print(f"[에러] {tg_path} 처리 중 오류 발생: {e}")
        continue

# JSONL 저장
with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
    for item in output_data:
        json.dump(item, f, ensure_ascii=False)
        f.write("\n")

print(f"[완료] {len(output_data)}개 항목이 {OUTPUT_JSON_PATH}에 저장되었습니다.")
