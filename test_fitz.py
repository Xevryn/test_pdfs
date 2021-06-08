# pip install pymupdf

# https://stackabuse.com/working-with-pdfs-in-python-reading-and-splitting-pages
import fitz
import sys

pdf_document = 'balsamic-glazed-pork-chops-608c0c893880cd71414ad1fa-d132ae7b.pdf' 

doc = fitz.open(pdf_document)
# print(f"number of pages: {doc.pageCount}")
# print(f"{doc.metadata}")

page1 = doc.loadPage(0)
page1text = page1.getText("text")
# print(f"{page1text}")

for current_page in range(len(doc)):
	for image in doc.getPageImageList(current_page):
		xref = image[0]
		pix = fitz.Pixmap(doc, xref)
		if pix.width > 1000:
			if pix.n == 4:
				# Greyscale - 1 or 2 bytes per pixel
				# RGB - 3 bytes per pixel
				# CMYK - 4 bytes per pixel (Convert to RGB)
				pix = fitz.Pixmap(fitz.csRGB, pix)
			pix.writePNG("page%s-%s.png" % (current_page, xref))
			pix = None
