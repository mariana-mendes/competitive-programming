# include <bits/stdc++.h>


int main(){
	int n;
	int soma;
	
	while(true){
		soma =0;
		scanf("%d",&n);
		if(n == 0){break;};
	
		while(true){
			if(n == 0){
				break;
			};
		
			soma += n*n;
			n--;
		
		};
	
	
	printf("%d\n",soma);
	
	}
return 0;}
