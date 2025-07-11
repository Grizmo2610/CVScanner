import os
from pathlib import Path
import fitz  # PyMuPDF
from google.genai import Client
from utils.utils import reading_key
from typing import Union

class GeminiModel:
    """
    A wrapper class for interacting with the Gemini API to generate content and summaries.
    """

    def __init__(self, model: str = 'gemini-2.5-flash', key_path: Union[str, None] = None) -> None:
        """
        Initialize the GeminiModel with API key and model.

        Args:
            model (str): The model name to use (e.g., 'gemini-2.5-flash').
            key_path (str | None): Optional path to the API key file. 
                                   If None or invalid, the key will be read from the GOOGLE_API_KEY environment variable.

        Raises:
            ValueError: If the API key cannot be found or loaded.
        """
        self.__model: str = model
        try:
            path = Path(key_path) if key_path else None
            if key_path is None or not path.is_file():
                self.__key: str = os.environ["GOOGLE_API_KEY"]
            else:
                self.__key: str = reading_key(key_path)
        except Exception:
            raise ValueError("Gemini Key not found!")

        self.__client: Client = Client(api_key=self.__key)

    def set_key(self, key: str) -> None:
        """
        Update the API key.

        Args:
            key (str): The new API key to use.
        """
        self.__key = key
        self.__client = Client(api_key=self.__key)

    def set_model(self, model: str = "gemini-2.5-flash") -> None:
        """
        Change the Gemini model.

        Args:
            model (str): The new model name to use.
        """
        self.__model = model

    def response(self, text: str, config: str = '') -> str:
        """
        Send a prompt to the Gemini API and receive a response.

        Args:
            text (str): The input text content.
            config (str): Optional custom prompt to prepend to the text.

        Returns:
            str: The generated output from the model.

        Raises:
            ValueError: If the API key is missing.
        """
        if not self.__key:
            raise ValueError("Gemini Key not found in environment.")

        content: str = f"{config}:\n{text}"
        response = self.__client.models.generate_content(
            model=self.__model, contents=content
        )
        return response.text.strip()

    def summary(self, text: str, lang: str, limit: int = 200) -> str:
        """
        Generate a summarized version of the given text using Gemini.

        Args:
            text (str): The full input content to summarize.
            lang (str): Language of the summary output (e.g., 'eng', 'vie').
            limit (int): Approximate word limit for the summary.

        Returns:
            str: The summarized text.
        """
        prompt: str = (
            f"Please, summarize this CV content in about {limit} word in {lang}. "
            f"Only summary, no introduction, no questions. "
            f"Highlight special skill and result."
        )
        return self.response(text, prompt)


class PDFReader:
    """
    A class to read and summarize text content from PDF files using GeminiModel.
    """

    def __init__(self, source: str, gemini_key_path: str = 'private/gemini.key') -> None:
        """
        Initialize the PDFReader with the given PDF file and optional API key.

        Args:
            source (str): Path to the PDF file.
            gemini_key_path (str): Path to the Gemini API key file.
        """
        self.content: list[dict[str, Union[int, str]]] = []
        path: Path = Path(source)

        if path.is_file() and path.suffix.lower() == ".pdf":
            self.doc: fitz.Document = fitz.open(path)
            for i, page in enumerate(self.doc):
                text: str = page.get_text().replace('\n', '\n\n\n')
                self.content.append({"page": i + 1, "content": text})

        self.__ai: GeminiModel = GeminiModel(key_path=gemini_key_path)

    def get_content(self, page: Union[int, None] = None) -> Union[str, dict[str, Union[int, str]]]:
        """
        Retrieve the content of a specific page or the entire document.

        Args:
            page (int | None): The 1-based index of the page to extract. If None, return the whole document.

        Returns:
            str | dict: The full text content or a dictionary containing a single page's content.
        """
        if page is None or not isinstance(page, int):
            full_text: str = ""
            for text in self.content:
                full_text += text['content'] + '\n\n===============\n\n\n'
            return full_text
        else:
            return self.content[page - 1]

    def summary(self, lang: str, limit: Union[int, str] = "No limit") -> str:
        """
        Generate a summary of the document using Gemini.

        Args:
            lang (str): Language of the summary (e.g., 'eng', 'vie').
            limit (int | str): Word limit for the summary. Use "No limit" to remove restriction.

        Returns:
            str: The summarized text.
        """
        return self.__ai.summary(self.get_content(), lang, limit)

    def set_key(self, key: str) -> None:
        """
        Set or update the Gemini API key.

        Args:
            key (str): A new API key.
        """
        self.__ai.set_key(key)
