import csv
import os
import logging


def import_csv(path_name):
    try:
        with open(path_name, encoding='utf-8') as csv_file:
            if path_name.endswith('.csv'):
                file_name = os.path.basename(path_name)
                book_name = file_name[:-4]
            else:
                book_name = os.path.basename(path_name)

            reader = csv.DictReader(csv_file)

            highlight_jsons = []
            for row in reader:
                highlight_json = {
                    "text": row['劃線內容'],
                    "title": book_name,
                    "source_type": "book",
                    "highlighted_at": row['劃線時間']
                }
                if row['註記']:
                    highlight_json["note"] = row['註記']

                highlight_jsons.append(highlight_json)

            return highlight_jsons
    except Exception as ex:
        logging.error('Error importing highlights to Readwise: ' + ex)
