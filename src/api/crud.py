from sqlalchemy import schema
from sqlalchemy.orm import Session

import models, schemas
from datetime import datetime, date

jumlahOrang = 0

def add_data_pembayaran(db: Session, pembayaran : schemas.PembayaranSchema):
    new_dataPembayaran = models.pembayaran(idBayar = pembayaran.idBayar, tanggal = pembayaran.tanggal, 
                                        metodePembayaran = pembayaran.metodePembayaran, totalHarga = pembayaran.totalHarga,
                                        idPesanan = pembayaran.idPesanan)
    db.add(new_dataPembayaran)
    db.commit()
    db.refresh(new_dataPembayaran)
    return new_dataPembayaran


def add_data_pesanan(db: Session, pesanan : schemas.PembayaranSchema):
    new_dataPesanan = models.pesanan(idPelanggan = pesanan.idPelanggan, idCabang = pesanan.idCabang, totalHarga = pesanan.totalHarga,
                                    idPesanan = pesanan.idPesanan, tanggal = pesanan.tanggal)
    db.add(new_dataPesanan)
    db.commit()
    db.refresh(new_dataPesanan)
    return new_dataPesanan


def get_data_pembayaran(db: Session, Tanggal: str):
    return db.query(models.pembayaran).filter(models.pembayaran.tanggal == Tanggal).all()

def get_data_pesanan(db: Session, Tanggal: str):
    return db.query(models.pesanan).filter(models.pesanan.tanggal == Tanggal).all()


def get_data_pemasukan(db: Session, Tanggal: str):
    totalPemasukan = db.query(models.pesanan.totalHarga).filter(models.pesanan.tanggal == Tanggal).all()
    total = len(db.query(models.pesanan.totalHarga).filter(models.pesanan.tanggal == Tanggal).all())
    totalUangMasuk  = 0
    for idx in range(total):
        totalUangMasuk += totalPemasukan[idx]['totalHarga']
    # total2 = totalPemasukan[2]['totalHarga'] + totalPemasukan[1]['totalHarga']
    
    return "Total pemasukan pada " + str(Tanggal) + " adalah Rp" + str(totalUangMasuk)



def post_data_pemasukan(db: Session, pembayaran: schemas.PembayaranSchema):
    rowsPembayaran = db.query(models.Pembayaran).count()
    newRowPembayaran = rowsPembayaran + 1
    rowsDataKeuangan = db.query(models.DataKeuangan).count()
    newRowDataKeuangan = rowsDataKeuangan + 1
    db_data_bayar = models.Pembayaran(idBayar=newRowPembayaran, tanggal=pembayaran.tanggal, metodePembayaran=pembayaran.metodePembayaran, totalHarga=pembayaran.totalHarga, idPesanan=pembayaran.idPesanan)
    db_data_masuk = models.DataKeuangan(idDataKeuangan=newRowDataKeuangan, idDataPemasukan=newRowPembayaran, tanggal=pembayaran.tanggal)
    db.add(db_data_bayar)
    db.add(db_data_masuk)
    db.commit()
    db.refresh(db_data_bayar)
    db.refresh(db_data_masuk)
    return db_data_bayar

def post_data_pengeluaran(db: Session, pengeluaran: schemas.Pengeluaran):
    rowsPengeluaran = db.query(models.Pengeluaran).count()
    newRowPengeluaran = rowsPengeluaran + 1
    rowsDataKeuangan = db.query(models.DataKeuangan).count()
    newRowDataKeuangan = rowsDataKeuangan + 1
    db_data_keluar = models.Pengeluaran(idPengeluaran=newRowPengeluaran, deskripsi=pengeluaran.deskripsi, jenis=pengeluaran.jenis, total=pengeluaran.total)
    db_data_keuangan_keluar = models.DataKeuangan(idDataKeuangan=newRowDataKeuangan, idDataPengeluaran= newRowPengeluaran, tanggal=date.today().strftime("%Y-%m-%d"))
    db.add(db_data_keluar)
    db.commit()
    db.refresh(db_data_keluar)
    db.add(db_data_keuangan_keluar)
    db.commit()
    db.refresh(db_data_keuangan_keluar)
    return db_data_keluar

def post_supply_bahan_dasar(db: Session, supplyBahanDasar: schemas.SupplyBahanDasar):
    rowsBahanDasar = db.query(models.SupplyBahanDasar).count()
    newRowBahanDasar= rowsBahanDasar + 1
    rowsPengeluaran = db.query(models.Pengeluaran).count()
    newRowPengeluaran = rowsPengeluaran + 1
    rowsDataKeuangan = db.query(models.DataKeuangan).count()
    newRowDataKeuangan = rowsDataKeuangan + 1
    db_data_bahan = models.SupplyBahanDasar(idPengeluaran=newRowPengeluaran, idBahan=supplyBahanDasar.idBahan, harga=supplyBahanDasar.harga, kuantitas=supplyBahanDasar.kuantitas, idSupplier= supplyBahanDasar.idSupplier, totalHarga=(supplyBahanDasar.kuantitas)*(supplyBahanDasar.harga), tanggal=date.today().strftime("%Y-%m-%d"), satuan=supplyBahanDasar.satuan)
    db_data_keluar = models.Pengeluaran(idPengeluaran=newRowPengeluaran, deskripsi="Supply Bahan Dasar", jenis="Supply", total=(supplyBahanDasar.kuantitas)*(supplyBahanDasar.harga))
    db_data_keuangan_keluar = models.DataKeuangan(idDataKeuangan=newRowDataKeuangan, idDataPengeluaran= newRowPengeluaran, tanggal=date.today().strftime("%Y-%m-%d"))
    db.add(db_data_keluar)
    db.commit()
    db.refresh(db_data_keluar)
    db.add(db_data_bahan)
    db.commit()
    db.refresh(db_data_bahan)
    db.add(db_data_keuangan_keluar)
    db.commit()
    db.refresh(db_data_keuangan_keluar)
    return db_data_bahan

def add_item(db: Session, bahanDasar: schemas.BahanDasar):
    new_item = models.DataBahanDasar(
    id=bahanDasar.id, 
    nama=bahanDasar.nama, 
    kuantitas=bahanDasar.kuantitas
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item(db: Session, id_bahan: int, nama: str, kuantitas: int):
    db_bahan_to_update = db.query(models.DataBahanDasar).filter(models.DataBahanDasar.id == id_bahan).first()
    db_bahan_to_update.kuantitas = kuantitas
    db_bahan_to_update.nama = nama
    db.add(db_bahan_to_update)
    db.commit()
    db.refresh(db_bahan_to_update)
    return db_bahan_to_update