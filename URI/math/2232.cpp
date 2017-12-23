# include <bits/stdc++.h>
/* Mariana Mendes
	Pascal's Triangle - 2232 */ 

int main(){
	int n;
	int ans;
	
	scanf("%d",&n);
	for(int i = 0; i < n ; i++){
		int m;
		scanf("%d",&m);
		m--;
		ans = 0;
		while(m >=0){
			ans += pow(2,m); 
			m--;		
		
		
		};
	
	
	printf("%d\n",ans);
	
	
	};





return 0;}
