DROP table disk_copy;
create table disk_copy as select * from disk;
delete from disk_copy;
select * from disk_copy;

DO $$
 DECLARE
     m_disk_id   disk_copy.disk_id%TYPE;
     m_type disk_copy.type%TYPE;

 BEGIN
     m_disk_id := 100;
     m_type := 'SSD';
     FOR i IN 6..12
         LOOP
            INSERT INTO disk_copy (capacity, type, disk_id)
             VALUES (power(2,i) || ' GB', m_type, m_disk_id + i - 6);
         END LOOP;
 END;
 $$;
 
 select * from disk_copy;


