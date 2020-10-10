#include<bits/stdc++.h>
using namespace std;
int partition(int arr[],int start,int r)
{
    int pivot=arr[r];
    
    int q=start;
    int i,t;
    
    for(i=start;i<r;i++)
    {
    	if(arr[i]<=pivot)
        {
            t=arr[i];
            arr[i]=arr[q];
            arr[q]=t;
            q++;
			
        }
     }
    
      t=arr[r];
      arr[r]=arr[q];
      arr[q]=t;
    
    
     return q;
 }
 void Quicksort(int arr[],int p,int r)
 {
    if(p<r)
    {
         int q=partition(arr,p,r);
             Quicksort(arr,p,q-1);
             Quicksort(arr,q+1,r);
    }
}
int main()
{
    int n;
        cout<<"Enter number of elements: ";
        cin>>n;
        int arr[n];
        cout<<"Enter the array elements:\n";
        for(int i=0;i<n;i++)
       {
    	 cin>>arr[i];
       }
      Quicksort(arr,0,n-1);
      cout<<"After Quick Sort the array is:\n";
      for(int i=0;i<n;i++)
      {
    	 cout<<arr[i]<<" ";
      }
    return 0;
}


