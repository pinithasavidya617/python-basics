from dataclasses import dataclass
from typing import Optional


@dataclass
class Student:
    st_id : str
    name : str
    email : str
    year : str

@dataclass
class Course:
    course_id : str
    title : str
    credits : str
    lecturer : str

@dataclass
class Registration:
    st_id : str
    course_id : str
    semester : Optional[str] = None