class Capital extends Thread
{
    public void run()
    {
        char ch='A';
        for(int i=0;i<26;i++)
            System.out.println(ch++);
    }
}
class Small extends Thread
{
    public void run()
    {
        char ch='a';
        for(int i=0;i<26;i++)
            System.out.println(ch++);
    }
}
class Demo
{
    public static void main(String[] args) {
        Thread t1=new Thread(new Capital());
        Thread t2=new Thread(new Small());
        t1.start();
        t2.start();
    }
}