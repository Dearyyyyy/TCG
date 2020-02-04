# coding=utf-8
public class lianxi {
	public static void main(String[] args) {
		Solution S = new Solution();
		String A = "abced";
		String B = "cdeab";
		boolean a = S.rotateString(A, B);
		System.out.println(a);
	}
}
class Solution {
    public boolean rotateString(String A, String B) {
        if(A.length() != B.length()){
            return false;
        }
        if(A.length() == 0){
            return true;
        }
        B += B;
        for(int i=0; i<B.length(); i++){
        	if(B.charAt(i) == A.charAt(0)){
        		int k = i+1;
        		for(int j=1; j<A.length() && k<B.length(); j++){
        			if(A.charAt(j) != B.charAt(k)){
                        break;
                    }
        					
        			k++;
        		}
        		if(k == i+A.length()){
                    return true;
                }			
            }	
        }
        return false;   
    }      
}

s1,s2=input().split()
while s1:
    if Solution.rotateString(s1, s2):
        print("YES")
    else:
        print("NO")
    s1,s2=input().split()