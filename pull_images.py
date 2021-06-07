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
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].getData()
                #for i in xObject[obj]:
                #    print(f"{i} : {xObject[obj][i]}")
                print(f"")
                print(f"{data}")
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "P"
                    #mode = "CMYK"
                    #mode = 'RGB'

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

# 2  Could potentially work, but the below is for jpg only.  Not sure what the startmark and endmark are for non jpg images
#import sys
#
#pdf = open(sys.argv[1], "rb").read()
#with open('testfile.out', 'wb') as writefile:
#    writefile.write(pdf)
#
#startmark = "\xff\xd8"
#startfix = 0
#endmark = "\xff\xd9"
#endfix = 2
#i = 0
#
#njpg = 0
#while True:
#    #istream = pdf.find("stream", i)
#    istream = pdf.find(str.encode("stream"), i)
#    if istream < 0:
#        break
#    istart = pdf.find(str.encode(startmark), istream, istream+20)
#    if istart < 0:
#        i = istream+20
#        continue
#    iend = pdf.find("endstream", istart)
#    if iend < 0:
#        raise Exception("Didn't find end of stream!")
#    iend = pdf.find(endmark, iend-20)
#    if iend < 0:
#        raise Exception("Didn't find end of JPG!")
#    
#    istart += startfix
#    iend += endfix
#    print(f"JPG {njpg} from {istart} to {iend}")
#    jpg = pdf[istart:iend]
#    filename = 'jpg'+njpg+'.jgp'
#    #jpgfile = file("jpg%d.jpg" % njpg, "wb")
#    jpgfile = open(filename,  "wb")
#    jpgfile.write(jpg)
#    jpgfile.close()
#    
#    njpg += 1
#    i = iend

# 3
import PyPDF2
import struct
