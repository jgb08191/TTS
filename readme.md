# 🗣️ TTS 프로젝트: FastPitch + HiFi-GAN

이 프로젝트는 **FastPitch**와 **HiFi-GAN**을 결합하여 고품질의 텍스트-투-스피치(TTS) 시스템을 구현합니다.  
**FastPitch**는 음소, 피치, 길이(duration) 정보를 기반으로 mel-spectrogram을 생성하며,  
**HiFi-GAN**은 이를 실제 waveform으로 변환합니다.

git
## 📥 코드 출처

이 프로젝트는 NVIDIA의 FastPitch TTS 모델을 기반으로 합니다.  
원본 저장소: [https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/SpeechSynthesis/FastPitch]

본 프로젝트는 해당 오픈소스 코드를 수정 및 확장하여 사용하였습니다.  
라이선스: Apache License 2.0

---

## 📦 구성 요소

- **FastPitch**  
  : 텍스트, 피치, duration 정보를 입력으로 mel-spectrogram을 생성  
- **HiFi-GAN**  
  : mel-spectrogram을 입력으로 고품질 waveform(음성) 생성

---

## ⚙️ 환경 설정

### 필수 환경

- Python >= 3.8
- PyTorch >= 1.10
- [Montreal Forced Aligner (MFA)](https://montreal-forced-aligner.readthedocs.io/en/latest/) 설치 필요

### MFA 설치

```bash
conda create -n mfa python=3.10
conda activate mfa

conda install -c conda-forge montreal-forced-aligner=2.2.17 openfst=1.8.2 kaldi=5.5.1068

mfa model download acoustic korean_mfa
mfa model download dictionary korean_mfa








