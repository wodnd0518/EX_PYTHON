# PYTHON EXERCISE
### UDEMY
https://www.udemy.com/course/best-100-days-python/
- DAY 32: smtplib(Dealing with e-mails)
- DAY 33: API(Dealing with Json)
- DAY 37: API(POST, PUT, DELETE) - habit tracker

**영어 자막 없이 콘텐츠 보기 챌린지**
: 매일 영어 자막 없이 영상을 보며 꾸준함을 기록해보고자 했습니다.

  ![No English Subtitles Graph](https://pixe.la/v1/users/jay-jay/graphs/graph123)
---
### PROGRAMMERS (for coding test & algorithms)
- Exhaustive Search
- 
---
## MINI PROJECT
### **VISION: Object-Detection & Tracking with fallen, standing human**

### Overall Pipeline
- Model Preparation
   - ROBOWFLOW
      1. Fall-detected: https://universe.roboflow.com/wow-iddfg/fall-stdgq
      2. Normal(Standing): https://universe.roboflow.com/oklahoma-state-university-rcgwk/person-469rx
- Yolov8 + Fine-tuning
- Real-time object track with webcam
  - ```self.model.track(frame, persist=True, device=DEVICE, verbose=False)```
- Fall Monitoring & Alert
- Gradio (Prototype)
