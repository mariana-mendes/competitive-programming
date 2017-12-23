# include <bits/stdc++.h>
/* Author: Mariana Mendes.
   Problem 617B  Chocolate*/


int main(){
	int n;
	scanf("%d",&n);
	
	int choc[n];
	for(int i = 0; i < n; i++){
		scanf("%d",&choc[i]);	
	};
	

	int index = 0;
	bool find = false;
	unsigned long long int count = 0;
	unsigned long long int ans = 1;
	bool resp = false;
	
	while(index < n){
		find = false;
		if(choc[index] == 1){
			resp = true;
			count++;
			index++;
			while(index < n){
				if(choc[index] == 1){
					find = true;
					break;
				};
				
				count++;
				index++;	
			};
			
			
			if(find){
				ans*= count;	
				count = 0;
			};
			
		}else{
			index++;
		};
		
	
	};
	
	
	if(resp){
		printf("%llu\n",ans);
	}else{
		printf("%d\n",0);
	};
	

return 0;}
