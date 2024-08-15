from fastapi import Depends

@router.get("/contacts/", response_model=List[schemas.Contact])
async def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Contact).filter(models.Contact.owner_id == current_user.id).offset(skip).limit(limit).all()
