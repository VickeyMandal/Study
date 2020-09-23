#include<iostream>
using namespace std;

void bubblesort(int arr[], int n){
	int temp;
	bool swapped;
	int count=0;
	for(int i=0;i<n;i++)
	{
		swapped=false;
		for(int j=0;j<n-1;j++)
		{
				if(arr[j]>arr[j+1])
				{
					temp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=temp;
					count++;
				}
						
		}
			
			if(swapped==false)
				break;
	}
	cout<<"Swapped "<<count<<" times\n";
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
	bubblesort(arr,n);
	display(arr,n);
	
}
