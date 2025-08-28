# VISION
### **Mini-Project: Object-Detection & Tracking with fallen, standing human**

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
