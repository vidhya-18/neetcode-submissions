class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
      int[] nos ={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199};
      if(strs == null || strs.length == 0)
       return null;
      Map<Integer,List<String>> map = new HashMap<>();  
      for(String a : strs)
      {
      int prod=1;
      for(int i=0;i<a.length();i++)
      {
      prod*=nos[a.charAt(i)-'a'];
      }
      if(map.containsKey(prod))
      {
        map.get(prod).add(a);
      }
      else
      {
        map.put(prod,new ArrayList<String>());
        map.get(prod).add(a);
      }
      } 
      List<List<String>> result = new ArrayList<List<String>>();
      for( List<String> a : map.values())
      {
        result.add(a);
      }  
      return result;
    }
}
