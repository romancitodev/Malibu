Config = {
   "username": r"[a-zA-Z][a-zA-Z0-9-_]{3,32}",
   "name": r"[a-zA-Z]{3,32}",
   "lastname": r"[a-zA-Z]{3,32}",
   "password": r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$",
   "email": r"\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b",
   "phone": r"^(\d{2})?(?:\s)?(\d{4})+(?:\s)?(\d{4})$",
}