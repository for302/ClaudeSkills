"""
PDF to PNG Splitter
PDF 파일을 페이지별 PNG 이미지로 분리합니다.

Usage:
    python split_pdf.py <pdf_path> [output_dir]

Example:
    python split_pdf.py document.pdf
    python split_pdf.py document.pdf ./pages
"""

import sys
from pathlib import Path

try:
    import pypdfium2 as pdfium
except ImportError:
    print("Error: pypdfium2 is not installed.")
    print("Please install it with: pip install pypdfium2")
    sys.exit(1)


def split_pdf_to_images(pdf_path, output_dir=None, scale=2.0):
    """PDF를 페이지별 PNG 이미지로 분리

    Args:
        pdf_path: PDF 파일 경로
        output_dir: 출력 디렉토리 (기본값: PDF파일명_pages)
        scale: 이미지 스케일 (기본값: 2.0, 해상도 조절)

    Returns:
        생성된 이미지 파일 경로 리스트
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    # 출력 디렉토리 설정
    if output_dir is None:
        output_dir = pdf_path.parent / f"{pdf_path.stem}_pages"
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    # PDF 열기
    pdf = pdfium.PdfDocument(pdf_path)
    total_pages = len(pdf)
    print(f"Total pages: {total_pages}")

    image_paths = []

    for page_num in range(total_pages):
        page = pdf[page_num]

        # 페이지를 이미지로 렌더링
        bitmap = page.render(scale=scale)
        pil_image = bitmap.to_pil()

        # 파일명: page_01.png, page_02.png, ...
        image_filename = f"page_{page_num + 1:02d}.png"
        image_path = output_dir / image_filename

        pil_image.save(image_path)
        image_paths.append(str(image_path))

        print(f"  Saved: {image_filename}")

    pdf.close()

    print(f"\nAll {total_pages} pages saved to: {output_dir}")
    return image_paths


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        result = split_pdf_to_images(pdf_path, output_dir)
        print(f"\nSplit complete: {len(result)} images created")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing PDF: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
