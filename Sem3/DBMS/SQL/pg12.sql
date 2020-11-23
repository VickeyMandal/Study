set serveroutput on
declare
    i number;

begin
    for i in 1..5 loop
    	if mod(i,2)=0 then
       		dbms_output.put_line('even no. are : '|| i);
       	end if;
    end loop; 
           
end; 
/
set serveroutput off