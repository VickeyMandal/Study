set serveroutput on
declare
    i number;

begin
    for i in (select * from students) loop
    	--if i.name = 'a' then
       		dbms_output.put_line('Name : '|| i.name||' age : '|| i.age);
       	--end if;
    end loop; 
           
end; 
/
set serveroutput off