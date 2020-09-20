#include<iostream>
using namespace std;

int binary_search(int arr[], int left, int right, int n){
	while(left<=right)
	{
		int mid = left + (right-left)/2;
		 
		if(arr[mid]==n)
		{
			return mid;
		}
		if(arr[mid]<n)
		{
			left = mid+1;
		}
		else
		{
			right = mid-1;
		}
	}
	
	return -1;
};

int main(){
	int n;
	int arr[]={2,3,4,5,6,7,8,9,10};
	int left=0;
	int right = sizeof(arr)/sizeof(arr[0])-1;
	cout<<"Enter a value to Search : ";
	cin>>n;
	int result=binary_search(arr,left,right,n);
	if(result==-1){
		cout<<"Not Found";
	} else {
		cout<<"Found at : "<<result;
	}
}
