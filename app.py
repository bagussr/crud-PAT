from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from modules import FastAPI, Depends, Request, Form, uvicorn, Session, TEMPLATE_DIR
from src.controller import EmployeesController
from src.models import get_db, EmployeesSchema, Base


app = FastAPI()

templates = Jinja2Templates(directory=TEMPLATE_DIR)

ClassEmployees = EmployeesController()


@app.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    employees = ClassEmployees.get_all_employee(db)
    meta = Base.metadata.tables["employees"].columns.keys()
    return templates.TemplateResponse("index.html", {"request": request, "employees": employees, "meta": meta})


@app.get("/tambahdata")
def index_employee(request: Request):
    return templates.TemplateResponse("addForm.html", {"request": request, "employee": None})


@app.post("/tambahdata")
def tambah_data(
    request: Request,
    db: Session = Depends(get_db),
    first_name: str = Form(...),
    last_name: str = Form(...),
    phone: int = Form(...),
    address: str = Form(...),
    is_staff: bool = Form(...),
):
    data = EmployeesSchema(first_name=first_name, last_name=last_name, phone=phone, address=address, is_staff=is_staff)
    ClassEmployees.create_employee(db, data)
    return RedirectResponse(url="/", status_code=302)


@app.get("/employee/{id}")
def index_edit(request: Request, id: int, db: Session = Depends(get_db)):
    employee = ClassEmployees.get_employee(db, id)
    return templates.TemplateResponse("addForm.html", {"request": request, "employee": employee})


@app.get("/employee/{id}/delete")
def delete_employee(request: Request, id: int, db: Session = Depends(get_db)):
    ClassEmployees.delete_employee(db, id)
    return RedirectResponse(url="/", status_code=302)


@app.post("/employee/update")
def update_employee(
    db: Session = Depends(get_db),
    id: int = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    phone: int = Form(...),
    address: str = Form(...),
    is_staff: bool = Form(...),
):
    emp = ClassEmployees.get_employee(db, id)
    data = EmployeesSchema(first_name=first_name, last_name=last_name, phone=phone, address=address, is_staff=is_staff)
    ClassEmployees.update_employee(db, id, data, emp)
    return RedirectResponse(url="/", status_code=302)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=80, reload=True)
