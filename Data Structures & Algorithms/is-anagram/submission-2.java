class Solution {
    public boolean isAnagram(String s, String t) {
    int[] ind1 = new int[26];
    int[] ind2 = new int[26];
    for(int i=0;i<s.length();i++)
    {

        int index = s.charAt(i) - 'a';
        ind1[index]++;
    }
    for(int i=0;i<t.length();i++)
    {

        int index = t.charAt(i) - 'a';
        ind2[index]++;
    }
    for(int i=0;i<26;i++)
    {
        if(ind1[i]!=ind2[i])
        {
         return false;
        }
    }
    return true;
    }
}
