create table login(names varchar2(20) check(initcap(names)=names), 
                    rollno varchar2(10) unique, 
                    department varchar2(20), 
                    gender varchar2(1) check(gender= 'M' or gender='F'), 
                    course varchar2(20), 
                    userid int primary key, 
                    mobile number(10), 
                    email varchar2(50));

create sequence userid 
start with 1000 
increment by 1;

create table userdetail(rollno varchar2(10),
                        userid int,
                        pass varchar2(25),
                        foreign key(userid) references login(userid));
        
                        
create table eventdetail(userid int,
                        event varchar2(15),
                        foreign key(userid) references login(userid));


create table administrator(userid varchar2(4), pass varchar2(25));
insert into administrator values('rath','rathgamer660');


create table sys_log(loguser varchar2(20),logtime varchar2(80),Operation varchar2(50));

drop table login;
drop sequence userid;
drop table userdetail;
drop table eventdetail;
drop table administrator;
drop table sys_log;

select * from login;
select * from userdetail;
select * from eventdetail;
select *from administrator;
select *from sys_log;

commit

/*T1 Trigger*/
CREATE OR REPLACE TRIGGER system_log_t1_insert
BEFORE INSERT ON login FOR EACH ROW
DECLARE 
    cur_user varchar2(10);
    cur_time varchar2(50);
BEGIN
    SELECT USER INTO cur_user FROM dual;
    select CURRENT_TIMESTAMP INTO cur_time from dual;
    INSERT INTO sys_log VALUES(cur_user,cur_time,'Inserted into Login');
END;

CREATE OR REPLACE TRIGGER system_log_t1_delete
BEFORE DELETE ON login FOR EACH ROW
DECLARE 
    cur_user varchar2(10);
    cur_time varchar2(50);
BEGIN
    SELECT USER INTO cur_user FROM dual;
    select CURRENT_TIMESTAMP INTO cur_time from dual;
    INSERT INTO sys_log VALUES(cur_user,cur_time,'Deleted from Login');
END;

CREATE OR REPLACE TRIGGER system_log_t1_update
BEFORE UPDATE ON login FOR EACH ROW
DECLARE 
    cur_user varchar2(10);
    cur_time varchar2(50);
BEGIN
    SELECT USER INTO cur_user FROM dual;
    select CURRENT_TIMESTAMP INTO cur_time from dual;
    INSERT INTO sys_log VALUES(cur_user,cur_time,'Updated into Login');
END;


/*T2 Trigger*/
CREATE OR REPLACE TRIGGER system_log_t2_insert
BEFORE INSERT ON userdetail FOR EACH ROW
DECLARE 
    cur_user varchar2(10);
    cur_time varchar2(50);
BEGIN
    SELECT USER INTO cur_user FROM dual;
    select CURRENT_TIMESTAMP INTO cur_time from dual;
    INSERT INTO sys_log VALUES(cur_user,cur_time,'Inserted into Userdetail');
END;

CREATE OR REPLACE TRIGGER system_log_t2_delete
BEFORE DELETE ON userdetail FOR EACH ROW
DECLARE 
    cur_user varchar2(10);
    cur_time varchar2(50);
BEGIN
    SELECT USER INTO cur_user FROM dual;
    select CURRENT_TIMESTAMP INTO cur_time from dual;
    INSERT INTO sys_log VALUES(cur_user,cur_time,'Deleted from Userdetail');
END;

CREATE OR REPLACE TRIGGER system_log_t2_update
BEFORE UPDATE ON userdetail FOR EACH ROW
DECLARE 
    cur_user varchar2(10);
    cur_time varchar2(50);
BEGIN
    SELECT USER INTO cur_user FROM dual;
    select CURRENT_TIMESTAMP INTO cur_time from dual;
    INSERT INTO sys_log VALUES(cur_user,cur_time,'Updated into Userdetail');
END;


/*T3 Trigger*/
CREATE OR REPLACE TRIGGER system_log_t3_insert
BEFORE INSERT ON eventdetail FOR EACH ROW
DECLARE 
    cur_user varchar2(10);
    cur_time varchar2(50);
BEGIN
    SELECT USER INTO cur_user FROM dual;
    select CURRENT_TIMESTAMP INTO cur_time from dual;
    INSERT INTO sys_log VALUES(cur_user,cur_time,'Inserted into Eventdetail');
END;

CREATE OR REPLACE TRIGGER system_log_t3_delete
BEFORE DELETE ON eventdetail FOR EACH ROW
DECLARE 
    cur_user varchar2(10);
    cur_time varchar2(50);
BEGIN
    SELECT USER INTO cur_user FROM dual;
    select CURRENT_TIMESTAMP INTO cur_time from dual;
    INSERT INTO sys_log VALUES(cur_user,cur_time,'Deleted from Eventdetail');
END;

CREATE OR REPLACE TRIGGER system_log_t3_update
BEFORE UPDATE ON eventdetail FOR EACH ROW
DECLARE 
    cur_user varchar2(10);
    cur_time varchar2(50);
BEGIN
    SELECT USER INTO cur_user FROM dual;
    select CURRENT_TIMESTAMP INTO cur_time from dual;
    INSERT INTO sys_log VALUES(cur_user,cur_time,'Updated into Eventdetail');
END;