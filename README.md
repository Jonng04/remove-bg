# 🪄 Background Remover - Xóa Nền Ảnh AI

<div align="center">
  
![Background Remover](https://img.shields.io/badge/AI-Background%20Remover-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-green?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.119-teal?style=for-the-badge&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Công cụ xóa nền ảnh tự động sử dụng AI - Nhanh, chính xác, miễn phí**

[Demo](#-demo) • [Tính năng](#-tính-năng) • [Cài đặt](#-cài-đặt) • [Sử dụng](#-sử-dụng) • [API](#-api)

</div>

---

## 📖 Giới thiệu

**Background Remover** là một ứng dụng web hiện đại cho phép xóa nền ảnh tự động bằng công nghệ AI. Được xây dựng với FastAPI và Rembg, công cụ này mang đến trải nghiệm xóa nền ảnh chuyên nghiệp, phù hợp cho:

- 📸 Chỉnh sửa ảnh sản phẩm e-commerce
- ✍️ Xóa nền chữ ký
- 👤 Ảnh profile, avatar
- 🎨 Thiết kế đồ họa
- 📄 Xử lý tài liệu

## ✨ Tính năng

### 🎯 **Core Features**

- ✅ **AI xóa nền tự động** - Sử dụng mô hình U2-Net
- ✅ **Xử lý nhanh** - Chỉ trong vài giây
- ✅ **Không giới hạn** - Xử lý không giới hạn số lượng
- ✅ **Miễn phí 100%** - Hoàn toàn miễn phí

### 🎨 **Giao diện**

- 🖱️ **Drag & Drop** - Kéo thả ảnh dễ dàng
- 👀 **Preview trực tiếp** - Xem ảnh trước khi xử lý
- ⚖️ **So sánh Before/After** - Xem kết quả rõ ràng
- 📱 **Responsive** - Tương thích mọi thiết bị

### 📁 **Xuất đa định dạng**

Hỗ trợ xuất nhiều định dạng ảnh:

- 🖼️ **PNG** - Trong suốt, chất lượng cao
- 📸 **JPG** - Nền trắng, kích thước nhỏ
- 🌐 **WEBP** - Nén tốt, trong suốt
- 🎨 **BMP** - Không nén
- 📐 **SVG** - Vector format
- 🔲 **ICO** - Icon format
- 🖨️ **TIFF** - Chất lượng cao cho in ấn

## 🚀 Demo

### Giao diện chính

<div align="center">
  <img src="https://via.placeholder.com/800x500/f3f4f6/374151?text=Upload+Interface" alt="Upload Interface" width="80%">
</div>

### Kết quả xóa nền

<div align="center">
  <img src="https://via.placeholder.com/800x500/f3f4f6/374151?text=Before+%26+After+Comparison" alt="Result Comparison" width="80%">
</div>

## 🛠️ Công nghệ

<table>
  <tr>
    <td align="center"><b>Backend</b></td>
    <td align="center"><b>Frontend</b></td>
    <td align="center"><b>AI/ML</b></td>
  </tr>
  <tr>
    <td>
      • FastAPI<br>
      • Python 3.12<br>
      • Uvicorn<br>
      • Pillow
    </td>
    <td>
      • HTML5<br>
      • Tailwind CSS<br>
      • JavaScript (ES6+)<br>
      • Canvas API
    </td>
    <td>
      • Rembg<br>
      • U2-Net Model<br>
      • ONNX Runtime<br>
      • NumPy
    </td>
  </tr>
</table>

## ☁️ Deploy lên Render

Hướng dẫn nhanh để deploy trên Render.com (hoặc tương tự Heroku):

1. Đăng nhập vào Render và tạo một **Web Service** mới.
2. Chọn repository `Jonng04/remove-bg` (hoặc push repo của bạn lên GitHub và chọn repo đó).
3. Thiết lập:
  - Branch: `main`
  - Environment: `Python`
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120`

Hoặc bạn có thể cung cấp file `render.yaml` (đã có trong repo) để cấu hình tự động.

### Lưu ý quan trọng
- Model AI (rembg) sẽ tự động tải model khi lần đầu chạy. Model có thể lớn (~tens-hundreds MB) — hãy đảm bảo plan của bạn có đủ băng thông và storage.
- Rembg dùng `onnxruntime` để inference. Để dùng GPU trên Render (nếu có), cài `onnxruntime-gpu` thay vì `onnxruntime`.
- Render Starter (free/cheap) có giới hạn RAM/CPU: nếu xử lý ảnh lớn (>2000px) hoặc nhiều request cùng lúc, cân nhắc nâng plan hoặc dùng worker queue.

### Tối ưu đề nghị cho production
- Resize ảnh trước khi inference (giải pháp nhẹ: giới hạn max dimension 1024px) để giảm RAM và thời gian.
- Sử dụng queue (Redis + worker) nếu dự kiến nhiều request đồng thời.
- Cache kết quả theo hash của file upload để tránh xử lý lại cùng một ảnh.

## 📦 Cài đặt

### Yêu cầu

- Python 3.8 trở lên
- pip (Python package manager)
- 2GB RAM trở lên
- Kết nối internet (lần đầu tải model)

### Bước 1: Clone repository

```bash
git clone https://github.com/Jonng04/remove-bg.git
cd remove-bg
```

### Bước 2: Tạo môi trường ảo (khuyến nghị)

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### Bước 3: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### Bước 4: Chạy ứng dụng

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Ứng dụng sẽ chạy tại: **http://localhost:8000**

## 🎯 Sử dụng

### Web Interface

1. **Truy cập** http://localhost:8000
2. **Upload ảnh** - Click hoặc kéo thả ảnh vào vùng upload
3. **Xóa nền** - Click nút "Xóa nền ảnh"
4. **Chọn định dạng** - Chọn định dạng xuất (PNG, JPG, WEBP,...)
5. **Tải xuống** - Click "Tải xuống" để lưu ảnh

### API Endpoint

#### POST `/remove-bg`

Xóa nền ảnh thông qua API.

**Request:**

```bash
curl -X POST "http://localhost:8000/remove-bg" \
  -F "file=@your-image.jpg" \
  --output result.png
```

**Python Example:**

```python
import requests

url = "http://localhost:8000/remove-bg"
files = {"file": open("input.jpg", "rb")}
response = requests.post(url, files=files)

with open("output.png", "wb") as f:
    f.write(response.content)
```

**Response:**

- Content-Type: `image/png`
- Body: Binary image data (PNG với nền trong suốt)

## 📁 Cấu trúc thư mục

```
remove-bg/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── README.md           # Documentation
├── static/
│   └── index.html      # Frontend UI
└── .venv/              # Virtual environment (generated)
```

## ⚙️ Cấu hình

### Thay đổi port

```bash
uvicorn main:app --port 3000
```

### Chạy production mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🎨 Customization

### Thay đổi model AI

File `main.py` sử dụng model mặc định của rembg. Bạn có thể thay đổi model:

```python
from rembg import remove

# Các model có sẵn: u2net, u2netp, u2net_human_seg, u2net_cloth_seg
result = remove(img, model_name="u2net_human_seg")
```

### Tùy chỉnh giao diện

Chỉnh sửa file `static/index.html` để thay đổi:

- Màu sắc (Tailwind classes)
- Layout
- Text content
- Thêm/bớt định dạng xuất

## 🐛 Troubleshooting

### Lỗi: ModuleNotFoundError: No module named 'onnxruntime'

```bash
pip install onnxruntime
```

### Lỗi: Model download failed

Đảm bảo kết nối internet. Model (~180MB) sẽ tự động tải về lần đầu chạy.

### Ảnh quá lớn, xử lý chậm

Giảm kích thước ảnh trước khi upload hoặc tăng RAM cho server.

## 📊 Performance

| Kích thước ảnh | Thời gian xử lý | RAM sử dụng |
| -------------- | --------------- | ----------- |
| 500x500        | ~1-2s           | ~500MB      |
| 1000x1000      | ~2-3s           | ~800MB      |
| 2000x2000      | ~4-6s           | ~1.2GB      |
| 4000x4000      | ~8-12s          | ~2GB        |

_Thời gian trên CPU Intel i5, 8GB RAM_

## 🤝 Contributing

Contributions, issues và feature requests đều được chào đón!

1. Fork project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

Dự án này được phân phối dưới giấy phép MIT License.

## 👨‍💻 Author

**Phu Thang**

- GitHub: [@Jonng04](https://github.com/Jonng04)
- Project: [remove-bg](https://github.com/Jonng04/remove-bg)

## 🙏 Acknowledgments

- [Rembg](https://github.com/danielgatis/rembg) - AI background removal library
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Tailwind CSS](https://tailwindcss.com/) - UI framework
- [U2-Net](https://github.com/xuebinqin/U-2-Net) - Deep learning model

## 📮 Support

Nếu bạn thấy project này hữu ích, hãy cho một ⭐️!

Có câu hỏi? Tạo [issue](https://github.com/Jonng04/remove-bg/issues) mới.

---

<div align="center">
  
**Made with ❤️ by Phu Thang**

© 2025 Background Remover - All Rights Reserved

</div>
