
class Solution {
    public List<String> letterCombinations(String digits) {
      if (digits.isEmpty()) {
            return new ArrayList<>();
        }  
      return phone("",digits);
    }
    public ArrayList<String> phone(String p, String up)
    {
        if(up.isEmpty())
        {
            ArrayList<String> list = new ArrayList<>();
            list.add(p);
            return list;
        }
         int digit=up.charAt(0)-'0';
         String letter = Letters(digit);
         ArrayList<String> ans = new ArrayList<>();
         for(char ch : letter.toCharArray())
         {
            ans.addAll(phone(p+ch,up.substring(1)));
         }
         return ans;
    }

  public static   String Letters(int digit)
    {
        switch(digit)
        {
            case 2: return "abc";
            case 3: return "def";
            case 4: return "ghi";
            case 5: return "jkl";
            case 6: return "mno";
            case 7: return "pqrs";
            case 8: return "tuv";
            case 9: return "wxyz";
            default: return "";
        }
    }
}
