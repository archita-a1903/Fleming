import csv, json, uuid
from app.database import SessionLocal, Base, engine
from app.models import Doctor

def seed(csv_path="data/phantom_doctor_roster.csv"):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                did = str(uuid.uuid4())
                specialties = [s.strip() for s in (row.get("specialties","") or "").replace("|",",").split(",") if s.strip()]
                languages = [s.strip() for s in (row.get("languages","") or "").replace("|",",").split(",") if s.strip()]
                fee = row.get("fee_cents") or None
                fee = int(fee) if fee not in (None, "", "null", "NULL") else None
                is_free = str(row.get("is_free","false")).strip().lower() in ("true","1","yes","y")
                doc = Doctor(
                    id=did,
                    name=row.get("name","Unknown"),
                    degree=row.get("degree"),
                    regulator_id=row.get("regulator_id") or None,
                    affiliations=row.get("affiliations"),
                    years_experience=int(row.get("years_experience","0") or 0),
                    workplace=row.get("workplace"),
                    specialties=specialties or None,
                    languages=languages or None,
                    fee_cents=fee,
                    is_free=is_free,
                    timezone=row.get("timezone") or "Asia/Kolkata",
                    verified=False,
                    doctor_score=4.5
                )
                db.add(doc)
            db.commit()
        print("Seeded doctors from", csv_path)
    finally:
        db.close()

if __name__ == "__main__":
    seed()
