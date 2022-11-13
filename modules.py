from fastapi import FastAPI, Depends, Request, Form
from sqlalchemy import create_engine, Integer, String, Column, Boolean
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
import uvicorn
import os


TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "views")
