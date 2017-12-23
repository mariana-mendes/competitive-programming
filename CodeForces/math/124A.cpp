# include <bits/stdc++.h>
/* Author: Mariana Mendes.
   Problem 124A  The number of positions*/
   
   
   
int main(){
	int n,a,b;
	int ans =1;
	scanf("%d %d %d",&n,&a,&b);
	
	if(a+b == n) b--;
	
	
	b--;
	a++;
		
	while(b >= 0 && a < n){
		ans += 1;
		b--;
		a++;
	};
	
	printf("%d\n",ans);	

return 0;}
