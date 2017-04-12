from Tkinter import *
import Tkinter as tk
import tkMessageBox
import xml.etree.cElementTree as ET
from datetime import datetime
import re
import hashlib
import os
import time
import shutil
import sys
import time
import tkFileDialog
global log
import io
log = ""

i = datetime.now()
datestd = i.strftime('%m/%d/%y %H:%M %p')
def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
master = Tk()
cwgt=Canvas(master)
cwgt.pack(expand=YES, fill=BOTH)
image1=PhotoImage(file="VelaLogo.gif")

cwgt.img=image1
cwgt.create_image(800, 300,image=image1, anchor=W)
cwgt.configure(background='white')
assay = tk.StringVar(cwgt)
assay.set('Choose Assay')
choices = ["Oncology","Virology"]
option = tk.OptionMenu(cwgt, assay, *choices)
option.grid(row=0, column=5, sticky=S, pady=2)

panel = tk.StringVar(cwgt)
panel.set('Choose Assay')
panel_choices = ['Sentosa_SQ_Melanoma_Panel','Sentosa_SQ_NSCLC_Panel','Sentosa_SQ_CRC_Panel','Sentosa_SQ_Thyroid_Panel','Sentosa_SQ_Leukemia_Panel','Sentosa_SQ_HCV_Genotyping_Assay','Sentosa_SQ_HIV_Genotyping_Assay']
option1 = tk.OptionMenu(cwgt,panel, *panel_choices)
option1.configure(width=30)
option1.grid(row=0, column=9, columnspan=20,sticky=S, pady=2)
master.wm_title("Sentosa NGS Worklist generator Beta 1")

Label(cwgt, text="Run Name No duplicates, special characters or spaces allowed: ").grid(row=0)
Label(cwgt, text="Sample1 SC:").grid(row=1)
Label(cwgt, text="Sample2: ").grid(row=2)
Label(cwgt, text="Sample3: ").grid(row=3)
Label(cwgt, text="Sample4: ").grid(row=4)
Label(cwgt, text="Sample5: ").grid(row=5)
Label(cwgt, text="Sample6: ").grid(row=6)
Label(cwgt, text="Sample7: ").grid(row=7)
Label(cwgt, text="Sample8: ").grid(row=8)
Label(cwgt, text="Sample9: ").grid(row=9)
Label(cwgt, text="Sample10: ").grid(row=10)
Label(cwgt, text="Sample11: ").grid(row=11)
Label(cwgt, text="Sample12: ").grid(row=12)
Label(cwgt, text="Sample13: ").grid(row=13)
Label(cwgt, text="Sample14: ").grid(row=14)
Label(cwgt, text="Sample15: ").grid(row=15)
Label(cwgt, text="Sample16: ").grid(row=16)
Label(cwgt, text="Barcode Label: ").grid(row=3,column=8)
Label(cwgt, text="Library Kit: ").grid(row=1,column=8)
Label(cwgt, text="Extraction Kit: ").grid(row=2,column=8)
Label(cwgt, text="This tool is only meant for use when an error occurs during worklist creation or hardware error \n For Technical support please contact veladx US Support \n for Software support contact Ahmed Mahmoud at Ahmed.Mahmoud@veladx.com").grid(row=200,column=0, sticky=S )
Label(cwgt, text="Assay Name:").grid(row=0,column=8)
ename = Entry(cwgt)
e1 = Entry(cwgt)
e2 = Entry(cwgt)
e3 = Entry(cwgt)
e4 = Entry(cwgt)
e5 = Entry(cwgt)
e6 = Entry(cwgt)
e7 = Entry(cwgt)
e8 = Entry(cwgt)
e9 = Entry(cwgt)
e10 = Entry(cwgt)
e11 = Entry(cwgt)
e12 = Entry(cwgt)
e13 = Entry(cwgt)
e14 = Entry(cwgt)
e15 = Entry(cwgt)
e16 = Entry(cwgt)
ebar = Entry(cwgt)
eLib = Entry(cwgt, width=30)
eExt = Entry(cwgt, width=30)

ename.grid(row=0, column=1)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=9, column=1)
e10.grid(row=10, column=1)
e11.grid(row=11, column=1)
e12.grid(row=12, column=1)
e13.grid(row=13, column=1)
e14.grid(row=14, column=1)
e15.grid(row=15, column=1)
e16.grid(row=16, column=1)
ebar.grid(row=3, column=9)
eLib.grid(row=1, column=9,columnspan=10,sticky=W+E+N+S)
eExt.grid(row=2, column=9)
global default
default = ""
global lists
lists = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
global cksum
cksum = " "
def sel():
    selection = "Current Mode: " + str(var.get())
    label.config(text = selection)
var = IntVar()
label = Label(cwgt)
label.grid(row=6,column=8)
R1 = Radiobutton(cwgt, text="1:SUITE", variable=var, value=1,
                  command=sel)
