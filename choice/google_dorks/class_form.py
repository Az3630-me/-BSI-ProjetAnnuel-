from __future__ import annotations
from dataclasses import dataclass

@dataclass
class FormDorks:
    setting : str
    field1 : str
    field2 : str | None
    field3 : str | None
    field4 : str | None
    field5 : str | None

def create_empty_dork_form():
    return FormDorks()
