from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import Boolean, Float, Date
from database import Base

class DataBahanDasar(Base) :
    __tablename__ = 'bahanDasar'

    id = Column(Integer, primary_key=True)
    nama = Column(String)
    kuantitas = Column(Integer)

class Pengeluaran(Base) :
    __tablename__ = 'pengeluaran'

    idPengeluaran = Column(Integer, primary_key=True)
    deskripsi = Column(String)
    jenis = Column(String)
    total = Column(Float)

class Menu(Base) :
    __tablename__ = 'menu'

    idMenu = Column(Integer, primary_key=True)
    nama = Column(String)
    jenisMenu = Column(String)
    harga = Column(Float)
    ketersediaan = Column(Boolean)


class pembayaran(Base):
    __tablename__ = "pembayaran"

    idBayar = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    metodePembayaran = Column(String)
    totalHarga = Column(Integer)
    idPesanan = Column(Integer)


class pesanan(Base):
    __tablename__ = "pesanan"

    idPesanan = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    idPelanggan = Column(Integer, unique=True)
    idCabang = Column(Integer)
    totalHarga = Column(Integer)

class SupplyBahanDasar(Base):
    __tablename__ = "supplyBahanDasar"

    idPengeluaran= Column(Integer, primary_key=True, index=True)
    idBahan = Column(Integer)
    harga = Column(Integer)
    kuantitas = Column(Integer)
    idSupplier = Column(Integer)
    totalHarga = Column(Float)
    tanggal = Column(Date)
    satuan = Column(String)


class DataKeuangan(Base):
    __tablename__ = "dataKeuangan"


    idDataKeuangan = Column(Integer, primary_key=True, index=True)
    idDataPemasukan = Column(Integer)
    idDataPengeluaran = Column(Integer)
    idDataBeban = Column(Integer)
    tanggal= Column(Date, index=True)

class Beban(Base) :
    __tablename__ = 'dataBeban'

    idBeban = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    namaBeban = Column(String)
    harga = Column(Float)
    kuantitas = Column(Integer)
    satuan = Column(String)
    totalHarga = Column(Float)

class User(Base) :
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    password = Column(String)
    email = Column(String)
    cabang = Column(String)
    jabatan = Column(String)
    role = Column(String)
    namaLengkap = Column(String)



