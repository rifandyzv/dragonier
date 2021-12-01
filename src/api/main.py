from fastapi import FastAPI, HTTPException, Response
from fastapi.params import Depends
from sqlalchemy.sql.base import DedupeColumnCollection
from sqlalchemy.sql import functions
from starlette.responses import RedirectResponse
from schemas import BahanDasar, BebanSchema, PengeluaranSchema, PembayaranSchema, SupplyBahanDasar, BebanSchema, UserSchema, RegisterSchema
from sqlalchemy.orm import Session
from database import *
from models import DataBahanDasar, DataKeuangan, Menu, Pengeluaran, pembayaran, pesanan, Beban, User
import crud
from passlib.hash import bcrypt

app = FastAPI()

@app.get("/")
def redirect_to_docs():
    return (RedirectResponse('/docs'))
@app.get("/menu")
def get_menu(db : Session = Depends(get_db)):
    try :
        return db.query(Menu).all()
    except Exception as e :
        print(e)
        raise HTTPException(status_code=406, detail='error')

@app.post("/bahan-dasar")
def  add_bahan_dasar(newBahan: BahanDasar, db : Session = Depends(get_db)) :
    try :
        newData = DataBahanDasar(
            id = newBahan.id,
            nama=newBahan.nama,
            kuantitas = newBahan.kuantitas
        )
        db.add(newData)
        db.commit()

    except Exception as e :
        print(e)
        raise HTTPException(status_code=401, detail='Error')
    return {
        'status' : 'data post success',
    }

@app.post("/pengeluaran")
def  add_data_pengeluaran(pengeluaran: PengeluaranSchema, db : Session = Depends(get_db)) :
    try :
        newData = Pengeluaran(
            idPengeluaran = pengeluaran.idPengeluaran,
            deskripsi = pengeluaran.deskripsi,
            jenis = pengeluaran.jenis,
            total = pengeluaran.total
        )
        db.add(newData)
        db.commit()

    except Exception as e :
        print(e)
        raise HTTPException(status_code=400, detail='Error')
    return {
        'status' : 'data post success',
    }


@app.post("/postDataPembayaran/")
async def input_data_pembayaran(pembayaran : PembayaranSchema, db: Session = Depends(get_db)):
    try:
        addDataPesanan = crud.add_data_pesanan(db, pembayaran)
        addDataPembayaran = crud.add_data_pembayaran(db, pembayaran)
        if (addDataPembayaran == None):
            return "Adding data to database error!"
        return addDataPembayaran
    except: 
        return "Error adding to database, data already exist. idPesanan, idPelanggan, and idBayar should be unique"

@app.get("/homepage")
async def get_homepage():
    return "Homepage"
# @app.post("/dataPesanan/")
# async def input_data_pesanan(pesanan : schemas.pesanan, db: Session = Depends(get_db)):
#     addDataPesanan = crud.add_data_pesanan(db, pesanan)
#     return addDataPesanan

@app.get("/getDataPembayaran/")
async def get_data_pembayaran(tanggal: str, db: Session = Depends(get_db)):
    getDataPembayaran = crud.get_data_pembayaran(db, tanggal)
    if (getDataPembayaran == []):
        return "No data available" 
    return getDataPembayaran

@app.get("/getDataPesanan/")
async def get_data_pesanan(tanggal: str, db: Session = Depends(get_db)):
    getDataPesanan = crud.get_data_pesanan(db, tanggal)
    if (getDataPesanan == []):
        return "No data available"
    return getDataPesanan
    
@app.get("/getDataPemasukan")
async def get_data_pemasukan(tanggal: str, db: Session = Depends(get_db)):
    getDataPemasukan = crud.get_data_pemasukan(db, tanggal)
    if (getDataPemasukan == []):
        return "No data available"
    return getDataPemasukan


@app.post("/dataKeuangan/pemasukan", response_model=PembayaranSchema)
def post_data_pemasukan(pembayaran: PembayaranSchema, db: Session = Depends(get_db)):
    return crud.post_data_pemasukan(db=db, pembayaran=pembayaran)

@app.post("/dataKeuangan/pengeluaran", response_model=PengeluaranSchema)
def post_data_pengeluaran(pengeluaran: PengeluaranSchema, db: Session=Depends(get_db)):
    return crud.post_data_pengeluaran(db=db, pengeluaran=pengeluaran)

# @app.post("/dataKeuangan/supplyBahanDasar", response_model=SupplyBahanDasar)
# def post_data_supply_bahan(supplyBahanDasar: SupplyBahanDasar, db: Session=Depends(get_db)):
#     try :
#         return crud.post_supply_bahan_dasar(db=db, supplyBahanDasar=supplyBahanDasar)
#     except Exception as e :
#         print(e)

@app.post("/dataKeuangan/supplyBahanDasar", response_model=SupplyBahanDasar)
def post_data_supply_bahan(supplyBahanDasar: SupplyBahanDasar, db: Session=Depends(get_db)):
    return crud.post_supply_bahan_dasar(db=db, supplyBahanDasar=supplyBahanDasar)

@app.put("/bahanDasar")
async def update_bahan_dasar(id_bahan: int, nama: str, kuantitas: int, db: Session = Depends(get_db)):
    db_bahan = crud.update_item(db, id_bahan, nama, kuantitas)
    if db_bahan is None:
        raise HTTPException(status_code=404, detail="Bahan not found")
    return db_bahan

@app.get("/bahanDasar")
async def visualisasi_bahan_dasar(db : Session = Depends(get_db)):
    try :
        return db.query(DataBahanDasar).all()
    except Exception as e :
        print(e)

@app.get("/dataKeuangan")
async def get_data_keuangan(db : Session = Depends(get_db)):
    try :
        return db.query()
        
        # return db.query(DataKeuangan).all()
    except Exception as e :
        raise HTTPException(status_code=404, detail =e)

@app.post("/dataBeban")
async def post_data_beban(beban: BebanSchema, db: Session = Depends(get_db)):
    try :
        newData = Beban(
            idBeban = beban.idBeban,
            tanggal = beban.tanggal,
            namaBeban = beban.namaBeban,
            harga = beban.harga,
            kuantitas = beban.kuantitas,
            satuan = beban.satuan,
            totalHarga = beban.harga * beban.kuantitas
        )
        db.add(newData)
        db.commit()
        return {'status' : 'data post success'}
    except Exception as e:
        print(e)
        return e

@app.post("/login", tags=['auth'])
async def login(user : UserSchema, db: Session=Depends(get_db)) :
    try :
        userCheck = db.query(User).filter(user.username == User.username).first()
        if (user.username == userCheck.username and bcrypt.verify(user.password, userCheck.password)) :
            return {"status" : "ok"}
        else :
            raise HTTPException(status_code=400, detail="Invlid credentials !")
    except Exception as e :
        print(e)
        raise HTTPException(status_code=400, detail="Invlid credentials !")

@app.post("/register", tags=['auth'])
async def register(user : RegisterSchema, db: Session=Depends(get_db)) :
    try :
        user = User(
            username = user.username,
            password = bcrypt.hash(user.password),
            email = user.email,
            cabang = user.cabang,
            jabatan = user.jabatan,
            role = user.role,
            namaLengkap = user.namaLengkap

        )
        db.add(user)
        db.commit()

        return {
            'status' : 'user registered'
        }
    except Exception as e :
        print(e)
        raise HTTPException(status_code=400, detail="Bad Request !!")