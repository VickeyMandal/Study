import java.util.*;
public class MyComp implements Comparator
{
@Override
public int compare(Object o1, Object o2) {
String s1=(String) o1;
String s2=(String) o2;

if(s1.compareTo(s2)>0)
return -1;
else if(s1.compareTo(s2)<0)
return 1;
else
return 0;
}
}
public class knap
{
public static void main(String[] args) {

Set s=new TreeSet(new MyComp());//collection of homogeneous
Scanner sc=new Scanner(System.in);
for(int i=0;i<5;i++)
{
s.add(sc.nextLine());
}

System.out.println(s);

}
}