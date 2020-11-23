set serveroutput on
declare
    num1 number; 
begin
    --for i in 1..5 loop
    for i in reverse 1..5 loop
        dbms_output.put_line('Number is: '||i); 
    end loop;      
end; 
/
set serveroutput off