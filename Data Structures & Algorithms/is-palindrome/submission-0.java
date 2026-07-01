class Solution {
    public boolean isPalindrome(String s) {
    String org=s.toLowerCase();
    String a=org.replaceAll("[^a-z0-9]","");
    return check(a,0);   
    }
    public boolean check(String arr,int i)
    {
        int n=arr.length();
        if(i==n/2)
          return true;
        if(arr.charAt(i)!=arr.charAt(n-1-i))
          return false;
        return check(arr,i+1);    
    }
}
