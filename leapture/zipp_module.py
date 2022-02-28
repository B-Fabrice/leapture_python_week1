import zipfile
import zipp
import io

data = io.BytesIO()
z = zipp.Path('exp.zip')
z.open()