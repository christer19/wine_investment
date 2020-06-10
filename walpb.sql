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
1	Bordeaux Premier Cru - left bank	1
2	Bordeaux Pessac-Léognan/ Graves	1
3	Bordeaux St Emilion- right bank	2
4	Bordeaux St Emilion- right bank	1
5	Bordeaux Pomerols - right bank	1
\.


--
-- Data for Name: wines; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wines (id, name, country_id, region_id, year) FROM stdin;
1	Lafite Rothschild	1	1	2010
2	Latour	1	1	2016
3	Latour	1	1	2010
4	Latour	1	1	2009
5	Latour	1	1	2003
6	Latour	1	1	1982
7	Haut-Brion	1	1	2016
8	Haut-Brion	1	1	2015
9	Haut-Brion	1	1	2009
10	Mouton Rothschild	1	1	2016
11	Mouton Rothschild	1	1	1982
12	Mouton Rothschild	1	1	1945
13	La Mission Haut-Brion	1	2	2010
15	La Mission Haut-Brion	1	2	2009
18	Cheval Blanc	1	4	2015
19	Cheval Blanc	1	4	2010
20	Cheval Blanc	1	4	2009
21	Cheval Blanc	1	4	1998
22	Pavie 	1	4	2016
23	Pavie 	1	4	2010
24	Pavie 	1	4	2009
25	Le Pin	1	4	2010
26	Le Pin	1	4	2009
17	Cheval Blanc	1	4	2016
27	Petrus	1	5	2016
28	Petrus	1	5	2015
29	Petrus	1	5	2010
30	Petrus	1	5	2009
31	Lafleur	1	5	2015
\.


--
-- Name: countries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.countries_id_seq', 2, true);


--
-- Name: regions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.regions_id_seq', 5, true);


--
-- Name: wines_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wines_id_seq', 31, true);


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

