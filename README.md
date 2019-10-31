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

