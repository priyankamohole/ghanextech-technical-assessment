
import fitz
from langchain_core.documents import Document


def extract_pdf(uploaded_file):
    documents = []

    try:
        pdf_bytes = uploaded_file.getvalue()
        pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

        if pdf.needs_pass:
            raise ValueError("Password-protected PDFs are not supported.")

        if len(pdf) == 0:
            raise ValueError("The PDF contains no pages.")

        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text("text").strip()

            if text:
                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source": uploaded_file.name,
                            "page": page_number
                        }
                    )
                )

        pdf.close()

        if not documents:
            raise ValueError(
                "No readable text found. This may be a scanned PDF. "
                "OCR is required to process it."
            )

        return documents

    except ValueError:
        raise

    except Exception as e:
        raise ValueError(f"Unable to process PDF: {str(e)}")
