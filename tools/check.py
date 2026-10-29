"""Kiểm tra trước khi push / deploy:
- index.html đã build lại sau lần sửa slide/deck.json cuối cùng
- mọi src/poster trong index.html trỏ tới file có thật (đúng hoa/thường — Vercel phân biệt)
- không file media nào vượt giới hạn (GitHub cảnh báo > 50 MB, chặn > 100 MB)
python3 tools/check.py  → in OK hoặc liệt kê lỗi, exit 1 nếu lỗi"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIMIT_MB = 50


def main():
    errs = []
    index = ROOT / 'index.html'
    if not index.exists():
        sys.exit('Chưa có index.html — chạy: python3 build.py')
    sources = [*(ROOT / 'slides').glob('*.html'), ROOT / 'deck.json', ROOT / 'build.py']
    newest = max(sources, key=lambda p: p.stat().st_mtime)
    if newest.stat().st_mtime > index.stat().st_mtime:
        errs.append(f'index.html cũ hơn {newest.relative_to(ROOT)} — chạy: python3 build.py')

    html = index.read_text()
    refs = set(re.findall(r'(?:src|poster)="((?!https?:|data:)[^"]+)"', html))
    files = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
    for ref in sorted(refs):
        if ref not in files:
            errs.append(f'thiếu file (hoặc sai hoa/thường): {ref}')

    for p in (ROOT / 'media').iterdir():
        mb = p.stat().st_size / 1e6
        if mb > LIMIT_MB:
            errs.append(f'{p.name} nặng {mb:.0f} MB > {LIMIT_MB} MB')
        if ' ' in p.name or not p.name.isascii():
            errs.append(f'tên file nên không dấu, không khoảng trắng: {p.name}')

    total = sum(p.stat().st_size for p in (ROOT / 'media').iterdir()) / 1e6
    if errs:
        print('\n'.join('✗ ' + e for e in errs))
        sys.exit(1)
    print(f'OK · {len(refs)} file media được tham chiếu · media/ tổng {total:.1f} MB')


if __name__ == '__main__':
    main()
