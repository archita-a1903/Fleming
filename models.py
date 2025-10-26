from sqlalchemy import Column, String, Integer, Boolean, Text, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
from sqlalchemy.dialects.sqlite import JSON as SQLITE_JSON

class AppUser(Base):
    __tablename__ = "app_user"
    id = Column(String, primary_key=True)
    phone_e164 = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=True)
    name = Column(String, nullable=True)
    locale = Column(String, default="en-IN")
    tz = Column(String, default="Asia/Kolkata")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class UserProfile(Base):
    __tablename__ = "user_profile"
    user_id = Column(String, ForeignKey("app_user.id"), primary_key=True)
    age_group = Column(String, nullable=True)
    sex_at_birth = Column(String, nullable=True)
    chronic_conditions = Column(SQLITE_JSON, nullable=True)
    allergies = Column(SQLITE_JSON, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Doctor(Base):
    __tablename__ = "doctor"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    degree = Column(String, nullable=True)
    regulator_id = Column(String, nullable=True)
    affiliations = Column(Text, nullable=True)
    years_experience = Column(Integer, nullable=True)
    workplace = Column(String, nullable=True)
    specialties = Column(SQLITE_JSON, nullable=True)
    languages = Column(SQLITE_JSON, nullable=True)
    fee_cents = Column(Integer, nullable=True)
    is_free = Column(Boolean, default=False)
    timezone = Column(String, default="Asia/Kolkata", nullable=False)
    verified = Column(Boolean, default=False)
    doctor_score = Column(Numeric(2,1), default=4.5)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DoctorAvailability(Base):
    __tablename__ = "doctor_availability"
    id = Column(String, primary_key=True)
    doctor_id = Column(String, ForeignKey("doctor.id"))
    start_time = Column(DateTime(timezone=True), nullable=True)
    end_time = Column(DateTime(timezone=True), nullable=True)

class Encounter(Base):
    __tablename__ = "encounter"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("app_user.id"))
    doctor_id = Column(String, ForeignKey("doctor.id"), nullable=True)
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    closed_at = Column(DateTime(timezone=True), nullable=True)
    acuity = Column(String, nullable=True)
    red_flags = Column(SQLITE_JSON, nullable=True)
    guideline_citations = Column(SQLITE_JSON, nullable=True)
    summary_pdf_path = Column(String, nullable=True)

class TriageState(Base):
    __tablename__ = "triage_state"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("app_user.id"), nullable=True)
    complaint = Column(String, nullable=False)
    state = Column(SQLITE_JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class DoctorRating(Base):
    __tablename__ = "doctor_rating"
    id = Column(String, primary_key=True)
    encounter_id = Column(String, ForeignKey("encounter.id"))
    doctor_id = Column(String, ForeignKey("doctor.id"))
    user_id = Column(String, ForeignKey("app_user.id"))
    score = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AuditLog(Base):
    __tablename__ = "audit_log"
    id = Column(Integer, primary_key=True, autoincrement=True)
    actor_type = Column(String)
    actor_id = Column(String)
    event = Column(String)
    payload = Column(SQLITE_JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class GuidelineReference(Base):
    __tablename__ = "guideline_reference"
    id = Column(String, primary_key=True)
    complaint = Column(String, nullable=False)
    source = Column(String, nullable=False)
    version = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
    body = Column(Text, nullable=False)
