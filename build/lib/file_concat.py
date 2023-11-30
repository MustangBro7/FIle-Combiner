import os
import PyPDF2
import click
from pptx import Presentation
import comtypes.client
import ppt2pdf
import sys
def convert(input_path):
    # print(input_path)
    output = os.path.splitext(input_path)
    output1 = os.path.abspath(output[0] + ".pdf")
    input_path = os.path.abspath(output[0] + ".pptx")
    ppt = comtypes.client.CreateObject("PowerPoint.Application")
    # print(input_path)
    
    presentaion = ppt.Presentations.Open(input_path)
    
    presentaion.SaveAs(output1, 32)
    presentaion.Close()


@click.command()
@click.argument("filenames", nargs=-1)
def concat(filenames):

    dest_file_path = filenames[-1]
    with open(dest_file_path , "wb") as dest_file:
        merger = PyPDF2.PdfMerger()
        # print(filenames[-1])
        for i in filenames[0:-1]:
            print(i)
            name , ext = os.path.splitext(i)
            # print(ext , name)
            if ext  == ".ppt" or ext == '.pptx':
                # script_dir = os.path.dirname(os.path.abspath(__file__))
                # pptx_path = os.path.join(script_dir, name+ext)
                pptx_path = os.path.abspath(i)
                # print(pptx_path)
                convert(pptx_path)
                output1 = name + ".pdf"
                # print(output1)
                with open(output1,"rb") as file2:
                    merger.append(output1)
            else:
                with open(i,"rb") as file1:
                    merger.append(i)
        merger.write(dest_file)
        merger.close()
if __name__ == "__main__":
    concat()



# script_dir = os.path.dirname(os.path.abspath(__file__))
# pptx_path = os.path.join(script_dir, "Team_16_Cieloquest.pptx")
# pdf_path = os.path.join(script_dir, "dummy.pdf")
# pres1 = "Team_16_Cieloquest.pptx"
# pres2 = Presentation('Team_16_Cieloquest.pptx')

# merged_pres = Presentation()

# ppt = comtypes.client.CreateObject("PowerPoint.Application")
# presentaion = ppt.Presentations.Open(pptx_path)
# presentaion.ExportAsFixedFormat(r"dummy.pdf" , 2)

# presentaion.Close()
# ppt.Quit()\



# script_dir = os.path.dirname(os.path.abspath(__file__))
# pptx_path = os.path.join(script_dir, ".\Team_16_Cieloquest.pptx")
# convert(pptx_path)
# for i in sys.argv:
    
#     print(os.path.abspath(i))