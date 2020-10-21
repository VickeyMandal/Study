set serveroutput on
DECLARE 
   a integer := 10; 
   b integer := 20; 
   c integer; 
   f integer; 
BEGIN 
   c := a + b; 
   dbms_output.put_line('Add: ' || c); 
   f := 30/3; 
   dbms_output.put_line('Division: ' || f); 
END; 
/
set serveroutput off