R1.grid(row=4,column=8)

R2 = Radiobutton(cwgt, text="2:LINK + SUITE", variable=var, value=2,
                  command=sel)
R2.grid(row=5,column=8)

def quit_script():
   master.destroy()
   sys.exit()
def config(infile,row,row2,types):
    conf=open(infile, "r+")
    default = conf.readline()
    yes = Label(cwgt, text="Current " + types + " Path was "+ default).grid(row=row,column=0)
    dirname = tkFileDialog.askdirectory(parent=cwgt,initialdir='//', title='Please select the SQ Suite tmp/location')
    if dirname == "":
        dirname = "NONE" 
        conf=open(infile, "r+")
        conf.write(dirname)
        conf.truncate
        conf.close()
        conf=open(infile, "r")
        default = conf.readline()
        yes = Label(cwgt, text="Current " + types + " is now "+ default).grid(row=row2,column=0)
    else:
        open(infile, 'w').writelines(default[1])      
        conf=open(infile, "r+")
        conf.write(dirname)
        conf.truncate
        conf.close()
        conf=open(infile, "r")
        default = conf.readline()
        yes = Label(cwgt, text="Current " + types + " is now "+ default).grid(row=row2,column=0)
def configsuite():
   config("CONF.txt",25,26,"SQ Suite")
def configxml():
   config("CONFXML.txt",27,28,".xml Directory")

   
#----------------------------------------------------------------------------------------#

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

#----------------------------------------------------------------------------------------#
def remove_space(xml):
    out = re.sub(r'>\s+<', '><', xml)
    return out

