# include <bits/stdc++.h>
/* Author: Mariana Mendes.
   Problem 617A  Elephant*/
   
   
int main(){
	unsigned long long int dist;
	unsigned long long int ans = 0;
	int maxMove = 5;
	
	scanf("%llu",&dist);
	while(dist != 0){
		if(dist >= maxMove){
			dist -= maxMove;
			ans+=1;
		}else{
			maxMove--;

		};
	};


	printf("%llu\n",ans);

return 0;}
