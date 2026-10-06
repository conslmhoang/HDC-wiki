# HDC LLM Wiki — Hướng dẫn sử dụng

Wiki tri thức về **High Ductile Concrete (HDC)**. Wiki do LLM (Claude Code) viết và bảo trì,
phục vụ bài literature review.

## Cấu trúc
- `raw/`: bạn bỏ PDF bài báo vào đây. Không sửa file ở thư mục này.
- `wiki/`: các trang do LLM viết. Nên mở thư mục này bằng **Obsidian** để xem graph liên kết.
- `templates/`: mẫu trang.
- `CLAUDE.md`: **schema**, tức bộ quy tắc mà LLM phải tuân theo. Đây là file quan trọng nhất.

## Quy trình làm việc
1. **Thu thập:** tải bài báo về `raw/papers/` và đặt tên theo dạng `Li2001_ECC-micromechanics.pdf`.
2. **Ingest:** mở Claude Code tại thư mục này rồi gõ:
   `ingest raw/papers/Li2001_ECC-micromechanics.pdf`
   Mỗi lần chỉ nạp 1 bài. Đọc báo cáo LLM trả về và kiểm tra các mục trong "To verify".
3. **Hỏi:** ví dụ "So sánh ảnh hưởng của hàm lượng tro bay tới biến dạng kéo". Nếu câu trả lời
   tốt, bảo LLM lưu lại vào `synthesis/`.
4. **Lint:** sau khoảng 5–10 bài thì gõ `lint` để rà soát mâu thuẫn và khoảng trống nghiên cứu.
5. **Viết review:** gõ `draft chapter 4` (theo `wiki/synthesis/review-outline.md`).

## Gợi ý nguồn nên nạp trước (tự tìm và kiểm chứng)
- Các bài nền tảng của V.C. Li về ECC và micromechanics (khoảng 1992–2003)
- Bài review về ECC/SHCC, có thể tìm trên Scopus hoặc Web of Science
- Các bài HDC của nhóm Deng Mingke (Xi'an Univ. of Architecture & Technology)
- Báo cáo RILEM về SHCC, hướng dẫn JSCE, tiêu chuẩn Trung Quốc về HDC/ECC (nếu có)

Từ khóa tìm kiếm: `"high ductile concrete"`, `"high ductility concrete"`,
`"engineered cementitious composites"`, `"strain hardening cementitious composites"`,
`PVA fiber tensile strain hardening`.

## Lưu ý
LLM có thể ghi sai số liệu. Mọi con số dùng trong bài review đều phải đối chiếu lại với PDF gốc
(trang source luôn ghi vị trí Table/Fig để kiểm tra nhanh).
