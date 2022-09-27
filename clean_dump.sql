--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Homebrew)
-- Dumped by pg_dump version 14.5 (Homebrew)

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

SET default_table_access_method = heap;

--
-- Name: companies; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.companies (
    id character varying NOT NULL,
    name character varying NOT NULL,
    cif character varying(10) NOT NULL,
    email character varying NOT NULL,
    telephone bigint NOT NULL
);


--
-- Name: company_employee_contract_info; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.company_employee_contract_info (
    id character varying NOT NULL,
    company_id character varying NOT NULL,
    employee_id character varying NOT NULL,
    currently_employed boolean DEFAULT false NOT NULL,
    date_joined date NOT NULL,
    date_left date,
    hours_to_work_weekly smallint NOT NULL,
    salary_annum_gross integer NOT NULL,
    job_title character varying NOT NULL,
    social_security_nmbr integer NOT NULL
);


--
-- Name: employee_hour_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.employee_hour_log (
    id character varying NOT NULL,
    employee_id character varying NOT NULL,
    sign_in timestamp without time zone NOT NULL,
    sign_out timestamp without time zone,
    work_day date NOT NULL,
    company_id character varying NOT NULL,
    total_hours smallint
);


--
-- Name: task_app; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.task_app (
    id character varying NOT NULL,
    employee_id character varying NOT NULL,
    assigned_by_id character varying NOT NULL,
    title character varying NOT NULL,
    description character varying,
    is_completed boolean NOT NULL,
    company_id character varying NOT NULL,
    due_date date
);


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id character varying NOT NULL,
    name character(20) NOT NULL,
    surname character(20) NOT NULL,
    dni character varying NOT NULL,
    company_id character varying NOT NULL,
    is_admin boolean NOT NULL,
    password character varying NOT NULL,
    email character varying NOT NULL
);


--
-- Data for Name: companies; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.companies (id, name, cif, email, telephone) FROM stdin;
1111	test company	1111	test@company.com	11111
\.


--
-- Data for Name: company_employee_contract_info; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.company_employee_contract_info (id, company_id, employee_id, currently_employed, date_joined, date_left, hours_to_work_weekly, salary_annum_gross, job_title, social_security_nmbr) FROM stdin;
\.


--
-- Data for Name: employee_hour_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.employee_hour_log (id, employee_id, sign_in, sign_out, work_day, company_id, total_hours) FROM stdin;
\.


--
-- Data for Name: task_app; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.task_app (id, employee_id, assigned_by_id, title, description, is_completed, company_id, due_date) FROM stdin;
11111	1111	1111	title	kjdsnvlkdsnf ksldf jklsjf sdlf  ksdlfj kdslfjs  kslflksf	f	1111	2022-09-25
d7dbbc68-3deb-11ed-b2d4-f45c89c1d84f	1111	1111	title	kjdsnvlkdsnf ksldf jklsjf sdlf  ksdlfj kdslfjs  kslflksf	f	1111	2022-09-25
f70ddf4e-3deb-11ed-b2d4-f45c89c1d84f	1111	1111	fffff	fffff	f	1111	2022-09-22
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (id, name, surname, dni, company_id, is_admin, password, email) FROM stdin;
1111	test\n               	employee\n           	1111	1111	t	password	test@user.com\n
f46bf44c-3c51-11ed-b213-f45c89c1d84f	harsh               	singh               	xddsv2	1111	t	pbkdf2:sha256:260000$4nfzu2EzKYW4QZqC$895e0a8d408684484245be17447732ef3a39d1a6d5e692549a7037f1d4cb7793	harsh@email.com
c0d6f55e-3c52-11ed-a3d4-f45c89c1d84f	harsh               	singh               	xddsv21	1111	t	pbkdf2:sha256:260000$g2daEl4RbVDYQ6cc$78c562b74a3db7f5b670bc741e258eae6fd7e3da4a6be92183d85250042b4d63	harsh2@email.com
d38f6284-3d20-11ed-85d2-f45c89c1d84f	vue                 	client              	22121	1111	t	pbkdf2:sha256:260000$JWPwgqUsux6Wpzn3$b1ca4819e1d7aabafc181ffabfe8743e531a4629b9893571582af6a239a6db2c	vue@email.com
01ae23b2-3d2b-11ed-85d2-f45c89c1d84f	harsh               	harsh               	11111111	1111	t	pbkdf2:sha256:260000$ebQ7wgBHTEGrA9qD$d71bf8367875dd81a427afd2014479041a35b4f790b5afffe108300b3bb616e0	harsh@harsh.com
135a2e1a-3d2d-11ed-85d2-f45c89c1d84f	boot                	strap               	2334	1111	f	pbkdf2:sha256:260000$89Ay8ByVflsRDNCL$738a1a39511e95ca3037335e62a69dc3fc95fb42f3986688661fab04d31c0478	boot@strap.com
ce2ac404-3d76-11ed-97cb-f45c89c1d84f	matias              	guapo               	23e2423	1111	t	pbkdf2:sha256:260000$m1PL2zbBrgPt8CUU$0b9061c2a2f87b66bf1041b2a74fa1452fc87f20793b706a8263844990ed2446	matias@guapo.com
\.


