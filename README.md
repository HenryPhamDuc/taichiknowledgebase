# Tai Chi Knowledge Base

Một kiến thức toàn diện về Thái Cực Quyền — từ nền tảng đến tinh hoa.

A comprehensive Tai Chi knowledge base — from foundation to elite.

## Structure | Cấu Trúc

```
docs/
├── index.md                    # Home page
├── en/                         # English content
│   ├── foundation/
│   │   ├── index.md
│   │   ├── basics/
│   │   └── deep-dives/
│   ├── advanced/
│   │   ├── index.md
│   │   ├── basics/
│   │   └── deep-dives/
│   └── elite/
│       ├── index.md
│       ├── basics/
│       └── deep-dives/
├── vi/                         # Vietnamese content (Tiếng Việt)
│   ├── foundation/
│   │   ├── index.md
│   │   ├── basics/
│   │   └── deep-dives/
│   ├── advanced/
│   │   ├── index.md
│   │   ├── basics/
│   │   └── deep-dives/
│   └── elite/
│       ├── index.md
│       ├── basics/
│       └── deep-dives/
└── _lexicon/
    └── taichi-en-vi.md        # Terminology reference
```

## Levels | Cấp Độ

- **Foundation** | Nền Tảng: Core basics — stance, posture, weight transfer, breathing
- **Advanced** | Cao Cấp: Intermediate work — energy flow, timing, application  
- **Elite** | Tinh Hoa: Master level — fajin, silk reeling, internal mechanics

## Bilingual Navigation

- English: `/en/foundation/basics/index.md`
- Vietnamese: `/vi/foundation/basics/index.md`

## Building Locally

```bash
# Install mkdocs and material theme
pip install mkdocs mkdocs-material

# Build and serve
mkdocs serve

# Build for deployment
mkdocs build
```

## Deployment

Uses worktree pattern for GitHub Pages (avoids `mkdocs gh-deploy` timeout):

```bash
# 1. Build site
mkdocs build

# 2. Robocopy to worktree (Windows paths required)
robocopy site C:\path\to\worktree /E /XF ".git"

# 3. Commit in worktree
cd C:\path\to\worktree
git add .
git commit -m "Update site"
git push --force origin gh-pages
```

## Video Sources

Content drawn from:
- Peter Chen — Beginner instruction
- Master Song Kung Fu — Yang style fundamentals
- TRUNG TÂM HOA TỬ — Vietnamese instruction
- Chen Xiaowang — Chen style fajin
- Open the Door to Tai Chi — 10 Essentials
- Selfnature Tai Chi — Yang Cheng Fu principles

## License

Educational content for Tai Chi practitioners.

---

**English version:** [README above](#tai-chi-knowledge-base)  
**Vietnamese version:** [Bản tiếng Việt](#tai-chi-knowledge-base-1)

---

# Thái Cực Quyền Kiến Thức

Một tài liệu kiến thức toàn diện về Thái Cực Quyền — từ nền tảng đến tinh hoa.

## Cấu Trúc

Xem cây thư mục ở trên.

## Cấp Độ

- **Nền Tảng**: Những nguyên tắc cơ bản — trụ, tư thế, chuyển trọng lượng, hít thở
- **Cao Cấp**: Công việc trung cấp — dòng năng lượng, thời gian, ứng dụng
- **Tinh Hoa**: Cấp bậc thầy — phát kình, cuốn tơ, cơ chế nội tại

## Điều Hướng song Ngữ

- Tiếng Anh: `/en/foundation/basics/index.md`
- Tiếng Việt: `/vi/foundation/basics/index.md`

## Xây Dựng Cục Bộ

```bash
# Cài đặt mkdocs và theme material
pip install mkdocs mkdocs-material

# Xây dựng và phục vụ
mkdocs serve

# Xây dựng để triển khai
mkdocs build
```

## Triển Khai

Sử dụng mẫu worktree cho GitHub Pages (tránh timeout `mkdocs gh-deploy`):

```bash
# 1. Xây dựng trang
mkdocs build

# 2. Robocopy vào worktree (yêu cầu đường dẫn Windows)
robocopy site C:\path\to\worktree /E /XF ".git"

# 3. Commit trong worktree
cd C:\path\to\worktree
git add .
git commit -m "Cập nhật trang"
git push --force origin gh-pages
```

## Nguồn Video

Nội dung rút ra từ:
- Peter Chen — Hướng dẫn cho người mới
- Master Song Kung Fu — Nguyên tắc Dương phái
- TRUNG TÂM HOA TỬ — Hướng dẫn tiếng Việt
- Trần Tiểu Vương — Phát kình Trần phái
- Open the Door to Tai Chi — 10 Nguyên Tắc Thiết Yếu
- Selfnature Tai Chi — Nguyên tắc Dương Trừng Phủ

## Giấy Phép

Nội dung giáo dục cho võ sinh Thái Cực Quyền.

---

**Phiên bản tiếng Anh:** [English README](#tai-chi-knowledge-base)  
**Phiên bản tiếng Việt:** [Bản tiếng Việt ở trên](#thái-cực-quyền-kiến-thức)