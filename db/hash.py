from passlib.context import CryptContext

pswd_ctx = CryptContext(schemes=["bcrypt"], deprecated='auto')

class Hash():

    def bcrypt(password: str) -> str:
        return pswd_ctx.hash(password)
    
    def verify(hashed_password: str, plain_password: str) -> bool:
        return pswd_ctx.verify(plain_password, hashed_password)