create trigger undemployee
	before update on empt
		for each row 
		 begin
		insert into oldemp values(:old.eid,:old.ename,:old.did,:old.dptname,:old.location);
end;
/