
#include <iostream> 
using namespace std; 

void insort(int arr[], int n) 
{ 
	int i, k, j; 
	for (i = 1; i < n; i++) 
	{ 
		k = arr[i]; 
		j = i - 1; 

		while (j >= 0 && arr[j] > k) 
		{ 
			arr[j + 1] = arr[j]; 
			j = j - 1; 
		} 
		arr[j + 1] = k; 
	} 
} 

void printArray(int arr[], int n) 
{ 
	int i; 
	for (i = 0; i < n; i++) 
		cout << arr[i] << " "; 
	cout << endl; 
}

int main() 
{ 
	int arr[] = { 14, 7, 3, 11, 6 }; 
	int n = sizeof(arr) / sizeof(arr[0]); 

	insort(arr, n); 
	printArray(arr, n); 

	return 0; 
} 

