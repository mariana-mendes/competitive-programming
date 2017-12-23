# include <bits/stdc++.h>

bool isPrime(int n){
	int raiz = ceil(sqrt(n));
	bool eh_primo = true;
	if(n == 2) return eh_primo;
	
	if(n%2 == 0) return false;
		
	for(int i = 2; i < raiz+1; i++){
		if(n%i == 0){
			eh_primo = false;
			break;
		};
	
	
	};
	
	return eh_primo;
};



int main(){
	int n, temp;
	scanf("%d",&n);
	for(int i = 0; i < n; i++){
		scanf("%d",&temp);
		if(isPrime(temp)){
			printf("%s\n","Prime");
		}else{
			printf("%s\n","Not Prime");
			
		};
	
	};




return 0;}
