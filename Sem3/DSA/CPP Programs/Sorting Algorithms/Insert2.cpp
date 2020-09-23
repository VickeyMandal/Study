#include<iostream>
using namespace std;

void insertsort(int arr[], int n)
{
	for(int i=1;i<n;i++)
	{
		int key=arr[i];
		int j=i-1;
		
		while(j>=0 && arr[j]>key)
		{
			arr[j+1]=arr[j];
			j=j-1;
		}
		arr[j+1]=key;
		
	}
}

void display(int arr[], int n){
	cout<<"Sorted array : ";
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
}

int main(){
	int arr[]={1,2,3,4,6,5};
	int n= sizeof(arr)/sizeof(arr[0]);
	insertsort(arr,n);
	display(arr,n);
}
