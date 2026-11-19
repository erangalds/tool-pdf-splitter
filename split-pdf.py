import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter

def split_pdf(input_file: str, parts: int = 3):
    path = Path(input_file)
    if not path.is_file():
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    reader = PdfReader(str(path))
    total_pages = len(reader.pages)
    print(f"Total pages detected: {total_pages}")

    pages_per_part = total_pages // parts

    for i in range(parts):
        writer = PdfWriter()
        start_idx = i * pages_per_part
        # Assign remainder pages to the final part
        end_idx = total_pages if i == parts - 1 else (i + 1) * pages_per_part

        for page_idx in range(start_idx, end_idx):
            writer.add_page(reader.pages[page_idx])

        # Optional lossless compression for stream objects
        for page in writer.pages:
            page.compress_content_streams()

        output_path = path.with_name(f"{path.stem}_part_{i + 1}.pdf")
        with open(output_path, "wb") as f_out:
            writer.write(f_out)

        print(f"Created: {output_path.name} (Pages {start_idx + 1} to {end_idx})")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "large_doc.pdf"
    split_pdf(target, parts=3)