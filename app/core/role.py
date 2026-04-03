from fastapi import Depends, HTTPException

def require_role(roles: list):
    def checker(user):
        if user.role not in roles:
            raise HTTPException(status_code=403, detail="Not Found")
        return user
    return checker