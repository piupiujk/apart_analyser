from typing import Optional
from pydantic import BaseModel, EmailStr

class SUserRegister(BaseModel):
    email: EmailStr
    password: Optional[str] = None
    tg_id: Optional[int] = None

    @property
    def is_valid(self):
        return bool(self.password) or bool(self.tg_id)