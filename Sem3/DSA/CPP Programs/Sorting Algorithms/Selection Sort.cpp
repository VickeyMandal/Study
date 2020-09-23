#include<iostream>
 
using namespace std;

void selsort(int arr[], int n){
	 int loc,temp,min;
	
	for(int i=0;i<n-1;i++)
    {
        min=arr[i];
        loc=i;
        for(int j=i+1;j<n;j++)
        {
            if(min>arr[j])
            {
                min=arr[j];
                loc=j;
            }
            
        }
 		cout<<arr[i]<<" swapped with "<<arr[loc]<<"\n";
        temp=arr[i];
        arr[i]=arr[loc];
        arr[loc]=temp;
    }
}
 
int main()
{
   
    int arr[]={4,6,1,9,5};
    int n=5;
    selsort(arr,n);
 
    cout<<"\nSorted list is as follows\n";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
 
    return 0;
}
