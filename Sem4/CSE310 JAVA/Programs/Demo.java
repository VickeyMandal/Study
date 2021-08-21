import java.util.*;

class MyComparator implements Comparator
{
    @Override
    public int compare(Object o1, Object o2) {
    String i1=(String) o1;
    String i2=(String) o2;

    if(i1.compareTo(i2)<0)
        return 1;
    else if(i1.compareTo(i2)>0)
        return -1;
    else
        return 0;
    }
}
public class Demo
{
    public static void main(String[] args) {

        Set s=new TreeSet(new MyComparator());//collection of homogeneous

        s.add("Red");
        s.add("Green");
        s.add("Blue");

        System.out.println(s);

    }
}