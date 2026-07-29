import json

# Đọc file JSON hiện tại
with open('7.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Lấy template từ object đầu tiên
template = data[0]

# Tạo list mới để lưu tất cả các tài khoản
new_data = []

# Tạo các tài khoản từ luongclone001 đến luongclone999
for i in range(541, 541+90):
    account = json.loads(json.dumps(template))  # Deep copy
    account['TaiKhoan'] = f'luongclone{i:03d}'  # luongclone001, luongclone001, ..., luongclone999
    new_data.append(account)

# Tạo các tài khoản từ luongclone1000 đến luongclone10000
for i in range(1171, 1171+90):
    account = json.loads(json.dumps(template))  # Deep copy
    account['TaiKhoan'] = f'luongclone{i}'  # luongclone1000, luongclone1001, ..., luongclone10000
    new_data.append(account)

# Ghi lại vào file JSON
with open('7.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)

print(f"✓ Hoàn thành! Đã tạo {len(new_data)} tài khoản")
print(f"  - luongclone001 đến luongclone999 (90 tài khoản)")
print(f"  - luongclone1000 đến luongclone10000 (90 tài khoản)")
