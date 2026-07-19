# Unity Game Automation

Tool này tự động nhận quà cho nhiều tài khoản trong game Unity. Tool chỉ chạy
trên **Windows** vì cần điều khiển cửa sổ game bằng DirectInput.

## Cài đặt bằng Miniconda

Mở **Anaconda Prompt** hoặc Command Prompt trên Windows, chuyển đến thư mục dự án,
rồi chạy:

```bash
conda create -n tool-nso python=3.11
conda activate tool-nso
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> `conda create -n tool-nso python=3.11` tạo môi trường. Sau đó mới dùng
> `conda activate tool-nso` để kích hoạt nó.

## Chuẩn bị

1. Mở `account.csv` và điền các tài khoản theo định dạng:

   ```csv
   username,password
   tai_khoan_1,mat_khau_1
   tai_khoan_2,mat_khau_2
   ```

2. Mở game thủ công, đăng nhập đến màn hình phù hợp với bước đầu tiên và để cửa
   sổ game hiển thị, không bị che khuất.
3. Kiểm tra các ảnh mẫu trong thư mục `imgs/` khớp với giao diện game hiện tại.

## Chạy

Mỗi lần chạy, kích hoạt môi trường trước:

```bash
conda activate tool-nso
cd duong-dan-den/auto-game-nso
python main.py
```

Phím tắt:

- `F7`: in tọa độ chuột hiện tại `(x, y)` ra terminal. Đưa chuột lên nút trong
  game rồi bấm `F7`; dùng tọa độ đó cho biến `FORCE_*` tương ứng.
- `F8`: tạm dừng / tiếp tục.
- `Esc`: dừng tool an toàn.

## Lấy tọa độ chuột

Để lấy point cho `FORCE_*`, chạy script riêng sau trên Windows:

```bash
conda activate tool-nso
python capture_mouse_position.py
```

Mỗi lần bấm chuột trái, tọa độ màn hình sẽ được in ra terminal và lưu vào
`logs/mouse_positions.log`. Nhấn `Ctrl+C` để dừng. Ví dụ `(960, 540)` có thể
được đặt thành `FORCE_LOGIN = (960, 540)` trong `actions/login.py`.

## Cấu hình và xử lý lỗi

- Đặt `DEBUG = True` trong `config.py` để hiện màn hình preview cùng khung xanh
  tại vị trí ảnh được tìm thấy.
- Nếu game chưa nhận username hoặc password, tăng `INPUT_FIELD_FOCUS_WAIT` (mặc
  định `0.75` giây) trong `config.py`.
- Tool mặc định nhập bằng từng phím DirectInput (`TEXT_INPUT_METHOD = "direct"`),
  phù hợp hơn với nhiều ô nhập Unity. Nếu game của bạn nhận được `Ctrl+V` tốt hơn,
  có thể đổi thành `TEXT_INPUT_METHOD = "clipboard"`.
- Tốc độ gõ được chỉnh bằng `TEXT_TYPING_INTERVAL_SECONDS` (mặc định `0.01`
  giây/ký tự). Nếu game bị thiếu ký tự, tăng lên `0.03` hoặc `0.05`.
- Mặc định `TEXT_CLEAR_METHOD = "right_backspace"`: tool gửi phím `Right` đủ
  `MAX_LEN_USER` lần để đưa con trỏ về cuối, sau đó gửi `Backspace` cùng số lần
  để xóa tài khoản cũ. Cách này không dùng `Ctrl+A` hay `Home`. Tăng
  `MAX_LEN_USER` nếu username/password có thể dài hơn 64 ký tự.
- Toàn bộ tọa độ click nằm trong `config.py`. Đặt giá trị, ví dụ
  `FORCE_LOGIN = (x, y)`, để click tọa độ cố định thay vì tìm ảnh; đặt `None`
  để chỉ thao tác đó quay lại tìm ảnh bằng OpenCV.
- Khi không tìm thấy ảnh hoặc xảy ra lỗi, tool dừng và lưu screenshot vào thư mục
  `logs/` để kiểm tra.
