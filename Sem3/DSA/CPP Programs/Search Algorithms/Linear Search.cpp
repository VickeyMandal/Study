#include<iostream>
using namespace std;

void linearsearch(int arr[],int arrsize, int n){
	int flag = -1;
	for(int i=0; i<arrsize; i++)
	{
		if(arr[i]==n)
		{
			flag = 1;
			cout<<"Found at : "<<i;
			break;
		}
	}
	
	if(flag==-1)
	{
		cout<<"Not found";
	}
		
}

int main(){
	int n;
	int arr[]={2,4,6,1,32,67,54};
	int arrsize=sizeof(arr)/sizeof(arr[0]); 
	cout<<"Enter a number search : ";
	cin>>n;
	linearsearch(arr,arrsize,n);
}
