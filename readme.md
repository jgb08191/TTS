# TTS Project

FastPitch + HiFi-GAN을 이용한 구현

## 구성

- FastPitch: 음소, 피치, 길이 기반 mel-spectrogram 생성
- HiFi-GAN: mel → waveform 변환

## 준비 사항

- Python 3.8+
- PyTorch 1.10+
- montreal-forced-aligner (MFA)

## 실행 예시

```bash
python train_fastpitch.py
python train_hifigan.py
