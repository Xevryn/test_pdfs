# https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python

test_pdf = 'balsamic-glazed-pork-chops-608c0c893880cd71414ad1fa-d132ae7b.pdf'

# 1
import PyPDF4
from PIL import Image

if __name__ == '__main__':
        input1 = PyPDF4.PdfFileReader(open(test_pdf, "rb"))
        page0 = input1.getPage(0)
        xObject = page0['/Resources']['/XObject'].getObject()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                if xObject[obj]['/Width'] > 1000:
                    size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                    data = xObject[obj].getData()
                    for i in xObject[obj]:
                       print(f"{i} : {xObject[obj][i]}")
                    if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                        mode = "RGB"
                    else:
                        mode = "P"

                    if xObject[obj]['/Filter'] == '/FlateDecode':
                        img = Image.frombytes(mode, size, data)
                        img.save(obj[1:] + ".png")
                    elif xObject[obj]['/Filter'] == '/DCTDecode':
                        img = open(obj[1:] + ".jpg", "wb")
                        img.write(data)
                        img.close()
                    elif xObject[obj]['/Filter'] == '/JPXDecode':
                        img = open(obj[1:] + ".jp2", "wb")
                        img.write(data)
                        img.close()


# 3
import PyPDF2
import struct
