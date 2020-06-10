--
-- PostgreSQL database dump
--

-- Dumped from database version 11.4
-- Dumped by pg_dump version 11.4

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: countries; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.countries (
    id integer NOT NULL,
    name character varying
);


--
-- Name: countries_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.countries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: countries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.countries_id_seq OWNED BY public.countries.id;


--
-- Name: regions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.regions (
    id integer NOT NULL,
    name character varying,
    country integer
);


--
-- Name: regions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.regions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: regions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.regions_id_seq OWNED BY public.regions.id;


--
-- Name: wines; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wines (
    id integer NOT NULL,
    name character varying,
    country_id integer,
    region_id integer,
    year integer
);


--
-- Name: wines_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wines_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wines_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wines_id_seq OWNED BY public.wines.id;


--
-- Name: countries id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.countries ALTER COLUMN id SET DEFAULT nextval('public.countries_id_seq'::regclass);


--
-- Name: regions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.regions ALTER COLUMN id SET DEFAULT nextval('public.regions_id_seq'::regclass);


--
-- Name: wines id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wines ALTER COLUMN id SET DEFAULT nextval('public.wines_id_seq'::regclass);


--
-- Data for Name: countries; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.countries (id, name) FROM stdin;
1	France
2	France
\.


--
-- Data for Name: regions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.regions (id, name, country) FROM stdin;
1	Bordeaux Premier Cru - left bank	\N
2	Bordeaux Premier Cru - left bank	2
3	Bordeaux Margaux, France	\N
4	Bordeaux Pessac-Léognan/ Graves	\N
5	Bordeaux Pessac-Léognan/ Graves	\N
6	Bordeaux St Emilion- right bank	\N
7	Bordeaux Pomerols - right bank	2
\.


--
-- Data for Name: wines; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wines (id, name, country_id, region_id, year) FROM stdin;
4	Lafite Rothschild	2	2	2010
5	Lafite Rothschild	2	2	2010
6	Lafite Rothschild	2	2	2003
7	Lafite Rothschild	2	2	1953
8	Lafite Rothschild	2	2	1870
9	Margaux	2	2	1996
10	Margaux	2	2	1990
11	Margaux	2	2	1900
12	Latour	2	2	2010
13	Latour	2	2	2009
14	Latour	2	2	2003
15	Latour	2	2	1982
16	Latour	2	2	1961
17	Haut-Brion	2	2	2009
18	Haut-Brion	2	2	2005
19	Haut-Brion	2	2	1989
20	Haut-Brion	2	2	1961
21	Haut-Brion	2	2	1945
22	Mouton Rothschild	2	2	1945
23	Mouton Rothschild	2	2	1986
24	Mouton Rothschild	2	2	1982
25	Mouton Rothschild	2	2	1959
28	La Mission Haut-Brion	2	5	2010
29	La Mission Haut-Brion	2	5	2009
30	La Mission Haut-Brion	2	5	2005
31	La Mission Haut-Brion	2	5	2000
32	La Mission Haut-Brion	2	5	1989
33	La Mission Haut-Brion	2	5	1961
34	La Mission Haut-Brion	2	5	1959
35	La Mission Haut-Brion	2	5	1955
36	Angelus 	2	6	2005
37	Cheval Blanc	2	6	2010
38	Cheval Blanc	2	6	2009
39	Cheval Blanc	2	6	2005
40	Cheval Blanc	2	6	1998
41	Cheval Blanc	2	6	1947
42	Pavie	2	6	2010
43	Pavie	2	6	2009
44	Pavie	2	6	2005
45	Pavie	2	6	2000
46	Le Pin	2	6	2010
47	Le Pin	2	6	2009
48	Le Pin	2	6	1982
50	Petrus	2	7	2010
51	Petrus	2	7	2009
52	Petrus	2	7	2000
53	Petrus	2	7	1990
54	Petrus	2	7	1989
55	Petrus	2	7	1947
56	Petrus	2	7	1929
57	Petrus	2	7	1921
58	Lafleur	2	7	2005
59	Lafleur	2	7	2000
60	Lafleur	2	7	1982
61	Lafleur	2	7	1950
62	Lafleur	2	7	1947
63	Lafleur	2	7	1945
64	L'Evangile	2	7	2009
65	L'Evangile	2	7	1961
\.


--
-- Name: countries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.countries_id_seq', 2, true);


--
-- Name: regions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.regions_id_seq', 7, true);


--
-- Name: wines_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wines_id_seq', 65, true);


--
-- Name: countries countries_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.countries
    ADD CONSTRAINT countries_pkey PRIMARY KEY (id);


--
-- Name: regions regions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.regions
    ADD CONSTRAINT regions_pkey PRIMARY KEY (id);


--
-- Name: wines wines_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wines
    ADD CONSTRAINT wines_pkey PRIMARY KEY (id);


--
-- Name: regions regions_country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.regions
    ADD CONSTRAINT regions_country_fkey FOREIGN KEY (country) REFERENCES public.countries(id);


--
-- Name: wines wines_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wines
    ADD CONSTRAINT wines_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.countries(id);


--
-- Name: wines wines_region_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wines
    ADD CONSTRAINT wines_region_id_fkey FOREIGN KEY (region_id) REFERENCES public.regions(id);


--
-- PostgreSQL database dump complete
--

