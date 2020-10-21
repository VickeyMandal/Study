set serveroutput on
prompt Enter Department number
accept n

declare
	empno empl.no%type;
	ename empl.name%type;
	deptno empl.dept_no%type;
begin
	select no,name,dept_no into empno,ename,deptno from empl where no=&n;
	dbms_output.put_line('Employeeno   :' || empno);
	dbms_output.put_line('Employeename   :' || ename);
	dbms_output.put_line('Departmentno   :' || deptno);
	
end;
/
set serveroutput off
