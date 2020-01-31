## PDF2IDML

![Version](https://img.shields.io/badge/beta-0.0.1-orange)
![Download](https://img.shields.io/badge/download-2-blue)
![License](https://img.shields.io/badge/license-GNU%203.0-green)

This project aims to translate the data/information from PDF to Indesign formate (IDML) by Python. The data/information includes text, images, layouts and styles. 

Currently, it just starts with this big idea, has not got any code yet. A project road map / structure will be described following to show the complete process of how to construct this program, and will build each component step by step after.

## Introduction

PDF is the most popular format to record and present documents, Indesign is the most popular software to edit and layout the document. However, there is only one way transformation from Indesign to PDF, but not the other from PDF to Indesign. 

There are several solutions on the market, but not ideal or free. 
- [[PDF2ID](https://www.recosoft.com/products/pdf2id/)]: A commercial software that can import PDF into Indesign.  
- [[PDF2DTP](https://markzware.com/products/pdf2dtp/)]: Similar to PDF2ID. The biggist different is PDF2DTP parse the text to paragraph, while PDF2ID parse the text into single line.  

IDML (*InDesign Markup Language*) files are a Zip archives (Adobe calls them packages) storing essentially XML files. Adobe made a descent job because those files can completely express the content of the native (binary) documents. It is a potential format that could be translated and modified easily from other formats (PDF, PPT, EPUB, ...)

## Big Idea

The general concept is that using current python library to parse pdf to text, image, layout, and style data, then using these data to rebuild the idml file that Indesign can read and edit. Within the general concept, there are two roads can go:

- __PDF -> XML -> IDML__: Since the idml file is basically a bunch of xml file compressed together, it is make-sense that first convert the pdf to a xml, then reorganize it to the structure that idml requiring. 
- __PDF -> Raw Data (Images, text, layout, and styles in SQL or Json formate) -> IDML__:  It is also feasible that extracting all the raw data temporary to a place. Then adding the data to the idml template.

## Road Map / Components

1. **PDF Parser**: Research and explore the potential PDF parser library in Python, test with different types of PDF samples.
2. **Middleware**: Research the best way to store the data extracted from PDF parser. They potentially include XML, SQL, and JSON.
3. **XML Constructor**: Base on the data format and idml file structure, a constructor or compiler has to be built to import the data into idml template properly.
4. **IDML Compiler**: The last step is to compress these XML files and converted to standard IDML file.



## Reference Projects

- [[SimpleIDML]](https://github.com/Starou/SimpleIDML): SimpleIDML is a Python library to manipulate Adobe® InDesign® IDML file. The main purpose being the ability to compose IDML files together and produce complex documents from simple pieces and to separate the data from the structure.

  The philosophy behind SimpleIDML is to keep separated the content and the structure and to use XML files to feed your documents by using the XML Structure in InDesign. Keeping this isolation is important to ease the debugging and to keep track of what is going on.

- [[pdfminer]](https://github.com/euske/pdfminer/): PDFMiner is a tool for extracting information from PDF documents. Unlike other PDF-related tools, it focuses entirely on getting and analyzing text data. PDFMiner allows one to obtain the exact location of text in a page, as well as other information such as fonts or lines. It includes a PDF converter that can transform PDF files into other text formats (such as HTML). It has an extensible PDF parser that can be used for other purposes than text analysis.

- [[PyPDF2]](https://github.com/mstamy2/PyPDF2): PyPDF2 could extract images from PDF with other decoding library.

- [[PyMuPDF]](https://github.com/pymupdf/PyMuPDF): PyMuPDF could be used to extract images and fonts from PDF. PNG is the image format that PyMuPDF export to.

- [[minecart]](https://github.com/felipeochoa/minecart): minecart is a Python package that simplifies the extraction of text, images, and shapes from a PDF document. It provides a very Pythonic interface to extract positioning, color, and font metadata for all of the objects in the PDF.

- [[slate]](https://github.com/timClicks/slate): Slate is a Python package that simplifies the process of extracting text from PDF files. It depends on the PDFMiner package. (No layout information converted)



## Revisions

#### Beta 0.0.1 - 10/22/2019

Start README.md, add badge icons.

#### Beta 0.0.2 - 10/30/2019

Complete README.md with chapters: big idea, road map, and reference projects.

#### Beta 0.0.3 - 11/11/2019

Read and test about [[pdfminer]](https://github.com/euske/pdfminer/) library. Check different typologies of pdf and their output results. 

The pdfminer seems only working with text in PDF. It has different formats to export with different information attached. Text format basically only include content of text; HTML did a good job to maintain the format and layout of the text; XML did the same work as HTML. However, it composed each character of the words into an individual unit of format and layout. The one information of the PDF missing for pdfminer is the size of the pages.

Since the HTML is the more ideal exported format to maintain the integraty and accuracy of the PDF text. The next step is to convert the html into indesign format / idml. Several relevent projects were found below.

- [[ickmull]](https://code.google.com/archive/p/ickmull/): Converts XHTML to IDML/ICML. -- *No layout information, No font, one text box*
- [[jaumeortola/ickmull]](https://github.com/jaumeortola/ickmull/tree/ickmull/ickmull): github version of ickmull
- [[Tutorial on .icml]](https://vishmili.wordpress.com/papers-on-publishing/ickmull/): A blog tutors how to convert html by using ickmull.
- [[Pandoc]](https://pandoc.org/): A universal document converter that could convert html to icml -- *Successfully convert html to icml; the icml is invalid and can not be opened in inDesign or inCopy; no layout information in icml; export to xml, only text, no layout*
- [[Id-extras]](https://www.id-extras.com/html-import-script/): An InDesign HTML Import Script. -- *Can only import the contents online; can only import into one text box; no font, layout, style information*

#### Beta 0.0.4 - 11/27/2019

Test the 4 methods above, all of them are failed to convert html to icml/idml with layout, style information. Going to test other PDF parsers: 

- [[PyPDF2]](https://github.com/mstamy2/PyPDF2): Tried pdf-image-extractor.py, no working.
- [[PyMuPDF]](https://github.com/pymupdf/PyMuPDF): The export result is similar to [[pdfminer]](https://github.com/euske/pdfminer/). HTML is still the best export format including most complete information. It also include images comparing to pdfminer. XML is the second ideal format, however, it format each character of the text instead of a paragraph. And XML has no image information either.
- [[minecart]](https://github.com/felipeochoa/minecart): Coding running error since the wrong pdfminer library using.

Since there is no ideal direct solution so far, the next step would deep down the pdfminer library and SimpleIDML library to extract and convert the raw data instead of indirectly converting to other formats.

#### Beta 0.0.5 - 12/3/2019

Check the [[SimpleIDML]](https://pypi.org/project/SimpleIDML/) document and test it on a project example. SimpleIDML has basic functions of parsing and reading IDML files, extracting contents and structures of an IDML, inserting elements to IDML, merging multiple IDML together, converting different formats related to IDML. 

However, SimpleIDML does not have ability to compose new elements from raw data. What we need first step is to writing a composer that can format the raw data into the element that SimpleIDML can directly add or insert. Before this, we need to study about the standard structure of IDML. [[IDML Specification]](https://wwwimages.adobe.com/content/dam/acom/en/devnet/indesign/sdk/cs6/idml/idml-specification.pdf)

#### Beta 0.0.6 - 1/24/2020

SimpleIDML can not edit layout and text style, which are essential information to create an IDML file. Need to go back to origin, and check the official document about InDesign Scripting. [InDesign Scripting Tutorial](https://www.adobe.com/content/dam/acom/en/devnet/indesign/sdk/cs6/scripting/InDesign_ScriptingTutorial.pdf). 

#### Beta 0.0.7 - 1/29/2020

It is possible to write an InDesign plugin to extract the data from pdf and compose an InDesign file. InDesign Script supports multiple programming languages. However, JavaScript would be the most modern and popular language to script InDesign Plugin. Through reading the [[Adobe InDesign CS6 JavaScript Scripting Guide]](https://www.adobe.com/content/dam/acom/en/devnet/indesign/sdk/cs6/scripting/InDesign_ScriptingGuide_JS.pdf), it seems promising to compose an InDesign file through JavaScript programming, and control all the editable contents inside the InDesign. The major problem would be that how to extract information from PDF? 

PPT is another popular document format that has similar file structure with .idml. You can change the .pptx  suffix to .zip suffix, then unzip it to a folder. The uncompressed contents include all the media data(images, sounds, videos) and .xml which descript the slides, layouts, texts, and shapes. It seems possible to extract the complete information including pages, layouts, contents, images, from the uncompressed .pptx file. It may be easier to start with PPT instead of PDF. 

[[ExtendScript Toolkit]](https://www.adobe.com/devnet/scripting/estk.html) would be the tool to programming InDesign Plugin through JavaScript. It contains all the available InDesign Object Model and descriptions. 














