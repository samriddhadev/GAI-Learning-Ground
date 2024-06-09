import os
import logging

logger = logging.getLogger(__name__)

def load_unstructured():
    from langchain_community.document_loaders import UnstructuredPDFLoader
    f = os.getenv('SOURCE_FILE')
    logger.info(f"loading file: {f}")
    loader = UnstructuredPDFLoader(f)
    return loader.load()

def load_pymupdf():
    from langchain_community.document_loaders import PyMuPDFLoader
    f = os.getenv('SOURCE_FILE')
    logger.info(f"loading file: {f}")
    loader = PyMuPDFLoader(f)
    return loader.load()