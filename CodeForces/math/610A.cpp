# include <bits/stdc++.h>
/* Author: Mariana Mendes.
   Problem 610A  Pasha and Stick*/
   
   
int main(){
	int n;
	int ans =0;
	int tam1 =0;
	
	scanf("%d",&n);
	if(n%2 != 0){
		printf("%d\n",0);
	}else{
		tam1 +=2;
		n-=2;
		while(tam1 < n){
			if(tam1 != n){
				ans++;
			}else{
				break;
			}
			
			tam1 +=2;
			n-=2;
		}
	printf("%d\n",ans);
	}





return 0;}
