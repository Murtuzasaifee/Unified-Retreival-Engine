from typing import Any

from pydantic import BaseModel, Field


class DocumentChunk(BaseModel):
    """
    Chunk of document with metadata
    """
    text: str = Field(..., description="The chunk text")
    chunk_index: int = Field(..., description="Sequential index")
    token_count: int = Field(..., description="Actual token count")
    start_char: int = Field(..., description="Starting character position")
    end_char: int = Field(..., description="Ending character position")
    headings: list[str] = Field(..., description="List of hierarchical headings")
    page_numbers: list[int] = Field(..., description="List of page numbers")
    doc_items: list[Any] = Field(..., description="References to original document items")
    captions: list[str] = Field(..., description="Table/figure captions")
