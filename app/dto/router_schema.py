from typing import Any

from pydantic import BaseModel, Field


class ConfidenceScore(BaseModel):
    sql: float = Field(..., description="SQL confidence score")
    documents: float = Field(..., description="Document confidence score")
    hybrid: float = Field(..., description="Hybrid confidence score")
    
class KeywordMatches(BaseModel):
    sql_keywords: int = Field(..., description="Number of SQL keyword matches")
    document_keywords: int = Field(..., description="Number of document keyword matches")
    hybrid_keywords: int = Field(..., description="Number of hybrid keyword matches")
    
class RouterConfidence(BaseModel):
    """
    Response schema for query routing.
    """
    question: str = Field(..., description="The user's natural language question")
    route: str = Field(..., description="The routing decision")
    confidence_scores: ConfidenceScore = Field(..., description="Confidence scores for each routing option")
    keyword_matches: KeywordMatches = Field(..., description="Keyword matches for each routing option")
    

    

