from .models import Employees, EmployeesSchema
from modules import Session


class EmployeesController:
    @staticmethod
    def create_employee(db: Session, data: EmployeesSchema):
        employee = Employees(**data.dict())
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee

    @staticmethod
    def get_all_employee(db: Session):
        employees = db.query(Employees).all()
        return employees

    @staticmethod
    def get_employee(db: Session, id: int):
        employee = db.query(Employees).filter(Employees.id == id).first()
        return employee

    @staticmethod
    def delete_employee(db: Session, id: int):
        employee = db.query(Employees).filter(Employees.id == id).first()
        db.delete(employee)
        db.commit()
        return employee

    @staticmethod
    def update_employee(db: Session, id: int, data: EmployeesSchema, emp):
        employee = emp
        employee.first_name = data.first_name
        employee.last_name = data.last_name
        employee.phone = data.phone
        employee.address = data.address
        employee.is_staff = data.is_staff
        db.merge(employee)
        db.commit()
        db.refresh(employee)
        return employee
