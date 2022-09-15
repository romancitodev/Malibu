from src.models.Interface import App
from types.Employee import EmployeeDict

app = App()

dummy_name = 'Dummy'
dummy_password = "DummyPassword01!"
credentials: EmployeeDict = {
    'username': dummy_name,
    'password': dummy_password
}
app.start(credentials,1)

