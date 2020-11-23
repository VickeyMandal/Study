create or replace procedure totalsale(cid in number,tot out number)
is
p sale.price%type;
t number := 0;
cursor cur_sale is
select price from sale where customerid=cid;
begin
open cur_sale;
loop
fetch cur_sale into p;
if cur_sale%ROWCOUNT = 0 then
raise_application_error(20020,'No data found');
end if;
exit when cur_sale%NOTFOUND;
t := t + p;
end loop;
close cur_sale;

tot := t;

exception
when others then
raise_application_error(20001,'As error was encountered');
end totalsale;
/