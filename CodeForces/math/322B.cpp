# include <bits/stdc++.h>
/* Mariana Mendes
   322B - Ciel and Flowers */ 


int main(){	
	int r,g,b;
	int ans = 0;
	bool achouZ = false; 
	scanf("%d %d %d", &r,&g,&b);

	if(r == 0 || g == 0|| b == 0){achouZ = true;};

	ans += r/3;
	ans += g/3;
	ans += b/3;
	
	r -= r-(r%3);
	g -= g-(g%3);
	b -= b-(b%3);

	while(r > 0 && g > 0 && b > 0){
		r--;
		g--;
		b--;
		ans++;
	};
	
	if(!achouZ){
	
	if(r+g+b > 3 && r+g+b < 6){ans+= 1;};
	
	if(r+g+b == 6){
		ans+= 2;
		
		};};
			printf("%d\n",ans);
	
	return 0;
	
	
	
	};
