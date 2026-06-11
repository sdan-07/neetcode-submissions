class Solution {
    public boolean isAnagram(String s, String t) {

        Map<Character, Integer> Smap = new HashMap<>();
        Map<Character, Integer> Tmap = new HashMap<>();

        for (char c: s.toCharArray())
            Smap.put(c, Smap.getOrDefault(c, 0)+1);
        
        for (char c: t.toCharArray())
            Tmap.put(c, Tmap.getOrDefault(c, 0)+1);

        if(Smap.equals(Tmap))
            return true;

        return false;

        
    }
}
