# File Combiner
Have you ever tried combining PDF's or PPT's online but hated the experience , well now you can do it from your own terminal!!!!

## Installation:
To set this up clone this repo , switch into the cloned folder and execute the following commands:
        pip install .

## How to use:
To combine files execute the command in this format:
        concat [input file paths] [output file path]

## Here are some example commands:
        concat "Copy of Club Deck_20230913_133732_0000.pptx" "1. Lecture-1-Unit 1 (1).pptx" sample.pdf
        Here "Copy of Club Deck_20230913_133732_0000.pptx" and "1. Lecture-1-Unit 1 (1).pptx" are input paths and sample.pdf is output file

## Another example:
        concat "D:\python projects\file_concat\1. Lecture-1-Unit 1 (1).pptx" "D:\python projects\file_concat\Team_16_Cieloquest.pptx" se.pdf

**Note**
The output can only be a pdf file 
The input file can be a simple name if its in the same directory or can be the whole path included in quotations