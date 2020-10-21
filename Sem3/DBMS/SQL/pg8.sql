set serveroutput on
declare
  
-- declare variable num1, num2  
-- and temp of datatype number 
    num1 number; 
    num2 number; 
    temp number; 
  
   
begin
    num1:=7; 
    num2:=9; 
      
    -- print result before swapping 
    dbms_output.put_line('before'); 
    dbms_output.put_line('num1 = '|| num1 ||' num2 = '|| num2); 
      
    -- swapping of numbers num1 and num2 
    num1:=num1+num2;
    num2:=num1-num2;
    num1:=num1-num2;
   -- print result after swapping 
    dbms_output.put_line('after'); 
    dbms_output.put_line('num1 = '|| num1 ||' num2 = '|| num2); 
      
end; 
/
set serveroutput off