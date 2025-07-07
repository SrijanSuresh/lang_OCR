# 🌐 Real-Time Translation OCR System

A sophisticated real-time screen capture and translation system that performs OCR (Optical Character Recognition) and instant translation overlay on live video feeds. Built with Python, OpenCV, and modern web technologies.

![Demo](https://github.com/user-attachments/assets/bc771635-8a8a-4db2-8761-3ca33fdb5f04)

##  Features

### Core Functionality
- **Real-time Screen Capture** - Live monitoring of any monitor or custom region
- **Multi-language OCR** - Support for English and Japanese text recognition
- **Instant Translation** - Japanese to English translation using Hugging Face models
- **Live Video Feed** - Web-based interface with real-time streaming
- **Professional UI** - Modern dark theme with sidebar controls

### Advanced Features
- **Multi-Monitor Support** - Select from available monitors dynamically
- **Custom Region Capture** - Define specific screen areas for focused translation
- **Visual Indicators** - Red border overlay to show active capture areas
- **Performance Monitoring** - Real-time FPS and statistics tracking
- **Responsive Design** - Works seamlessly on desktop and mobile devices

## 🛠️ Technology Stack

### Backend
- **Python 3.11+** - Core application logic
- **Flask** - Web server and API endpoints
- **OpenCV** - Computer vision and image processing
- **EasyOCR** - Multi-language text recognition
- **Transformers (Hugging Face)** - Neural machine translation
- **MSS** - High-performance screen capture
- **NumPy** - Numerical computing

### Frontend
- **HTML5/CSS3** - Modern responsive interface
- **JavaScript (ES6+)** - Real-time updates and controls
- **WebSocket-like polling** - Live video streaming
- **CSS Grid/Flexbox** - Professional layout system

### AI/ML Components
- **EasyOCR** - Pre-trained OCR models for text detection
- **Helsinki-NLP/opus-mt-ja-en** - Japanese to English translation model
- **Real-time inference** - Sub-second translation processing

##  Prerequisites

- Python 3.11 (due to sentencepiece compatibility)
- NVIDIA GPU (optional, for CUDA acceleration)
- Windows 10/11 (tested on Windows 10.0.26100)

## Installation
- NOTE: My suggestion would be to use uv with pip to speed up the process
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/lang_OCR.git
   cd lang_OCR
   ```

2. **Create virtual environment**
   ```bash
   uv python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python web_app.py
   ```

5. **Access the interface**
   ```
   http://localhost:5000
   ```

##  Usage

### Basic Operation
1. **Select Monitor** - Choose from available displays
2. **Configure Region** - Set custom capture area (optional)
3. **Start Capture** - Begin real-time translation
4. **Monitor Feed** - Watch live translations overlay

### Advanced Configuration
- **Custom Resolution** - Define specific screen coordinates
- **Border Toggle** - Show/hide capture area indicators
- **Performance Settings** - Adjust frame rate and quality

##  Performance Metrics

- **Real-time Processing** - 10 FPS average
- **OCR Accuracy** - High precision text detection
- **Translation Speed** - Sub-second response time
- **Memory Usage** - Optimized for continuous operation
- **CPU Utilization** - Efficient background processing

## 🏗️ Architecture

### System Components
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Screen        │    │   OCR Engine    │    │   Translation   │
│   Capture       │───▶│   (EasyOCR)     │───▶│   (HuggingFace) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Server    │    │   Image         │    │   Overlay       │
│   (Flask)       │    │   Processing    │    │   Generation    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐
│   Web Interface │
│   (Real-time)   │
└─────────────────┘
```

### Key Features
- **Modular Design** - Separated concerns for maintainability
- **Thread-safe Operations** - Background processing without UI blocking
- **Error Handling** - Robust error recovery and logging
- **Scalable Architecture** - Easy to extend with new languages/features

##  Technical Challenges Solved

### 1. Real-time Performance
- **Optimized screen capture** using MSS library
- **Efficient image processing** with OpenCV
- **Background threading** for non-blocking UI

### 2. Multi-language Support
- **EasyOCR integration** for robust text detection
- **Hugging Face transformers** for accurate translation
- **Extensible language pipeline** for future additions

### 3. Web-based Interface
- **Real-time video streaming** via base64 encoding
- **Responsive design** for multiple screen sizes
- **Professional UI/UX** with modern styling

### 4. System Compatibility
- **Python version management** (3.11 compatibility)
- **Dependency resolution** (sentencepiece/cmake issues)
- **Cross-platform considerations** (Windows focus)

##  UI/UX Design

### Professional Features
- **Dark theme** for reduced eye strain
- **Sidebar layout** for organized controls
- **Real-time statistics** and performance metrics
- **Smooth animations** and transitions
- **Mobile-responsive** design

### User Experience
- **Intuitive controls** for monitor selection
- **Visual feedback** for active capture areas
- **Real-time status** updates and error handling
- **Professional styling** throughout the interface

## Future Enhancements

### Planned Features
- **Additional Languages** - Support for Korean, Chinese, Spanish
- **GPU Acceleration** - CUDA support for faster processing
- **Cloud Integration** - Remote translation services
- **API Development** - RESTful endpoints for external integration
- **Mobile App** - Native mobile application

### Technical Improvements
- **WebSocket Implementation** - True real-time communication
- **Database Integration** - Translation history and caching
- **Machine Learning** - Custom OCR model training
- **Performance Optimization** - Reduced latency and improved FPS

## Business Applications

### Use Cases
- **International Business** - Real-time document translation
- **Educational Technology** - Language learning tools
- **Accessibility** - Screen reader enhancement
- **Content Creation** - Multi-language video production
- **Customer Support** - Real-time communication assistance

### Market Potential
- **Global Market** - Multi-language support demand
- **Remote Work** - International collaboration tools
- **E-learning** - Language education platforms
- **Enterprise** - Business communication solutions

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Srijan Suresh**
- GitHub: [@SrijanSuresh](https://github.com/SrijanSuresh)
- LinkedIn: [Srijan](https://linkedin.com/in/srijan-suresh)
- Email: srijansuresh04@gmail.com

## Acknowledgments

- **EasyOCR** - For robust text recognition capabilities
- **Hugging Face** - For pre-trained translation models
- **OpenCV** - For computer vision and image processing
- **Flask** - For web framework and API development

---
 **Star this repository if you find it useful!**
