import os
import json
from textgrid import TextGrid

# 설정
textgrid_dir = "mfa_output"  # MFA 결과 폴더
output_dir = "alignment_json"  # 변환된 JSON 저장 위치
sample_rate = 16000
hop_length = 256  # FastPitch 기본값

os.makedirs(output_dir, exist_ok=True)

for fname in os.listdir(textgrid_dir):
    if not fname.endswith(".TextGrid"):
        continue

    base = os.path.splitext(fname)[0]
    tg_path = os.path.join(textgrid_dir, fname)
    tg = TextGrid.fromFile(tg_path)

    try:
        phones = tg.getFirst("phones")
    except:
        print(f"❌ {fname}: 'phones' tier 없음")
        continue

    phonemes = []
    durations = []

    for interval in phones:
        phone = interval.mark.strip()
        if phone == "":  # 공백은 무시
            continue

        start = interval.minTime
        end = interval.maxTime
        duration_sec = end - start
        duration_frames = round(duration_sec * sample_rate / hop_length)

        phonemes.append(phone)
        durations.append(duration_frames)

    # 저장
    output = {
        "phonemes": phonemes,
        "durations": durations
    }

    with open(os.path.join(output_dir, base + ".json"), "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✅ {base}.json 저장 완료")
