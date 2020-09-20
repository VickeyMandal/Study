#include<iostream>
using namespace std;

int q[20], mc=10, f=-1, r=-1;

void insertq(int item)
{
	if((f==0 && r==mc-1 || f==r+1))
	{
		cout<<"Overflow";
		return;
	}
	
	if(f==-1)
	{
		f=0;
		r=0;
	}
	else if(r==mc-1)
	{
		r=0;
	}
	else
	{
		r=r+1;
	}
	
	q[r]=item;
	cout<<"inserted: "<<item<<endl;
}

//---------------------------------------------//

void deleteq()
{
	
	if(f==-1)
	{
		cout<<"Underflow";
	}
	
	int item = q[f];
	if(f==r)
	{
		f=-1,r=-1;
	}
	else if(f==mc-1)
	{
		f=0;
	}
	else
	{
		f=f+1;
	}
	cout<<"deleted: "<<item<<endl;
}

//---------------------------------------------//

void display()
{
	int i;
	if(f==r)
	{
		cout<<"Empty";	
		return;
	}	
	else if(f<=r)
	{
		for (i = f; i <= r; i++)
		{ 
            cout<<q[i]<<" "; 
        } 
	}
	else if(r>f)
	{
		for(int j=f;j<mc;j++)
		{
			cout<<q[j]<<" ";
		}
		for(int k=0;k<=r;k++)
		{
			cout<<q[k]<<" ";
		}
	}
	cout<<endl;
}


int main()
{
	insertq(1);
	insertq(2);
	insertq(4);
	insertq(7);
	insertq(3);
	deleteq();
	deleteq();
	insertq(6);
	insertq(5);
	deleteq();
	insertq(8);
	display();
}
