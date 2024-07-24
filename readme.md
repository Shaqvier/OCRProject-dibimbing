# OCRProject-dibimbing
OCR Project for Dibimbing's AI ML class assignment.

The result of text detection and text recognition training can be downloaded [here.](https://drive.google.com/drive/folders/15VBvxgebyiFLmxUpIYMIrh_XzZktBAzn?usp=sharing)

This project is a modification of [octadion's handwritten mmocr.](https://github.com/octadion/handwritten-mmocr.git.)

## Execution
To run this project, do the following steps:

1. Clone this repository
2. Download the models and configs from the link above
3. Update the model paths in `trained_app.py`
4. Run the following command in your terminal in the project directory:
    > pip install -r requirements.txt
5. Run the following command in your terminal:
    > python trained_app.py --input_dir [INPUT_IMAGE_DIRECTORY] --output_dir [OUTPUT_TXT_DIRECTORY]
6. If you encounter a problem, mess around with the configs in mmocr a little (change the paths in the relevant config files)

## Result
The result of this project is as follows:
| Model         | Metric Library | CER  | WER | 
|---------------|----------------|------|-----|
| MMOCR base    | JiWER          | 0.29 | 1.0 |
| MMOCR trained | JiWER          | 0.24 | 1.0 |

## Analysis
From the result above, we can conclude that the MMOCR model trained with handwriting has lower character error rate (CER) than the base model. However, both model has relatively high word error rate (WER).

The steps that could be taken to increase the performance of the model are:

- Add more training data
- Use better, more recognizable handwriting
- Increase the number of epochs used in training