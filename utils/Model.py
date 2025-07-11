import os
from pathlib import Path
import fitz
from google.genai import Client
from utils.utils import *
from typing import Any, Union

class GeminiModel:
    def __init__(self, model: str = 'gemini-2.5-flash', key_path: str= ...) -> None:
        """
        Initialize GeminiModel for interacting with Gemini API.

        Args:
            model (str): Model name to use. Default is 'gemini-2.5-flash'.
            key_path (str | ...): API key. If not provided, it reads from environment variable.
        """
        self.__model: str = model
        try:
            path = Path(key_path) 
            if key_path == ... or path.is_file():
                self.__key: str = os.environ["GOOGLE_API_KEY"]
            else:
                key = reading_key(key_path)
                self.__key: str = key
        except:
            raise ValueError("Gemini Key not found!")
        self.__client: Client = Client(api_key=self.__key)

    def set_key(self, key: str) -> None:
        """Set a new API key."""
        self.__key = key
        self.__client = Client(api_key=self.__key)

    def set_model(self, model: str = "gemini-2.5-flash") -> None:
        """Change the model."""
        self.__model = model

    def respone(self, text: str, config: str = '') -> str:
        """
        Send a prompt and return the response from Gemini.

        Args:
            text (str): Input content.
            config (str): Custom prompt configuration.

        Returns:
            str: Output from the model.
        """
        content = f"{config}:\n{text}"
        response = self.__client.models.generate_content(
            model=self.__model, contents=content
        )
        return response.text.strip()


class PDFReader:
    def __init__(self, source: str, gemini_key_path: str = 'private/gemini.key', lang: str = 'vie') -> None:
        """
        Read and extract text content from a PDF file.

        Args:
            source (str): File path to the PDF.
            gemini_key_path (str): Path to the API key file.
            lang (str): Language for summarization output (e.g. 'vie', 'eng').
        """
        path = Path(source)
        self.content: list[dict[str, Union[int, str]]] = []
        self.language: str = lang

        if path.is_file() and path.suffix.lower() == ".pdf":
            self.doc: fitz.Document = fitz.open(path)
            for i, page in enumerate(self.doc):
                text = page.get_text().replace('\n', '\n\n\n')
                self.content.append({"page": i + 1, "content": text})

        self.__ai: GeminiModel = GeminiModel(key_path=gemini_key_path)

    def get_content(self, page: Union[int, None] = ...) -> Union[str, dict[str, Union[int, str]]]:
        """
        Get the content of a specific page or the entire document.

        Args:
            page (int | ...): Page number to extract. If not specified, returns full document text. Page start from 1

        Returns:
            str | dict: Text content or dictionary with page info.
        """
        if page == ... or not isinstance(page, int):
            content = ""
            for text in self.content:
                content += text['content'] + '\n\n===============\n\n\n'
            return content
        else:
            return self.content[page - 1]

    def summary(self, limit: Union[int, str] = "No limit") -> str:
        """
        Summarize the content of the document using Gemini.

        Args:
            limit (int | str): Word limit for the summary. Use "No limit" for no restriction.

        Returns:
            str: Summarized content.
        """
        prompt = (
            f"Please, summarize this CV content in about {limit} word in {self.language}. "
            f"Only summary, no introduction, no questions."
            f"Highlight special skill and result"
        )
        return self.__ai.respone(self.get_content(), prompt)

    def set_key(self, key: str):
        """
        Set API of Gemini Key model
        
        Args:
            key: Google API Key
        """
        self.__ai.set_key(key)