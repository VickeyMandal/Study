set serveroutput on
declare
    n number; 
    f number:=1;
    i number;

begin
	n:=&num;
    for i in 1..n loop
       f:=f*i;
    end loop; 
     dbms_output.put_line('Factorial: '||f);      
end; 
/
set serveroutput off