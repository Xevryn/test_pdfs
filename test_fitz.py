# apt-get install mupdf
# apt-get install libmupdf-dev # Fixes : fatal error: fitz.h: No such file or directory 
# sudo apt-get install libfreetype6-dev # Fixes : fatal error: ft2build.h: No such file or directory
# sudo apt-get install mupdf-tools # Testing fix : Block of warnings warning: ‘jm_tracedraw_clip_path’ defined but not used [-Wunused-function]
# pip install PyMuPDF


# https://stackabuse.com/working-with-pdfs-in-python-reading-and-splitting-pages
import fitz

pdf_document = 'balsamic-glazed-pork-chops-608c0c893880cd71414ad1fa-d132ae7b.pdf' 

page = 0

for image in pdf_document.getPageImageList(page):
    xref = image[0]
    pix = fitz.Pixmap(pdf_document, xref)
    if pix.n < 5: # This is GRAY or RGB
        filename = f"page{current_page}-{xref}.png"
        pix.writePNG(filename)
    else:
        pix1 = fitz.Pixmap(fitz.csRGB, pix)
        filename = f"page{current_page}-{xref}.png"
        pix1.writePNG(filename)
        pix1 = None
    pix = None
