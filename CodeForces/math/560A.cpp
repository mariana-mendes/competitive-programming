# include <bits/stdc++.h>
# include <algorithm>
/* Author: Mariana Mendes.
   Problem 560A  Currency System in Geraldion*/
   
   
 using namespace std;
int main(){
	int n;
	scanf("%d",&n);
	int a[n];
	
	for(int i = 0; i < n; i++){
		scanf("%d",&a[i]);
	
	};
	
	sort(a,a+n);
	
	if(a[0] == 1){
		printf("%d\n",-1);
	
	}else{
		printf("%d\n",1);
	
	};
	
	




return 0;}
