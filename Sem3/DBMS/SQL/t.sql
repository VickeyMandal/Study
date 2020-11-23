set serveroutput on
DECLARE
num number;
fn number;

FUNCTION fx(x number)
RETURN number
IS
f number;
BEGIN
IF x=0 THEN
f := 1;
ELSE
f := x * fx(x-1);
END IF;
RETURN f;
END;
/
set serveroutput off