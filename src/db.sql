--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Ubuntu 11.5-3.pgdg18.04+1)
-- Dumped by pg_dump version 11.5 (Ubuntu 11.5-3.pgdg18.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: btree_gin; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS btree_gin WITH SCHEMA public;


--
-- Name: EXTENSION btree_gin; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION btree_gin IS 'support for indexing common datatypes in GIN';


--
-- Name: btree_gist; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS btree_gist WITH SCHEMA public;


--
-- Name: EXTENSION btree_gist; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION btree_gist IS 'support for indexing common datatypes in GiST';


--
-- Name: citext; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;


--
-- Name: EXTENSION citext; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION citext IS 'data type for case-insensitive character strings';


--
-- Name: cube; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS cube WITH SCHEMA public;


--
-- Name: EXTENSION cube; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION cube IS 'data type for multidimensional cubes';


--
-- Name: dblink; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS dblink WITH SCHEMA public;


--
-- Name: EXTENSION dblink; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION dblink IS 'connect to other PostgreSQL databases from within a database';


--
-- Name: dict_int; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS dict_int WITH SCHEMA public;


--
-- Name: EXTENSION dict_int; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION dict_int IS 'text search dictionary template for integers';


--
-- Name: dict_xsyn; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS dict_xsyn WITH SCHEMA public;


--
-- Name: EXTENSION dict_xsyn; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION dict_xsyn IS 'text search dictionary template for extended synonym processing';


--
-- Name: earthdistance; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS earthdistance WITH SCHEMA public;


--
-- Name: EXTENSION earthdistance; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION earthdistance IS 'calculate great-circle distances on the surface of the Earth';


--
-- Name: fuzzystrmatch; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS fuzzystrmatch WITH SCHEMA public;


--
-- Name: EXTENSION fuzzystrmatch; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION fuzzystrmatch IS 'determine similarities and distance between strings';


--
-- Name: hstore; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS hstore WITH SCHEMA public;


--
-- Name: EXTENSION hstore; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION hstore IS 'data type for storing sets of (key, value) pairs';


--
-- Name: intarray; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS intarray WITH SCHEMA public;


--
-- Name: EXTENSION intarray; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION intarray IS 'functions, operators, and index support for 1-D arrays of integers';


--
-- Name: ltree; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS ltree WITH SCHEMA public;


--
-- Name: EXTENSION ltree; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION ltree IS 'data type for hierarchical tree-like structures';


--
-- Name: pg_stat_statements; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pg_stat_statements WITH SCHEMA public;


--
-- Name: EXTENSION pg_stat_statements; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_stat_statements IS 'track execution statistics of all SQL statements executed';


--
-- Name: pg_trgm; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;


--
-- Name: EXTENSION pg_trgm; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_trgm IS 'text similarity measurement and index searching based on trigrams';


--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


--
-- Name: pgrowlocks; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pgrowlocks WITH SCHEMA public;


--
-- Name: EXTENSION pgrowlocks; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgrowlocks IS 'show row-level locking information';


--
-- Name: pgstattuple; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pgstattuple WITH SCHEMA public;


--
-- Name: EXTENSION pgstattuple; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgstattuple IS 'show tuple-level statistics';


--
-- Name: tablefunc; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS tablefunc WITH SCHEMA public;


--
-- Name: EXTENSION tablefunc; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION tablefunc IS 'functions that manipulate whole tables, including crosstab';


--
-- Name: unaccent; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS unaccent WITH SCHEMA public;


--
-- Name: EXTENSION unaccent; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION unaccent IS 'text search dictionary that removes accents';


--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


--
-- Name: xml2; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS xml2 WITH SCHEMA public;


--
-- Name: EXTENSION xml2; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION xml2 IS 'XPath querying and XSLT';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: bahanDasar; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public."bahanDasar" (
    id integer NOT NULL,
    nama character varying,
    kuantitas integer
);


ALTER TABLE public."bahanDasar" OWNER TO xpjfchbo;

--
-- Name: bahanDasar_menu; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public."bahanDasar_menu" (
    "idBahan" integer NOT NULL,
    "idMenu" integer NOT NULL
);


ALTER TABLE public."bahanDasar_menu" OWNER TO xpjfchbo;

--
-- Name: cabang; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public.cabang (
    "idCabang" integer NOT NULL,
    alamat character varying,
    status character varying,
    "noTelp" integer,
    "kapasitasPelanggan" integer
);


ALTER TABLE public.cabang OWNER TO xpjfchbo;

--
-- Name: cabang_Owner; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public."cabang_Owner" (
    "idCabang" integer NOT NULL,
    "idOwner" integer NOT NULL,
    "kapasitasPelanggan" integer
);


ALTER TABLE public."cabang_Owner" OWNER TO xpjfchbo;

--
-- Name: dataBeban; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public."dataBeban" (
    "idBeban" integer NOT NULL,
    tanggal date,
    "namaBeban" character varying,
    harga double precision,
    kuantitas integer,
    satuan character varying,
    "totalHarga" double precision
);


ALTER TABLE public."dataBeban" OWNER TO xpjfchbo;

--
-- Name: dataKeuangan; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public."dataKeuangan" (
    "idDataKeuangan" integer NOT NULL,
    "idDataPemasukan" integer,
    "idDataPengeluaran" integer,
    "idDataBeban" integer,
    tanggal date
);


ALTER TABLE public."dataKeuangan" OWNER TO xpjfchbo;

--
-- Name: karyawan; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public.karyawan (
    "idKaryawan" integer NOT NULL,
    "namaKaryawan" character varying,
    email character varying,
    "noTelp" integer,
    jabatan character varying,
    username character varying,
    password character varying,
    gaji double precision,
    role character varying,
    "idCabang" integer
);


ALTER TABLE public.karyawan OWNER TO xpjfchbo;

--
-- Name: menu; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public.menu (
    "idMenu" integer NOT NULL,
    nama character varying,
    "jenisMenu" character varying,
    harga double precision,
    ketersediaan boolean
);


ALTER TABLE public.menu OWNER TO xpjfchbo;

--
-- Name: orderLine; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public."orderLine" (
    "idPesanan" integer NOT NULL,
    "idMenu" integer NOT NULL,
    kuantitas integer,
    "jumlahHarga" integer
);


ALTER TABLE public."orderLine" OWNER TO xpjfchbo;

--
-- Name: owner; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public.owner (
    "idOwner" integer NOT NULL,
    nama character varying,
    email character varying,
    "noTelp" integer,
    alamat character varying,
    username character varying,
    password character varying,
    role character varying
);


ALTER TABLE public.owner OWNER TO xpjfchbo;

--
-- Name: pelanggan; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public.pelanggan (
    "idPelanggan" integer NOT NULL,
    "namaPelanggan" character varying
);


ALTER TABLE public.pelanggan OWNER TO xpjfchbo;

--
-- Name: pembayaran; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public.pembayaran (
    "idBayar" integer NOT NULL,
    tanggal date,
    "metodePembayaran" character varying,
    "totalHarga" double precision,
    "idPesanan" integer
);


ALTER TABLE public.pembayaran OWNER TO xpjfchbo;

--
-- Name: pengeluaran; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public.pengeluaran (
    "idPengeluaran" integer NOT NULL,
    deskripsi character varying(50),
    jenis character varying,
    total integer
);


ALTER TABLE public.pengeluaran OWNER TO xpjfchbo;

--
-- Name: pesanan; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public.pesanan (
    "idPesanan" integer NOT NULL,
    tanggal date,
    "idPelanggan" integer,
    "idCabang" integer,
    "totalHarga" double precision
);


ALTER TABLE public.pesanan OWNER TO xpjfchbo;

--
-- Name: suppliers; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public.suppliers (
    "idSupplier" integer NOT NULL,
    "namaSupplier" character varying,
    "noTelp" integer
);


ALTER TABLE public.suppliers OWNER TO xpjfchbo;

--
-- Name: supplyBahanDasar; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public."supplyBahanDasar" (
    "idPengeluaran" integer NOT NULL,
    "idBahan" integer,
    harga integer,
    kuantitas integer,
    "idSupplier" integer,
    "totalHarga" double precision,
    tanggal date,
    satuan character varying
);


ALTER TABLE public."supplyBahanDasar" OWNER TO xpjfchbo;

--
-- Name: users; Type: TABLE; Schema: public; Owner: xpjfchbo
--

CREATE TABLE public.users (
    username character varying(100) NOT NULL,
    password character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    cabang character varying(100) NOT NULL,
    jabatan character varying(100) NOT NULL,
    role character varying(100) NOT NULL,
    "namaLengkap" character varying(100)
);


ALTER TABLE public.users OWNER TO xpjfchbo;

--
-- Data for Name: bahanDasar; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public."bahanDasar" (id, nama, kuantitas) FROM stdin;
1	Ceker	10
2	Kunyit	200
6	Mangga	0
8	Daging Ayam	20
4	Cayenne pepper	40
10	Black Pepper	30
666	ayam	30
33	daging kambing	14
34	sayur	11
123	Daging bebek	30
44	Habanero pepper	30
321	Kentang	13
37	Garam Masala	40
\.


--
-- Data for Name: bahanDasar_menu; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public."bahanDasar_menu" ("idBahan", "idMenu") FROM stdin;
\.


--
-- Data for Name: cabang; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public.cabang ("idCabang", alamat, status, "noTelp", "kapasitasPelanggan") FROM stdin;
\.


--
-- Data for Name: cabang_Owner; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public."cabang_Owner" ("idCabang", "idOwner", "kapasitasPelanggan") FROM stdin;
\.


--
-- Data for Name: dataBeban; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public."dataBeban" ("idBeban", tanggal, "namaBeban", harga, kuantitas, satuan, "totalHarga") FROM stdin;
8	2021-11-30	Gaji karyawan	3000000	50	orang	150000000
9	2021-11-30	Biayar print	30000	15	lembar	450000
16	2021-11-30	Biaya makan	30000	3	Rupiah	90000
3	2021-12-01	Bayar gaji karyawan	3000000	40	Orang	120000000
1	2021-12-01	Listrik 	5000000	50	MW	250000000
\.


--
-- Data for Name: dataKeuangan; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public."dataKeuangan" ("idDataKeuangan", "idDataPemasukan", "idDataPengeluaran", "idDataBeban", tanggal) FROM stdin;
1	4	\N	\N	2021-11-22
2	5	\N	\N	2021-11-22
3	\N	1	\N	2021-12-01
4	\N	2	\N	2021-12-01
\.


--
-- Data for Name: karyawan; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public.karyawan ("idKaryawan", "namaKaryawan", email, "noTelp", jabatan, username, password, gaji, role, "idCabang") FROM stdin;
\.


--
-- Data for Name: menu; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public.menu ("idMenu", nama, "jenisMenu", harga, ketersediaan) FROM stdin;
1	Jus Mangga	Minuman	7000	f
2	Seblak Ceker	Seblak	15000	t
3	Seblak Kerupuk	Seblak	12000	t
\.


--
-- Data for Name: orderLine; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public."orderLine" ("idPesanan", "idMenu", kuantitas, "jumlahHarga") FROM stdin;
\.


--
-- Data for Name: owner; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public.owner ("idOwner", nama, email, "noTelp", alamat, username, password, role) FROM stdin;
\.


--
-- Data for Name: pelanggan; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public.pelanggan ("idPelanggan", "namaPelanggan") FROM stdin;
\.


--
-- Data for Name: pembayaran; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public.pembayaran ("idBayar", tanggal, "metodePembayaran", "totalHarga", "idPesanan") FROM stdin;
1	2021-11-21	BRI	300000	2
7	2021-11-21	Cash	23000	7
3	2021-11-22	BNI	1000000	4
4	2021-11-22	test	100000	6000
5	2021-11-22	BRI	500000	200
10	2021-11-29	BCA	35000	10
\.


--
-- Data for Name: pengeluaran; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public.pengeluaran ("idPengeluaran", deskripsi, jenis, total) FROM stdin;
1	Supply Bahan Dasar	Supply	140000
2	Supply Bahan Dasar	Supply	20000000
\.


--
-- Data for Name: pesanan; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public.pesanan ("idPesanan", tanggal, "idPelanggan", "idCabang", "totalHarga") FROM stdin;
1	2021-11-20	1	1	18000
2	2021-11-20	2	2	24000
3	2021-11-20	3	3	21000
4	2021-11-20	4	1	4
5	2021-11-20	5	1	37000
7	2021-11-21	7	1	23000
10	2021-11-29	10	1	35000
\.


--
-- Data for Name: suppliers; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public.suppliers ("idSupplier", "namaSupplier", "noTelp") FROM stdin;
1	relieyan	81374856
\.


--
-- Data for Name: supplyBahanDasar; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public."supplyBahanDasar" ("idPengeluaran", "idBahan", harga, kuantitas, "idSupplier", "totalHarga", tanggal, satuan) FROM stdin;
1	2	20000	7	1	140000	2021-12-01	kilogram
2	37	500000	40	1	20000000	2021-12-01	karung
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: xpjfchbo
--

COPY public.users (username, password, email, cabang, jabatan, role, "namaLengkap") FROM stdin;
admon	admin	admin@admin.com	dago	owner	owner	\N
admin	$2b$12$D6yjrLpM323BNjYUcQroSuQOi/Ymx8AuB92zUpJC4A2HDAZrEV9ZO	admin@admin.co.id	Cihanjuang	admin	admin	admin
simas	$2b$12$m0nDqrYIUo31YLmlyy/RteGxPCT2IeFh6.B8vgfIl..uL5utbm8si	mas@gmail.com	Dago	Kepala Cabang Dago	admin	Si Mas
masala	$2b$12$m2JEp4qFT7sGfwt..GmJ9.aAEfDbmlJ7l4x1NHOpA6Wbpbu/Gj8tG	indianguy@gmail.com	Bombai	Kepala Cabang	Karyawan	Tika Masala
\.


--
-- Name: bahanDasar_menu bahanDasar_menu_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."bahanDasar_menu"
    ADD CONSTRAINT "bahanDasar_menu_pkey" PRIMARY KEY ("idBahan", "idMenu");


--
-- Name: bahanDasar bahanDasar_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."bahanDasar"
    ADD CONSTRAINT "bahanDasar_pkey" PRIMARY KEY (id);


--
-- Name: cabang_Owner cabang_Owner_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."cabang_Owner"
    ADD CONSTRAINT "cabang_Owner_pkey" PRIMARY KEY ("idCabang", "idOwner");


--
-- Name: cabang cabang_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.cabang
    ADD CONSTRAINT cabang_pkey PRIMARY KEY ("idCabang");


--
-- Name: dataBeban dataBeban_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."dataBeban"
    ADD CONSTRAINT "dataBeban_pkey" PRIMARY KEY ("idBeban");


--
-- Name: dataKeuangan dataKeuangan_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."dataKeuangan"
    ADD CONSTRAINT "dataKeuangan_pkey" PRIMARY KEY ("idDataKeuangan");


--
-- Name: karyawan karyawan_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.karyawan
    ADD CONSTRAINT karyawan_pkey PRIMARY KEY ("idKaryawan");


--
-- Name: menu menu_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.menu
    ADD CONSTRAINT menu_pkey PRIMARY KEY ("idMenu");


--
-- Name: orderLine orderLine_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."orderLine"
    ADD CONSTRAINT "orderLine_pkey" PRIMARY KEY ("idPesanan", "idMenu");


--
-- Name: owner owner_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.owner
    ADD CONSTRAINT owner_pkey PRIMARY KEY ("idOwner");


--
-- Name: pelanggan pelanggan_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.pelanggan
    ADD CONSTRAINT pelanggan_pkey PRIMARY KEY ("idPelanggan");


--
-- Name: pembayaran pembayaran_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.pembayaran
    ADD CONSTRAINT pembayaran_pkey PRIMARY KEY ("idBayar");


--
-- Name: pengeluaran pengeluaran_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.pengeluaran
    ADD CONSTRAINT pengeluaran_pkey PRIMARY KEY ("idPengeluaran");


--
-- Name: pesanan pesanan_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.pesanan
    ADD CONSTRAINT pesanan_pkey PRIMARY KEY ("idPesanan");


--
-- Name: suppliers suppliers_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.suppliers
    ADD CONSTRAINT suppliers_pkey PRIMARY KEY ("idSupplier");


--
-- Name: supplyBahanDasar supplyBahanDasar_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."supplyBahanDasar"
    ADD CONSTRAINT "supplyBahanDasar_pkey" PRIMARY KEY ("idPengeluaran");


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (username);


--
-- Name: bahanDasar_menu FK_bahanDasar_menu.idBahan; Type: FK CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."bahanDasar_menu"
    ADD CONSTRAINT "FK_bahanDasar_menu.idBahan" FOREIGN KEY ("idBahan") REFERENCES public."bahanDasar"(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: bahanDasar_menu FK_bahanDasar_menu.idMenu; Type: FK CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."bahanDasar_menu"
    ADD CONSTRAINT "FK_bahanDasar_menu.idMenu" FOREIGN KEY ("idMenu") REFERENCES public.menu("idMenu") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: cabang_Owner FK_cabang_Owner.idCabang; Type: FK CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."cabang_Owner"
    ADD CONSTRAINT "FK_cabang_Owner.idCabang" FOREIGN KEY ("idCabang") REFERENCES public.cabang("idCabang");


--
-- Name: cabang_Owner FK_cabang_Owner.idOwner; Type: FK CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."cabang_Owner"
    ADD CONSTRAINT "FK_cabang_Owner.idOwner" FOREIGN KEY ("idOwner") REFERENCES public.owner("idOwner");


--
-- Name: karyawan FK_karyawan.jabatan; Type: FK CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public.karyawan
    ADD CONSTRAINT "FK_karyawan.jabatan" FOREIGN KEY ("idCabang") REFERENCES public.cabang("idCabang");


--
-- Name: orderLine FK_orderLine.idMenu; Type: FK CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."orderLine"
    ADD CONSTRAINT "FK_orderLine.idMenu" FOREIGN KEY ("idMenu") REFERENCES public.menu("idMenu");


--
-- Name: orderLine FK_orderLine.idPesanan; Type: FK CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."orderLine"
    ADD CONSTRAINT "FK_orderLine.idPesanan" FOREIGN KEY ("idPesanan") REFERENCES public.pesanan("idPesanan");


--
-- Name: dataKeuangan fk_datapengeluaran_idpengeluaran; Type: FK CONSTRAINT; Schema: public; Owner: xpjfchbo
--

ALTER TABLE ONLY public."dataKeuangan"
    ADD CONSTRAINT fk_datapengeluaran_idpengeluaran FOREIGN KEY ("idDataPengeluaran") REFERENCES public.pengeluaran("idPengeluaran");


--
-- PostgreSQL database dump complete
--

