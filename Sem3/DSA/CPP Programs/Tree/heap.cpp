#include<iostream>
using namespace std;
int Tree[50];
int N=0;
void insertHeap(int item){
	N=N+1;
	int ptr=N;
	int par;
	while(ptr>1){
		par=ptr/2;
		if(item<=Tree[par])
		{
			Tree[ptr]=item;
			return;
		}
		Tree[ptr]=Tree[par];
		ptr=par;
	}
	Tree[1]=item;
}


int delHeap(){
	int item = Tree[1];
	int last = Tree[N];
	N=N-1;
	int ptr=1;
	int left=2;
	int right=3;
	while(right<=N){
		if(last>=Tree[left] && last>=Tree[right]){
			Tree[ptr] = last;
			return item;
		}
		if(Tree[right]<=Tree[left]){
			Tree[ptr]=Tree[left];
			ptr=left;
		}
		else{
			Tree[ptr]=Tree[right];
			ptr=right;
		}
		left=2*ptr;
		right=left+1;
	}
	if(left==N && last<=Tree[left]){
		Tree[ptr]=Tree[left];
		ptr=left;
	}
	Tree[ptr]=last;
	return item;
}

void heapsort(){
	int n,temp;
	cout<<"enter how many values: ";
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>temp;
		insertHeap(temp);
	}
	while(N>1){
		int t=delHeap();
		Tree[N+1]=t;
	}
	for(int i=1;i<=n;i++){
		cout<<Tree[i]<<"\n";
	}
	
}


void display(){
	for(int i=1;i<=N;i++){
		cout<<Tree[i]<<"\t";
	}
}

int main(){
	insertHeap(23);
	insertHeap(34);
	insertHeap(64);
	//delHeap();
	display();
	heapsort();
	
}
