create database if not exists emr;
use emr;

drop table if exists patient_identity cascade;
drop table if exists patient_examination cascade;
drop table if exists patient_xray cascade;
drop table if exists patient_inbody cascade;
drop table if exists patient_physioterapy cascade;
drop table if exists patient_reception cascade;
drop table if exists patient_payment cascade;
drop table if exists medical_person_classification cascade;
drop table if exists medical_person_notice cascade;
drop table if exists medical_person_identity cascade;

create table if not exists patient_identity(
    patient_id varchar(36) primary key,
    patient_name varchar(60) not null,
    patient_gender varchar(1),
    patient_birthday date not null,
    patient_phone_number varchar(15),
    patient_main_address longtext,
    patient_detail_address longtext,
    patient_residence_number varchar(8) not null
);

create table if not exists medical_person_identity(
    medical_person_id varchar(36) primary key,
    medical_person_name varchar(60) not null,
    medical_person_gender varchar(1),
    medical_person_birthday date not null,
    medical_person_phone_number varchar(15),
    medical_person_main_address longtext,
    medical_person_detail_address longtext,
    medical_person_license longtext
);

create table if not exists patient_examination(
    examination_id varchar(36) primary key,
    patient_id varchar(36) not null,
    medical_person_id varchar(36) not null,
    examination_detail longtext not null,
    examination_datetime datetime not null,
    constraint fk_patient_id
        foreign key (patient_id)
        references patient_identity(patient_id),
    constraint fk_medical_person_id
        foreign key (medical_person_id)
        references medical_person_identity(medical_person_id)
);

create table if not exists patient_inbody(
    inbody_id varchar(36) primary key,
    patient_id varchar(36) not null,
    medical_person_id varchar(36) not null,
    weight float not null,
    muscle_mass float not null,
    body_fat_mass float not null,
    total_body_water float not null,
    protein float not null,
    minerals float not null,
    bmi float not null,
    percent_body_fat float not null,
    right_arm float not null,
    left_arm float not null,
    trunk float not null,
    right_leg float not null,
    left_leg float not null,
    ecw_ratio float not null,
    record_date date not null,
    original_file_location longblob not null,
    constraint fk_patient_id_inbody
        foreign key (patient_id)
        references patient_identity(patient_id),
    constraint fk_medical_person_id_inbody
        foreign key (medical_person_id)
        references medical_person_identity(medical_person_id)
);

create table if not exists patient_xray(
    xray_id varchar(36) primary key,
    patient_id varchar(36) not null,
    medical_person_id varchar(36) not null,
    shooting_timestamp timestamp not null,
    original_xray_location longblob not null,
    constraint fk_patient_id_xray
        foreign key (patient_id)
        references patient_identity(patient_id),
    constraint fk_medical_person_id_xray
        foreign key (medical_person_id)
        references medical_person_identity(medical_person_id)
);

create table if not exists patient_physiotherapy(
    physiotherapy_id varchar(36) primary key,
    patient_id varchar(36) not null,
    medical_person_id varchar(36) not null,
    physiotherapy_record longblob,
    constraint fk_patient_id_physiotherapy
        foreign key (patient_id)
        references patient_identity(patient_id),
    constraint fk_medical_person_id_physiotherapy
        foreign key (medical_person_id)
        references medical_person_identity(medical_person_id)
);

create table if not exists patient_reception(
    reception_id varchar(36) primary key,
    patient_id varchar(36) not null,
    medical_person_id varchar(36) not null,
    reception_timestamp timestamp not null,
    reception_detail longtext,
    constraint fk_patient_id_reception
        foreign key (patient_id)
        references patient_identity(patient_id),
    constraint fk_medical_person_id_reception
        foreign key (medical_person_id)
        references medical_person_identity(medical_person_id)
);

create table if not exists patient_payment(
    payment_id varchar(36) primary key,
    patient_id varchar(36) not null,
    medical_person_id varchar(36) not null,
    payment_status boolean not null,
    payment_datetime datetime,
    payment_kind varchar(10),
    payment_number varchar(36),
    constraint fk_patient_id_payment
        foreign key (patient_id)
        references patient_identity(patient_id),
    constraint fk_medical_person_id_payment
        foreign key (medical_person_id)
        references medical_person_identity(medical_person_id)
);