import unittest
from unittest.mock import patch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api import Base, Device, ItemCreate

class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        self.SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
        Base.metadata.create_all(bind=self.engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.populate_test_data()

    def populate_test_data(self):
        db = self.SessionLocal()
        test_device = Device(
            tipo_dispositivo="computador",
            numero_tombamento="816996598",
            marca="positivo",
            memoria_ram="8GB",
            armazenamento="500GB",
            tipo_armazenamento="SSD",
            funcionando="sim",
            local_atual="sala de manutencao, gex-juaz",
            descricao="fonte queimada",
            data_analise="29/11/24"
        )
        db.add(test_device)
        db.commit()
        db.close()

    def test_connection(self):
        connection = self.engine.connect()
        self.assertIsNotNone(connection)
        connection.close()

    @patch('api.search_device')
    def test_search_device(self, mock_search_device):
        mock_device = Device(
            id=832658880,
            tipo_dispositivo="computador",
            numero_tombamento="832658880",
            marca="lenovo",
            memoria_ram="16GB",
            armazenamento="1TB",
            tipo_armazenamento="SSD",
            funcionando="sim",
            local_atual="sala de manutencao, gex-juaz",
            descricao="em perfeito estado",
            data_analise="01/01/25"
        )
        mock_search_device.return_value = mock_device

        db = self.SessionLocal()
        device = db.query(Device).filter(Device.numero_tombamento == "832658880").first()
        self.assertIsNotNone(device)
        self.assertEqual(device.marca, "lenovo")
        db.close()

if __name__ == '__main__':
    unittest.main()