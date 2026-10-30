# Nguồn tư liệu và số liệu

Số liệu mạng xã hội thay đổi hằng ngày; tất cả đọc ngày **29/10/2026**. Cập nhật lại trước khi trình bày nếu cách xa ngày này.

| slide | tư liệu | file | cách lấy |
|---|---|---|---|
| trust | Aprilynne Alter — “Stuck in The YouTube Dip?” (khung 11:00) | `media/seminar_trust.jpg` | lấy từ deck seminar “Tối ưu YouTube: học từ người giỏi” |
| zavyre | tiktok.com/@zavyre.music | `media/zavyre_profile.jpg` | chụp trang kênh, cắt bỏ thanh bên của tài khoản đang đăng nhập |
| ianfrost | tiktok.com/@ianfrost.music | `media/ianfrost_profile.jpg` | như trên |
| cinek | Reel Facebook của Cinek (facebook.com/share/r/1KPT6UF7vM) | `media/cinek.mp4` | yt-dlp, cắt viền đen |
| techref | “i'm upping my p(doom)” — mexicat; “Video mẫu” | `media/ref_pdoom.mp4`, `media/ref_mau.mp4` | 45 s đầu |
| opuscar | Opuscar 98 — Lemomo · LemoLab, lemomo-ai.github.io/lemo-opuscar/opuscar98 (giấy phép MIT) | `media/opuscar98.mp4` | trích 1:00–1:50 từ bản 1080p trên trang |
| styles | Khung hình Opuscar 98 (phim số 1, 10, 30, 40, 50, 60, 90, 98) | `media/opus_s*.jpg` | ảnh trong `img/opuscar98/` của trang |
| ourmv | MV Add It Up, Exp & Log (repo mascot-mv) | `media/mv_addup.mp4`, `media/mv_explog.mp4` | 60 s đầu |
| duck | Jensen Huang và robot nhỏ tại GTC Berlin (bản phụ đề VN trên Facebook) | `media/nvidia_duck.mp4` | file người dùng tải về |

## Số liệu TikTok

Cuộn hết trang kênh rồi cộng số view hiển thị trên từng ô video. Ngày đăng suy ra từ ID video (`id >> 32` = Unix time).

**Zavyre** — 407,7K follower · 4,6M lượt thích · 119 video (29/06 → 28/10/2026) · tổng ≈ 43,9M view ·
10 video ≥ 1M · cao nhất 4,5M (24/10) và 4,4M (03/09).

**Ian Frost** — 12,2K follower · 221,9K lượt thích · 29 video (14/06 → 27/10/2026) · tổng ≈ 1,82M view.
- 5 video từ 20/10: 954,2K · 304,1K · 252,3K · 57,5K · 47,2K → ≈ 1,62M
- 24 video trước đó: ≈ 0,20M (đa số 4–30K mỗi video)
- Video 954,2K là cảnh khán giả khóc (ghim đầu kênh), các video còn lại là nhân vật mặt nạ trắng.
  Kênh nhỏ, mới 1 tuần → tín hiệu sớm, chưa phải xu hướng bền.

## Lemo-Opuscar

Trang chủ (29/10/2026): 66 phong cách, 11 nhóm, 63 phút phim; Opuscar 98 dài 6:31, “Video model: None”,
làm bằng Claude Opus 5.5 trong Claude Code. Repo github.com/lemomo-ai/lemo-opuscar: MIT, 9.260 sao.

## Số liệu Facebook

**Cinek** — trang hiển thị “1.7M views · 81K reactions”; trường `view_count` yt-dlp trả về 735.621 (có thể chỉ đếm
một nguồn). Trên slide dùng số Facebook hiển thị; nếu bị hỏi, nói “khoảng 1,7 triệu theo Facebook”.

## Cần lưu ý khi trình bày

- Robot trong video là **bản trình diễn** trên sân khấu, chưa có thông tin bán đại trà.
- Clip và ảnh của bên thứ ba chỉ để minh hoạ, bình luận trong họp nội bộ — không đăng lại công khai.
