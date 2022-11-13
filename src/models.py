from modules import declarative_base, create_engine, sessionmaker, Integer, String, Column, Boolean, BaseModel
import json

db_url = "postgresql://postgres:dadasdudus12@localhost:5432/perusahaan"
engine = create_engine(db_url)
Local_Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = Local_Session()
        yield db
    finally:
        db.close()


Base = declarative_base()


class Employees(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(Integer)
    address = Column(String(100))
    is_staff = Column(Boolean)

    def __repr__(self):
        data = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "address": self.address,
            "is_staff": self.is_staff,
        }
        return json.dumps(data)


class EmployeesSchema(BaseModel):
    first_name: str
    last_name: str
    phone: int
    address: str
    is_staff: bool
