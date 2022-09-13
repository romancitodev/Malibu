from src.models.Interface import App

app = App()

dummy_name = 'Dummy'
dummy_password = "DummyPassword01!"
app.start({'username':dummy_name,'password':dummy_password},1)