#----------------------------------------------------------------------------------------#
def rm_spc_bin_add_cksum(xml):
        with open(xml) as fin:
            lines = fin.readlines()
            lines[0] = lines[0].replace('UTF-8', 'utf-8')
            lines[0] = lines[0].replace("'", '"')
        with open(xml, 'w') as fout:
            for line in lines:
                fout.write(line)
        im_file = xml + '.tmp'
        with io.open(xml, encoding='utf-8-sig', errors='ignore') as source:
            with io.open(im_file, mode='w', encoding='utf-8') as target:
                shutil.copyfileobj(source, target)
        with open(im_file) as f1:
            xml_content = ''.join(line.strip() for line in f1)
        checksum = find_between(str(xml_content), "<Checksum>", "</Checksum>")
        checksum_field = "<Checksum>" + checksum + "</Checksum>"
        #print checksum_field
        chs_xml_content = xml_content.replace(checksum_field, '')

        new_xml_content = remove_space(chs_xml_content)

        with open(im_file + '.tmp1', "w") as f2:
            f2.write(new_xml_content)

        with open(im_file + '.tmp1') as f:
            with open(im_file + '.tmp', 'w') as out:
                out.write(f.read().strip())


        hasher = hashlib.sha256()
        with open(im_file + '.tmp1', 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
            hashsum = (hasher.hexdigest())
            print hashsum
        with open(xml) as final:
            xml_content = ''.join(line.strip() for line in final)
        checksum = find_between(str(xml_content), "<Checksum>", "</Checksum>")
        checksum_field_replaced = "<Checksum>" + checksum + "</Checksum>"
        checksum_field_final = "<Checksum>" + hashsum + "</Checksum>"
       #print checksum_field
        chs_xml_content = xml_content.replace(checksum_field, checksum_field_final )
        with open(xml, "w") as final1:
            final1.write(chs_xml_content)
        os.remove(im_file)
        os.remove(im_file + '.tmp')
        os.remove( im_file + '.tmp1')
def xmlgenerate():
    conf=open('CONF.txt', 'r+')
    default = conf.readline()
    print default
    root = ET.Element("ID_List")
    assays = ET.SubElement(root, "Assay").text = panel.get()
    ListID = ET.SubElement(root, "ListID").text = ebar.get()
    PlannedRun = ET.SubElement(root, "PlannedRunName").text = ename.get()
    ListType = ET.SubElement(root, "ListType").text = "Result" #remains static
    CreationDate = ET.SubElement(root, "CreationDate").text =  datestd
    BarcodeSet = ET.SubElement(root, "BarcodeSet").text =  "Sentosa SQ Barcode Set"
    Checksum = ET.SubElement(root,"Checksum").text = "placeholder"
    Samples = ET.SubElement(root,"Samples")
    def loop(revolutions):
        cycle = 0
        bc = 1
        while (cycle < revolutions):
            Sample = ET.SubElement(Samples,"Sample")
            ET.SubElement(Sample,"Attrbute",{"Name":"SampleID","Value":((lists[(cycle)]).get())})
            ET.SubElement(Sample,"Attrbute",{"Name":"BarcodeID","Value":"SentosaBC-"+ str(bc)})
            ET.SubElement(Sample,"Attrbute",{"Name":"TestID","Value":panel.get()})
            ET.SubElement(Sample,"Attrbute",{"Name":"ExtractionKit","Value":eExt.get()})
            ET.SubElement(Sample,"Attrbute",{"Name":"Library Kit","Value":eLib.get()})
            ET.SubElement(Sample,"Attrbute",{"Name":"SentosaSX","Value":"5075CK502161"})
            cycle = cycle + 1
            bc = bc + 1

    if assay.get() == "Virology":
        loop(16)
    elif assay.get() == "Oncology":
        loop(8)

    tree = ET.ElementTree(root)
    tree.write(default + "/" + ename.get() + ".xml", encoding="UTF-8")
    im_file_tmp = (default +"/" + PlannedRun + ".xml")
    infile = im_file_tmp
    rm_spc_bin_add_cksum(im_file_tmp)
    
    print ename.get()
    print str(var.get())
    if str(var.get()) == "2":
            print "TRUE"
            main = ET.Element("PatientList")
            PlannedRunName = ET.SubElement(main, "PlannedRunName").text = ename.get()
            CreationDate = ET.SubElement(main, "CreationDate").text =  datestd
            Checksum = ET.SubElement(main,"Checksum").text = "placeholder"
            OperatorID = ET.SubElement(main,"OperatorID").text = " "
            OperatorName = ET.SubElement(main,"OperatorName").text = " "
            HospitalID = ET.SubElement(main,"HospitalID").text = " "
            Notes = ET.SubElement(main,"Notes").text = " "
            Samples = ET.SubElement(main,"Samples")
   #----------------------------------------------------------------------------------------#
            def loop(revolutions):
                cycle2 = 0
                bc1 = 1
                while (cycle2 < revolutions):
                    Sample = ET.SubElement(Samples,"Sample")
                    if assay.get() == "Virology" and cycle2 == 16 or assay.get() == "Oncology" and cycle2 == 8 :
                        ID = ET.SubElement(Sample,"ID").text = "24"
                        SampleID = ET.SubElement(Sample,"SampleID").text = ebar.get()
                    else:
                        ID = ET.SubElement(Sample,"ID").text = str(bc1)
                        SampleID = ET.SubElement(Sample,"SampleID").text = ((lists[(cycle2)]).get())
                    TestID = ET.SubElement(Sample,"TestID").text = panel.get()
                    PatientID = ET.SubElement(Sample,"PatientID")
                    if cycle2 == 0:
                        PatientName = ET.SubElement(Sample, "PatientName").text = 'SC'
                    else: PatientName = ET.SubElement(Sample, "PatientName").text = ''
                    Age = ET.SubElement(Sample, "Age")
                    DateBirth = ET.SubElement(Sample, "DateBirth")
                    Gender = ET.SubElement(Sample, "Gender")
                    if cycle2 == 0:
                        SampleType = ET.SubElement(Sample, "SampleType").text = "2"
                    else:
                        SampleType = ET.SubElement(Sample, "SampleType")
                    CollectionDate = ET.SubElement(Sample, "CollectionDate")
                    ReceivedDate = ET.SubElement(Sample, "ReceivedDate")
                    PatientHistory = ET.SubElement(Sample, "PatientHistory")
                    SampleOrigin = ET.SubElement(Sample, "SampleOrigin")
                    TumorCellularirty = ET.SubElement(Sample, "TumorCellularity")
                    DNAQuality = ET.SubElement(Sample, "DNAQuality")
                    Physician = ET.SubElement(Sample, "Physician")
                    cycle2 = cycle2 + 1
                    bc1 = bc1 + 1
                    print cycle2
            print panel.get()
            if assay.get() == "Virology":
                loop(17)
            elif assay.get() == "Oncology":
                loop(9)
            conf=open('CONFXML.txt', 'r+')
            default1 = conf.readline()
            tree1 = ET.ElementTree(main)
            tree1.write(default1 + "/" + ename.get() + "_PL" + ".xml", encoding="UTF-8")
            im_file_tmp1 = (default1 + "/" + PlannedRunName + "_PL" + ".xml")
            print im_file_tmp1
            rm_spc_bin_add_cksum(im_file_tmp1)
def run():
    #try:
        xmlgenerate()
        #tkMessageBox.showinfo("DONE!",  "Your XML has been created and sent to SQ Suite")
    
    #except:
        #tkMessageBox.showerror("There was an error",  "Please try again")
    
        
           
Button(cwgt, text='Quit', command=quit_script).grid(row=21, column=2)
Button(cwgt, text='Create Worklist', command=run).grid(row=21, column=1, sticky=W, pady=4)
Button(cwgt, text='Configuration to SQ Suite', command=configsuite).grid(row=21, column=0, sticky=W, pady=4)
Button(cwgt, text='Configuration to .xml Directory', command=configxml).grid(row=22, column=0, sticky=W, pady=4)
master.minsize(1250,800)
mainloop( )
