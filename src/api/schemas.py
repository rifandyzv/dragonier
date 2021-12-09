from pydantic import BaseModel
from datetime import date
class BahanDasar(BaseModel) :
    id: int
    nama: str
    kuantitas: int

    class Config:
        orm_mode = True

class PengeluaranSchema(BaseModel) :
    idPengeluaran: int
    deskripsi: str
    jenis: str
    total: float

    class Config:
        orm_mode = True

class PembayaranSchema(BaseModel):
    # idBayar : int
    # tanggal : str
    metodePembayaran : str
    # totalHarga : int
    idPesanan : int
    # idPelanggan : int
    # idCabang : int

class DataKeuanganSchema(BaseModel):
    idDataKeuangan: int
    idDataPemasukan: int
    idDataPengeluaran: int
    idDataBeban: int
    tanggal: date

    class Config:
        orm_mode = True

class Pembayaran(BaseModel):
    # idBayar: int
    # tanggal: date
    metodePembayaran: str
    # totalHarga: float
    idPesanan: int

    class Config:
        orm_mode = True

class Pengeluaran(BaseModel):
    idPengeluaran: int
    deskripsi: str
    jenis: str
    total: int

    class Config:
        orm_mode = True

class SupplyBahanDasar(BaseModel):
    idBahan : int
    harga : int
    kuantitas : int
    idSupplier : int
    satuan : str

    class Config:
        orm_mode = True

class BebanSchema(BaseModel) :
    idBeban: int
    tanggal: date
    namaBeban: str
    harga: float
    kuantitas: int
    satuan: str

    class Config:
        orm_mode = True

class UserSchema(BaseModel) :
    username :str
    password : str

    class Config:
        orm_mode = True

class RegisterSchema(BaseModel) :
    namaLengkap : str
    email : str
    username : str
    password : str
    cabang : str
    jabatan : str
    role : str