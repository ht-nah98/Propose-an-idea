# Từ bán giờ công sang bán sản phẩm

Slide cho buổi họp định hướng Team Tech (30/10/2026): team Tech góp vào doanh thu thế nào — lợi thế của công ty
và đội ngũ, đề xuất **nội dung số có nhân vật** và **âm nhạc trong thiết bị**.

Trang tĩnh, không framework, không npm: `slides/*.html` → `build.py` → `index.html`. Deploy thẳng lên Vercel.

## Xem

```bash
python3 -m http.server 8797     # rồi mở http://localhost:8797
```

| phím | việc |
|---|---|
| ← → · Space · vuốt (điện thoại) · bấm nửa trái/phải | chuyển slide |
| N | ghi chú người nói |
| F | toàn màn hình |
| O | tổng quan, bấm để nhảy tới slide |
| Home / End | slide đầu / cuối |

Video tự phát (tắt tiếng) khi vào slide, dừng khi rời slide; bấm vào video để bật tiếng hoặc tua.
Link tới slide cụ thể: `.../#10`.

## Sửa nội dung

1. Sửa `slides/<id>.html` — mỗi file là một `<section>`; lời nói nằm trong `<aside>` (hiện khi bấm N).
2. Thứ tự slide: mảng `order` trong `deck.json`. Thêm slide = tạo file mới + thêm id vào `order`.
3. `python3 build.py` → ghi lại `index.html`.
4. `python3 tools/check.py` → kiểm tra index.html đã build, mọi ảnh/video tồn tại, file không quá nặng.

Kiểu dáng chung (màu, cỡ chữ, `.card`, `.stat`, `.pill`, `.src`…) nằm trong `PAGE` ở `build.py`. Khung slide 1920×1080,
tự co theo màn hình. Lớp `dark` cho slide nền tối, `fill` cho khối cần giãn hết chiều cao còn lại.

**Luôn commit cả `index.html`** — Vercel không chạy build, nó phục vụ đúng file đã commit.

## Cấu trúc

```
index.html        trang đã build (Vercel phục vụ file này)
build.py          ghép slide + CSS + JS trình chiếu
deck.json         tiêu đề, mô tả, thứ tự slide
slides/           25 slide nguồn
media/            ảnh + video đã nén (720p H.264, faststart) — ~37 MB
tools/check.py    kiểm tra trước khi push
docs/NGUON.md     nguồn và cách lấy từng số liệu, từng tư liệu
vercel.json       header cache cho media/, noindex
.vercelignore     chỉ đẩy index.html + media/ + robots.txt lên CDN
```

## Deploy lên Vercel

```bash
python3 build.py && python3 tools/check.py
git add -A && git commit -m "Cập nhật slide"
git push
```

Lần đầu:

1. Tạo repo **Private** trên GitHub, rồi `git remote add origin <url>` và `git push -u origin main`.
2. vercel.com → **Add New… → Project** → chọn repo → Framework Preset: **Other** → để trống Build/Output → **Deploy**.
3. Mỗi lần push lên `main` Vercel tự deploy lại.

Hoặc dùng CLI: `npx vercel` (preview) / `npx vercel --prod`.

### Riêng tư

Deck chứa định hướng nội bộ và tư liệu của bên thứ ba (clip, ảnh chụp kênh) dùng để bình luận trong cuộc họp.

- Repo GitHub để **Private**.
- Trang đã gắn `noindex` (meta + header + `robots.txt`) nên không lên Google, nhưng **ai có link vẫn xem được**.
- Muốn khoá bằng mật khẩu: Vercel → Project → Settings → **Deployment Protection** (Vercel Authentication cho
  thành viên team, hoặc Password Protection ở gói Pro). Đừng chia sẻ link production công khai.

## Thêm / thay video

```bash
ffmpeg -t 60 -i nguon.mp4 -vf scale=-2:720 -c:v libx264 -preset slow -crf 29 -pix_fmt yuv420p \
  -c:a aac -b:a 96k -movflags +faststart media/ten-moi.mp4
ffmpeg -ss 5 -i media/ten-moi.mp4 -frames:v 1 -q:v 3 media/ten-moi.jpg   # ảnh poster
```

Tên file không dấu, không khoảng trắng (Vercel phân biệt hoa/thường). Trong slide:
`<video src="media/ten-moi.mp4" poster="media/ten-moi.jpg" data-auto controls playsinline>` — bỏ `data-auto` nếu
không muốn tự phát.
