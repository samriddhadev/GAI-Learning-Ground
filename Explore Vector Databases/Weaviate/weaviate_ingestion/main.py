from dotenv import load_dotenv
load_dotenv()
import logging
import traceback

from weaviate_ingestion.source import load_unstructured, load_pymupdf
from weaviate_ingestion.transform import split_by_char
from weaviate_ingestion.sink import persists

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main():
    try:
        persists(split_by_char(load_pymupdf()))
    except Exception as ex:
        logger.error(f"exception : {str(ex)}")
        traceback.print_exception(ex)

if __name__ == '__main__':
    main()