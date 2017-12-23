# include <bits/stdc++.h>
/* Author: Mariana Mendes.
   Problem 466A Cheap Travel*/
   
 
int main(){
	long int n,m,c,mCust;
	scanf("%ld",&n);
	scanf("%ld",&m);
	scanf("%ld",&c);
	scanf("%ld",&mCust);
	
	long int menor = 0;
	long int aux =0;
	long int tickets;
	tickets = (n/m) + (n%m);
	menor = tickets*mCust;
	
	
	while(tickets > 0){
		tickets--;
		if(tickets*m >= n){
			if(tickets*mCust < menor){
				menor = tickets*mCust;
			}
		}else{
			aux = n-(tickets*m);
			aux = c*aux + tickets*mCust;
			if(aux < menor){
				menor = aux;
			};
		}
	}
	printf("%ld\n",menor);
	
return 0;
}
