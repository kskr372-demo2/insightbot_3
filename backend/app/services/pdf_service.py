import fitz


class PDFService:

    def extract_text(self, file_path: str):

        pages = []

        document = fitz.open(file_path)

        for page_number, page in enumerate(document, start=1):

            pages.append(
                {
                    "page": page_number,
                    "text": page.get_text()
                }
            )

        return pages


pdf_service = PDFService()