--
-- Name: companies companies_id_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_id_pk PRIMARY KEY (id);


--
-- Name: companies companies_info_un; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_info_un UNIQUE (name, cif, email, telephone);


--
-- Name: company_employee_contract_info company_employee_contract_info_id_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.company_employee_contract_info
    ADD CONSTRAINT company_employee_contract_info_id_pk PRIMARY KEY (id);


--
-- Name: employee_hour_log employee_hour_log_id_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.employee_hour_log
    ADD CONSTRAINT employee_hour_log_id_pk PRIMARY KEY (id);


--
-- Name: task_app task_app_id_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.task_app
    ADD CONSTRAINT task_app_id_pk PRIMARY KEY (id);


--
-- Name: users users_dni_un; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_dni_un UNIQUE (dni);


--
-- Name: users users_email_un; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_un UNIQUE (email);


--
-- Name: users users_id_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_id_pk PRIMARY KEY (id);


--
-- Name: company_employee_contract_info company_employee_contract_info_company_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.company_employee_contract_info
    ADD CONSTRAINT company_employee_contract_info_company_id_fk FOREIGN KEY (id) REFERENCES public.companies(id);


--
-- Name: company_employee_contract_info company_employee_contract_user_id_info_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.company_employee_contract_info
    ADD CONSTRAINT company_employee_contract_user_id_info_fk FOREIGN KEY (employee_id) REFERENCES public.users(id);


--
-- Name: employee_hour_log employee_hour_log_company_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.employee_hour_log
    ADD CONSTRAINT employee_hour_log_company_id_fk FOREIGN KEY (company_id) REFERENCES public.companies(id);


--
-- Name: employee_hour_log employee_hour_log_user_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.employee_hour_log
    ADD CONSTRAINT employee_hour_log_user_id_fk FOREIGN KEY (employee_id) REFERENCES public.users(id);


--
-- Name: task_app task_app_admin_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.task_app
    ADD CONSTRAINT task_app_admin_id_fk FOREIGN KEY (assigned_by_id) REFERENCES public.users(id);


--
-- Name: task_app task_app_company_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.task_app
    ADD CONSTRAINT task_app_company_id_fk FOREIGN KEY (company_id) REFERENCES public.companies(id);


--
-- Name: task_app task_app_employee_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.task_app
    ADD CONSTRAINT task_app_employee_id_fk FOREIGN KEY (employee_id) REFERENCES public.users(id);


--
-- Name: users users_company_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_company_id_fk FOREIGN KEY (company_id) REFERENCES public.companies(id);


--
-- PostgreSQL database dump complete
--

