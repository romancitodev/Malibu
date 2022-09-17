from src.models.Interface import App
from src.types.Employee import EmployeeDict

app = App()

dummy_name = 'Dummy'
dummy_password = "DummyPassword01!"
credentials = EmployeeDict(dummy_name, dummy_password)
app.start(credentials,1)



        