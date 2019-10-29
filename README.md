## PDF2IDML

![Version](https://img.shields.io/badge/beta-0.0.1-orange)
![Download](https://img.shields.io/badge/download-0-blue)
![License](https://img.shields.io/badge/license-GNU%203.0-green)

This project aims to translate the data/information from PDF to Indesign formate (IDML) by Python. The data/information includes text, images, layouts and styles. 

Currently, it just starts with this big idea, has not got any code yet. A project road map / structure will be described following to show the complete process of how to construct this program, and will build each component step by step after.

## Introduction

PDF is the most popular format to record and present documents, Indesign is the most popular software to edit and layout the document. However, there is only one way transformation from Indesign to PDF, but not the other from PDF to Indesign. 

There are several solutions on the market, but not ideal or free. 
- [[PDF2ID](https://www.recosoft.com/products/pdf2id/)]: A commercial software that can import PDF into Indesign.  
- [[PDF2DTP](https://markzware.com/products/pdf2dtp/)]: Similar to PDF2ID. The biggist different is PDF2DTP parse the text to paragraph, while PDF2ID parse the text into single line.  

## Big Idea

The general concept is that using current python library to parse pdf to text, image, layout, and style data, then using these data to rebuild the idml file that Indesign can 
