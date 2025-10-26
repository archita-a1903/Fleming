from pydantic import BaseModel, Field
from typing import List, Optional, Any

class StartTriageRequest(BaseModel):
    complaint: str

class AnswerTriageRequest(BaseModel):
    triage_id: str
    answer: Any

class FinishTriageRequest(BaseModel):
    triage_id: str

class TriageTurn(BaseModel):
    triage_id: str
    question: Optional[str] = None
    options: Optional[List[str]] = None
    warnings: Optional[List[str]] = None
    interim_advice: Optional[str] = None
    done: bool = False
    final_advice: Optional[str] = None
    acuity: Optional[str] = None
    citations: Optional[List[str]] = None

class DoctorOut(BaseModel):
    id: str
    name: str
    degree: Optional[str] = None
    specialties: Optional[List[str]] = None
    years_experience: Optional[int] = None
    workplace: Optional[str] = None
    languages: Optional[List[str]] = None
    fee_cents: Optional[int] = None
    is_free: bool = False
    timezone: str
    verified: bool = False
    doctor_score: float = Field(default=4.5)

class ReferenceIn(BaseModel):
    complaint: str
    source: str
    body: str
    version: Optional[str] = None

class ReferenceOut(BaseModel):
    id: str
    complaint: str
    source: str
    body: str
    version: Optional[str] = None
