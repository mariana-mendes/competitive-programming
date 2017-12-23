# include <bits/stdc++.h>

/* Mariana Mendes
   822A - I'm bored with life */

int fat(int n){
	if(n == 1 || n == 0){
		return 1;
	}else{
		return fat(n-1)*n;
	};
};



int main(){
	int m,n;
	int ans;
	scanf("%d %d",&m, &n);
	
	if(m > n){
		ans = fat(n);
	
	}else{
		ans = fat(m);
	};

	printf("%d\n",ans);
	

return 0;

}
